import csv
import pandas as pd

# nombres=input("Ingrese los nombres: ").split(",")
# print(nombres)
# print(",".join(nombres))

# with open("archivoP.csv", "r", encoding="utf-8") as archivo:
#     data=csv.reader(archivo)
#     print(data)
#     for fila in data:
#         print(fila)
#         # print(fila[0],fila[1],fila[2])
#         print(" - ".join(fila))


# with open("archivoP.csv", "w", encoding="utf-8") as archivo:
#     escribir=csv.writer(archivo)
#     escribir.writerow([ "Rodolfo","Lucas", "34465899" ])


# data=pd.read_csv("archivoP.csv")
# print(data)


serie_a=pd.Series([1, 2, 3, 4, 5])
print(serie_a)

print(" ")
serie_b=pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print(serie_b)

print(" ")
serie_c=pd.Series({"a": 100, "b": 200, "c" : 300, "d": 400, "e" :500  })
print(serie_c)

















print(".")