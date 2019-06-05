# -*- coding: utf-8 -*-

from two_point_hospital.df_int import df_to_list_table
from two_point_hospital.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "staff-skill.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")

lt_staff_skill = df_to_list_table(df=df, title="员工技能列表")

if __name__ == "__main__":
    print(lt_staff_skill.render())
