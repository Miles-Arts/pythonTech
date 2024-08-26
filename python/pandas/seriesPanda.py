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

# print(serie_a[0])
# print(serie_b["a"])
# print(serie_c["a"])

print(" ")
print(serie_a ** 2)


print(" ")
ventas=pd.Series([450, 300,200,400,600], index=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])
print(ventas)
print(ventas["Miercoles"])
print(ventas.iloc[2])

# print(ventas.sum())
# print(ventas.mean())
# print(ventas["Lunes"])
# print(ventas[ventas>300])
# print(ventas[ventas<400])

# ventas["Lunes"]=500
# print(ventas)

# ventas["Sabado"]=350
# print(ventas)

ventas2=pd.Series([500, 350,250,450,650], index=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])

print(ventas)
print(ventas2)
print(ventas+ventas2)














