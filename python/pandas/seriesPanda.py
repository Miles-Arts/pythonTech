import csv
import pandas as pn

# nombres=input("Ingrese los nombres: ").split(",")
# print(nombres)
# print(",".join(nombres))

with open("archivoP.csv", "r", encoding="utf-8") as archivo:
    data=csv.reader(archivo)
    for fila in data:
        print(fila)






























print(".")