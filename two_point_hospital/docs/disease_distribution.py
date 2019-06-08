# -*- coding: utf-8 -*-

import random
from two_point_hospital.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "disease-diagnose-and-treatment.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
columns = [
    "疾病",
    "全科",
    "综合诊断", "心脏病科", "病房", "精神科", "体液分析", "X光", "磁共振", "DNA",
    "重访全科"
]
all_rooms = columns[1:-1]
columns_percentage_type = columns[1:]
columns_secondary_diagnose = columns[2:-1]

# 将百分比字符串数据转化成小数
for c in columns_percentage_type:
    df[c] = df[c].apply(lambda x: float(x[:-1]) / 100)

df.index = df["疾病"]
df = df.sort_values("全科", ascending=True)  # 从

# 计算每个疾病的最二级诊所列表
ignore_x_raw = True  # 由于 X光 可以不造, 因为任何病 X光 最多只是和其他房间并列最优
disease_room_candidate = dict()
for _, row in df.iterrows():
    disease = row["疾病"]
    l = [
        (room, row[room])
        for room in columns_secondary_diagnose
    ]
    max_rate = max([rate for _, rate in l])
    if ignore_x_raw:
        room_candidate = [room for room, rate in l if ((rate == max_rate) and (room != "X光"))]
    else:
        room_candidate = [room for room, rate in l if rate == max_rate]
    disease_room_candidate[disease] = room_candidate

n_disease = df.shape[0]


class Config(object):
    # 全科诊断室 按照 5 级全科技能
    # 磁共振 按照 1 级放射 4 级诊断
    # DNA 按照 1 级 DNA, 4 级治疗
    # 病房和精神病科按照 5 级别 病房管理 或 精神病学
    # 综合诊断, 心脏病科, 体液分析 按照 5 级诊断
    员工级别 = 1
    全科药柜数量 = 0  # 全科单独拿出来, 因为可以全科堆大量药柜尽量保证一次诊断成功
    诊断室药柜数量 = 0  # 对 病房, 精神病室, 综合诊断, 心脏病科 有效, 假设数量都一样

    诊断室器材升级 = 0  # 最高 2, 对 综合诊断, 心脏病科, 体液分析, 磁共振, DNA 有效

    每种疾病的病人人数 = 1000
    治疗所需最低诊断 = 0.9

    def __init__(self):
        self.counts = {
            room: 0
            for room in all_rooms
        }

    @property
    def 全科诊断加成(self):
        医生加成 = 0.7 + self.员工级别 * 0.1 + self.员工级别 * 0.2
        药柜加成 = 1 + self.全科药柜数量 * 0.01
        return 医生加成 * 药柜加成

    @property
    def 综合和心脏病科诊断加成(self):
        护士加成 = 0.7 + self.员工级别 * 0.1 + self.员工级别 * 0.1
        药柜加成 = 1 + self.诊断室药柜数量 * 0.01
        器材加成 = 1 + 0.25 * self.诊断室器材升级
        return 护士加成 * 药柜加成 * 器材加成

    @property
    def 病房或精神病诊断加成(self):
        """
        计算公式和全科一样, 因为都是每级20%
        """
        return self.全科诊断加成

    @property
    def 体液分析诊断加成(self):
        护士加成 = 0.7 + self.员工级别 * 0.1 + self.员工级别 * 0.1
        器材加成 = 1 + 0.25 * self.诊断室器材升级
        return 护士加成 * 器材加成

    @property
    def 磁共振诊断加成(self):
        医生加成 = 0.7 + self.员工级别 * 0.1 + (self.员工级别 - 1) * 0.1
        器材加成 = 1 + 0.25 * self.诊断室器材升级
        return 医生加成 * 器材加成

    @property
    def DNA诊断加成(self):
        医生加成 = 0.7 + self.员工级别 * 0.1  # 因为一般 DNA 里面的医生全加治疗, 因为治疗很难
        器材加成 = 1 + 0.25 * self.诊断室器材升级
        return 医生加成 * 器材加成

    @property
    def 一次诊断直接治疗所需全科基础诊断率(self, 送诊最低概率=0.9):
        return 送诊最低概率 / self.全部加成

    def simulate(self, 送诊最低概率=0.9):
        """
        模拟大量随机病人进入医院, 造访所有房间的次数.
        """
        multiplier_mapper = {
            "全科": self.全科诊断加成,
            "综合诊断": self.综合和心脏病科诊断加成,
            "心脏病科": self.综合和心脏病科诊断加成,
            "体液分析": self.体液分析诊断加成,
            "病房": self.病房或精神病诊断加成,
            "精神科": self.病房或精神病诊断加成,
            "磁共振": self.磁共振诊断加成,
            "DNA": self.DNA诊断加成,
        }

        patient_id = 0
        patient_passed_room = {
            i: 0
            for i in range(1, 1 + self.每种疾病的病人人数 * n_disease)
        }
        room_visited = {
            room: 0
            for room in all_rooms
        }

        for disease, row in df.iterrows():
            row = dict(row)
            for _ in range(self.每种疾病的病人人数):
                patient_id += 1

                # 一个实际的病人样本诞生
                current_diagnose_perc = 0  # 用于监视当前总诊断率

                current_diagnose_perc += (row["全科"] * multiplier_mapper["全科"])
                room_visited["全科"] += 1
                patient_passed_room[patient_id] += 1

                for _ in range(10):
                    if current_diagnose_perc < 送诊最低概率:
                        room_candidate = disease_room_candidate[disease]
                        room = random.choice(room_candidate)

                        current_diagnose_perc += (row[room] * multiplier_mapper[room])  # 访问二级诊端室
                        current_diagnose_perc += (row["重访全科"] * multiplier_mapper["全科"])  # 回访全科
                        patient_passed_room[patient_id] += 2
                        room_visited[room] += 1
                        room_visited["全科"] += 1
                    else:
                        patient_passed_room[patient_id] += 1  # 前往治疗
                        try:
                            room_visited[row["科室"]] += 1
                        except:
                            room_visited[row["科室"]] = 1
                        break
                # break
            # break

        # reformat room_visited
        total_visits = sum(list(room_visited.values()))
        room_visited["全科初诊"] = n_disease * self.每种疾病的病人人数
        room_visited["全科返诊"] = room_visited["全科"] - n_disease * self.每种疾病的病人人数
        for key, value in sorted(room_visited.items(), key=lambda x: x[1], reverse=True):
            perc_text = "%.2f%%" % (value * 1.0 / total_visits * 100,)
            print("%s\t%s" % (key, perc_text))


Config.员工级别 = 5
Config.全科药柜数量 = 15
Config.诊断室药柜数量 = 10
Config.诊断室器材升级 = 2
Config.每种疾病的病人人数 = 1000

config = Config()
config.simulate()
