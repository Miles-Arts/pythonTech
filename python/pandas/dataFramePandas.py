import pandas as pd
import numpy as np
# datos1=[
#     [1, "Ana"],
#     [2, "Juan"],
#     [3, "Maria"]
# ]

# # print(datos)

# df1=pd.DataFrame(datos1, index=["a", "b", "c"], columns=["ID", "Nombre"])
# print(df1)

# print("-"*60)

# datos2={"ID":[1,2,3], "Nombre": ["Ana", "Juan", "Maria"]}
# df2=pd.DataFrame(datos2)
# print(df2)

# nombres=pd.Series(["Ana", "Juan", "Maria"])
# edades=pd.Series([10, 15, 20])
# ciudades=pd.Series(["Bogota", "Cucuta", "Medellin"])

# df4=pd.DataFrame({"Nombres": nombres, "Edades": edades, "Ciudades": ciudades})
# print(df4)

print("-"*60)

datos={
    "Dia": ["Lunes", "Martes", "Miercoles", "Martes", "Viernes", np.nan, "Viernes"],
    "Ventas": [100, 150, np.nan, 150, 200, 130, 200],
    "Vendedor": ["Ana", "Juan", "Ana", "Juan", "Ana", "Maria", "Ana"],
    "Ciudad": ["Bogota", "Cucuta", np.nan, "Cucuta", "Bogota", "Bogota","Bogota", ]
}




















