import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("order.csv")

# melihat isi file
print(order_df)

# melihat struktur dari file order.csv
print(order_df.shape)

# tampilkan beberapa data menggunakan Head dan Tail
print(order_df.head(10))
print(order_df.tail(10))

# Statistik Deskriptif
print(order_df.describe())

# Median dari total pembelian konsumen per transaksi price
print(order_df.loc[:, "price"].median())

# plot histogram sederhana untuk kolom: price
order_df[["price"]].hist(figsize=(5, 6), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()

# Standar variasi product_weight_gram
order_df.loc[:, "product_weight_gram"].std()

# Varians product_weight_gram
order_df.loc[:, "product_weight_gram"].var()

# Menemukan Outlier dari data
# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range
IQR = Q3 - Q1
print(IQR)

# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)

# rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)

# sortir dari harga maksimum
sort_harga = order_df.sort_values(by="price", ascending=True)
print(sort_harga)

