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

df=df.dropna(subset=["Fechas"])
# print(df)


df["Ventas"]=df["Ventas"].fillna(df["Ventas"].mean())
print(df)








