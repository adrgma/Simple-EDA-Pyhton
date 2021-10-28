import pandas as pd
import numpy as np
import io
import pandas_profiling

# df_positif = pd.read_csv('positif rate.csv', sep=';')
# print(df_positif.head())
# print(df_positif.columns)
# report = pandas_profiling.ProfileReport(df_positif)
# report.to_file(output_file = 'report.html')

df_positif = pd.read_csv('source_data.csv', sep=';')
print(df_positif.head())
# # print(df_positif.columns)
# report = pandas_profiling.ProfileReport(df_positif)
# report.to_file(output_file = 'report.html')

# # print(df_positif.mean())
# # print(df_positif.var())
# # print(df_positif.corr())
# # print(df_positif.cov())


