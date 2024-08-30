import pandas as pd
import numpy as np

print("-"*60)

# Creación de DataFrame desde Listas
# (Lista de lista) usando Pandas
data=[["Alice", 25], ["Bob", 30], ["Charly", 35]]
df=pd.DataFrame(data, columns=["Nombre", "Edad"])
print(df)


# Creación de DataFrame desde
# Diccionarios usando Pandas
data={"Nombre": ["Alice", "Bob", "Charñie"], "Edad": [15, 30, 35]}
df=pd.DataFrame(data)
print(df)





