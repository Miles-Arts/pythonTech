import pandas as pd

datos1=[
    [1, "Ana"],
    [2, "Juan"],
    [3, "Maria"]
]

# print(datos)

df1=pd.DataFrame(datos1, index=["a", "b", "c"], columns=["ID", "Nombre"])
print(df1)

print("-"*60)

datos2={"ID":[1,2,3], "Nombre": ["Ana", "Juan", "Maria"]}
df2=pd.DataFrame(datos2)
print(df2)

nombres=pd.Series(["Ana", "Juan", "Maria"])
edades=pd.Series([10, 15, 20])
ciudades=pd.Series(["Bogota", "Cucuta", "Medellin"])

df4=pd.DataFrame({"Nombres": nombres, "Edades": edades, "Ciudades": ciudades})
print(df4)























