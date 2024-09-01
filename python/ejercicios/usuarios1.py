import pandas as pd
import numpy as np
# # Enunciado

# # Manipulación básica con pandas: 
# # Crea un programa que utilice la biblioteca 
# # Pandas para realizar las siguientes tareas:

# # Crear un DataFrame llamado datos con las 
# # siguientes columnas: Nombre, Edad, Ciudad.

# # Mostrar por pantalla la información del DataFrame.
# # Filtrar las filas donde la edad sea mayor que 25.
# # Añadir una nueva columna llamada Categoría que 
# # clasifique a las personas en ""Joven"" 
# # si tienen 25 años o menos, y ""Adulto"" 
# # si tienen más de 25 años.
# # Mostrar por pantalla el DataFrame actualizado.
# print("-"*60)
# print("")
# personas={
#     "Nombre":   ["Juanita Castrillo", "Lucas Curtis", "Peter Motaño", "Ana España"],
#     "Edad":     [      18,                30,             50,            32       ],
#     "Ciudad":   [    "Cali",            "Tunja",         "Bogotá",      "Armenia" ]
# }

# df=pd.DataFrame(personas)
# print(df)
# print("-"*60)
# print("")


# # df["Categoria"]= df["Edad"]
# # print(df)
# # print("-"*60)
# # print("")

# df["Categoría"]= np.where(df["Edad"] < 25, "Joven", "Adulto" )
# print(df)
# print("-"*60)
# print("")


datos=pd.DataFrame({
    "Nombre":   ["Ana",    "Juan",   "María",       "Carlos"  ],
    "Edad":     [  22,       30,        25,            28     ],
    "Ciudad":   ["Madrid", "Bogotá", "Buenos Aires","New York"]
})

print("Informaicón del DataFrame:")
print(datos)

datos_filtrado = datos[datos["Edad"] > 25]














