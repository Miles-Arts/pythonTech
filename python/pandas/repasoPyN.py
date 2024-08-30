import pandas as pd
import numpy as np

print("-"*60)

# Creación de DataFrame desde Listas
# (Lista de lista) usando Pandas
data=[["Alice", 25], ["Bob", 30], ["Charly", 35]]
df=pd.DataFrame(data, columns=["Nombre", "Edad"])
print(df)

carros=[["Mercdes Benz", 300], ["BMW", 320], ["Audi", 4]]
df1=pd.DataFrame(carros, columns=["Marca Carro", "Modelo"])
print(df1)

flores=[["Rosa", "Morada"], ["Margarita", "Azul"], ["Girasol", "Amarilla"]]
df3=pd.DataFrame(flores, columns=["Nombre Flores", "Color Flores"])
print(df3)

notas=[["Matemáticas", 5], ["Español", 4.5], ["Inglés", 5]]
df6=pd.DataFrame(notas, columns=["Materias", "Notas"] )
print(df6)

ciudades=[["Tunja", "Frío"], ["Armenia", "Templado"], ["Bogotá", "Frío"]]
df8=pd.DataFrame(ciudades, columns=["Ciudades", "Climas"])
print(df8)

# Creación de DataFrame desde
# Diccionarios usando Pandas
data={"Nombre": ["Alice", "Bob", "Charlie"], "Edad": [15, 30, 35]}
df=pd.DataFrame(data)
print(df)

libros={"Libros": ["Tiempos", "Verde", "Azul"], "Autores":["Lucas A", "Carla B", "Juan O y Ana Q"]}
df2=pd.DataFrame(libros)
print(df2)

juegos={"Nintendo": ["NT 64", "Game Boy", "Nest"], "Juego": ["Gold 007", "Tetris", "F1 Car"]}
df5=pd.DataFrame(juegos)
print(df5)

peliculas={"Peliculas": ["Alien", "Star Wars", "Terminator"], "Genero": ["Ciencia Ficción - Terror", "Ciencia Ficción - Futuro", "Ciencia Ficción - Acción"]}
df9=pd.DataFrame(peliculas)
print(df9)


