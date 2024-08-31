import pandas as pd
import numpy as np
import sqlalchemy 

print("-"*60)

# # Creación de DataFrame desde Listas
# # (Lista de lista) usando Pandas
# data=[
#     ["Alice", 25], 
#     ["Bob", 30], 
#     ["Charly", 35]
#     ]
# df=pd.DataFrame(data, columns=["Nombre", "Edad"])
# print(df)

# carros=[
#     ["Mercdes Benz", 300], 
#     ["BMW", 320], 
#     ["Audi", 4]
#     ]
# df1=pd.DataFrame(carros, columns=["Marca Carro", "Modelo"])
# print(df1)

# flores=[
#     ["Rosa", "Morada"], 
#     ["Margarita", "Azul"], 
#     ["Girasol", "Amarilla"]
#     ]
# df3=pd.DataFrame(flores, columns=["Nombre Flores", "Color Flores"])
# print(df3)

# notas=[
#     ["Matemáticas", 5], 
#     ["Español", 4.5], 
#     ["Inglés", 5]
#     ]
# df6=pd.DataFrame(notas, columns=["Materias", "Notas"] )
# print(df6)

# ciudades=[
#     ["Tunja", "Frío"], 
#     ["Armenia", "Templado"], 
#     ["Bogotá", "Frío"]
#     ]
# df8=pd.DataFrame(ciudades, columns=["Ciudades", "Climas"])
# print(df8)

# celulares=[["iPhone", "Azul"], ["Motorola", "Blanco"], ["LG", "Negro"]]
# df10=pd.DataFrame(celulares, columns=["Marca Celular", "Color"])
# print(df10)

# computador=[["Asus", "32 GB"], ["HP", "8 GB"], ["Sony", "16 GB"]]
# df11=pd.DataFrame(computador, columns=["Computador", "Ram"])
# print(df11)

# navegador=[["Opera", "12.0"], ["Chrome", "20"], ["Edge", "8.0.1"]]
# df12=pd.DataFrame(navegador, columns=["Navegador", "Actualización"])
# print(df12)

# # Creación de DataFrame desde
# # Diccionarios usando Pandas
# data={
#     "Nombre": ["Alice", "Bob", "Charlie"], 
#     "Edad": [15, 30, 35]
#     }
# df=pd.DataFrame(data)
# print(df)

# libros={
#     "Libros": ["Tiempos", "Verde", "Azul"], 
#     "Autores":["Lucas A", "Carla B", "Juan O y Ana Q"]
#     }
# df2=pd.DataFrame(libros)
# print(df2)

# juegos={
#     "Nintendo": ["NT 64", "Game Boy", "Nest"], 
#     "Juego": ["Gold 007", "Tetris", "F1 Car"]
#     }
# df5=pd.DataFrame(juegos)
# print(df5)

# peliculas={
#     "Peliculas": ["Alien", "Star Wars", "Terminator"], 
#     "Genero": ["Ciencia Ficción - Terror", "Ciencia Ficción - Futuro", "Ciencia Ficción - Acción"]
#     }
# df9=pd.DataFrame(peliculas)
# print(df9)


# sistema_operativo={"Sistema_Operativo": ["Windows", "Abunto", "Debian"], "Versión": ["11", "Dark VI", "Blue 13"]}
# df13=pd.DataFrame(sistema_operativo)
# print(df13)

# Creación de Arrays
# Creación de array unidimensional
arr=np.array([1,2,3,4,5])
print(arr)
# arr=np.array(["Casa", "Perro", 123])
# print(arr)

# Creación de array bidimensional
arr_2s=np.array([[1, 2, 3], [4,5,6], [7, 8, 9]])
print(arr_2s)
# arr_2s=np.array([["nombre", "edad", "Salon"], ["Juan", 23, "Quinto"], ["Alberto", 22, "Cuarto"]])
# print(arr_2s)

# Manipulación de Arrays en NumPy
print(arr[0])
#           Fila | Columna
print(arr_2s[ 1,      2]) #Elemento especifico ARRAY

print(arr[1:4]) #Rebanar arry unidimensioanl
print(arr_2s[ :2, 1: ]) #Rebanar arry bidimensioanl

arr2=np.array([6, 7, 8, 9, 10])
print(arr)
print(arr + arr2)
print(arr * 2)

#CSV
df_csv=pd.read_csv("archivo20.csv")
print(df_csv)

df_csv=pd.read_csv(
    "archivo20.csv",
    sep=";",
    header=0,
    index_col="ID"
)

#  EXCEL
df_excel=pd.read_excel("archivo.xlsx", sheet_name="nombre_hoja")
print(df_excel)

df_excel=pd.read_excel(
    "archivo.xlsx",
    sheet_name="nombre_hoja",
    header=0,
    index_col="ID"
)
print(df_excel)


#JSON
df_json=pd.read_json("archivo.json")
print(df_json)

df_json=pd.read_json(
    "archivo.json",
    orient="records"
)
print(df_json)




















