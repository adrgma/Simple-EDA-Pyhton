import pandas as pd
import numpy as np
import io
import pandas_profiling

df_retail = pd.read_csv('retail_raw_reduced_data_quality.csv')
print(df_retail.head())
print(df_retail.dtypes)

length_city = len(df_retail['city'])
print('Length kolom city:', length_city)

count_city = df_retail['city'].count()
print('Count kolom count_city:', count_city)

number_of_missing_values_city = length_city - count_city
float_of_missing_values_city = float(number_of_missing_values_city/length_city)
pct_of_missing_values_city = '{0:.1f}%'.format(float_of_missing_values_city * 100)
print('Persentase missing value kolom city:', pct_of_missing_values_city)


print('Kolom quantity')
print('Minimum value: ', df_retail['quantity'].min())
print('Maximum value: ', df_retail['quantity'].max())
print('Mean value: ', df_retail['quantity'].mean())
print('Mode value: ', df_retail['quantity'].mode())
print('Median value: ', df_retail['quantity'].median())
print('Standard Deviation value: ', df_retail['quantity'].std())
print(df_retail['quantity'].quantile([0.25, 0.5, 0.75]))

print('Korelasi quantity dengan item_price')
print(df_retail[['quantity', 'item_price']].corr())

report = pandas_profiling.ProfileReport(df_retail)
report.to_file(output_file = 'report.html')

print('Check kolom yang memiliki missing data:')
print(df_retail.isnull().any())

print('\nFilling the missing value (imputasi):')
print(df_retail['quantity'].fillna(df_retail.quantity.mean()))

print('\nDrop missing value:')
print(df_retail['province'].dropna())

# Q1, Q3, dan IQR
Q1 = df_retail['quantity'].quantile(0.25)
Q3 = df_retail['quantity'].quantile(0.75)
IQR = Q3 - Q1

# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('Shape awal: ', df_retail.shape)

# Removing outliers
df_retail = df_retail[~((df_retail['quantity'] < (Q1 - 1.5 * IQR)) | (df_retail['quantity'] > (Q3 + 1.5 * IQR)))]

# Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', df_retail.shape)

#Check ukuran (baris dan kolom) sebelum data duplikasi dibuang
print('Shape awal: ', df_retail.shape)


#Buang data yang terduplikasi
df_retail.duplicated(subset=None)
df_retail.drop_duplicates(inplace=True)

#Check ukuran (baris dan kolom) setelah data duplikasi dibuang
print('Shape akhir: ', df_retail.shape)