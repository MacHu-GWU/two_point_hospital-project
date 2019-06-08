# -*- coding: utf-8 -*-

from two_point_hospital.df_int import df_to_list_table
from two_point_hospital.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "disease-diagnose-and-treatment.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")

lt_disease_diagnose_and_treatment = df_to_list_table(df=df, title="疾病的诊断和治疗数据")

if __name__ == "__main__":
    # print(lt_disease_diagnose_and_treatment.render())

    print(df["全科"][0])