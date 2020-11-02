# -*- coding: utf-8 -*-

from two_point_hospital.df_int import df_to_list_table
from two_point_hospital.tsv_gz import make_gzip, read_compressed_tsv

tsv_filename = "general-diagnose-one-time-visit-drug-cabinet-threshold.tsv"
make_gzip(this_file=__file__, filename=tsv_filename)
df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")

lt_general_diagnose_one_time_visit_drug_cabinet_threshold = df_to_list_table(df=df, title="全科一次确诊药柜阈值")

if __name__ == "__main__":
    print(df)