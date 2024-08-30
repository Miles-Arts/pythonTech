import pandas as pd
import numpy as np


data={
    "Fechas": ["2024-01-01", "2024-01-02", np.nan,"2024-01-02","2024-01-03", "2024-01-03"],
    "Ventas": [100,200,200, np.nan, 150, 150],
    "Vendedores": ["Juan", np.nan, "Ana", "Juan", "Ana", "Ana"],
    "Ciudades": ["Cuauta", "Cucuta", "Bogota", "Cucuta", "Cucuta", "Cucuta"]
}

df=pd.DataFrame(data)
# print(df)

# print(df.isnull().sum())

df_dropped=df.dropna()
# print(df_dropped)

# df=df.dropna(subset=["Fechas"])
# print(df)

# df_cleaned=df.dropna(axis=1)
# # print(df_cleaned)

# df["Ventas"]=df["Ventas"].fillna(df["Ventas"].mean())
# # print(df)

# df["Vendedores"]=df["Vendedores"].fillna(df["Vendedores"].mode()[0])
# # print(df)

print("-"*60)

df["Vendedores"].fillna("Carlos", inplace=True)
# df=df.drop_duplicates()
print(df)

# df["Fechas"]=pd.to_datetime(df["Fechas"])
# # print(df["Fechas"])
# # # print(df.info())

# df["Ventas"]=df["Ventas"].astype(int)
# print(df["Ventas"])


# df["Ciudades"]=df["Ciudades"].astype("category")
# # print(df["Ciudades"])

# print(df.dtypes)


# df.replace({"Cucuta": "Cúcuta"}, inplace=True)
# print(df)


# df.rename(columns={"Ventas": "Total/Ventas"}, inplace=True)
# print(df)

df.drop(columns=["Ciudades"], inplace=True)
print(df)

df.replace(200, 300, inplace=True)
print(df)
