import json
print("----------------------------")
print(" ")

# nombre_dia="Viernes"
# nombre_producto="Libro"
# precio=200
# iva=0.19
# estado=True

# print("El producto: " + nombre_producto + " tiene le precio de $" + str(precio))
# print("El producto:", nombre_producto , "tiene le precio de $" ,precio)
# print(f"El producto: {nombre_producto} tiene le precio de ${precio } ")

# # ARITMETICOS   
# precio_producto = precio + (precio * iva)
# precio_producto =  (precio * iva)


# print("----------------------------")
# print(f"Total a pagar es: '\'{precio_producto }'\'")

# print(f"El total IVA: {precio_producto}")
# print(f"El total IVA: {precio + precio_producto}")

# CONDICIONALES
# if precio > 200 and precio < 300:
#     print("Entre 200 y 300")
# elif precio > 200 and precio > 300:
#     print("Es mayor de 200 y 300")
# elif precio < 200 or precio == 200:
#     print("Es menor o igual a 200")    
# else: 
#     if precio <= 100:
#         print("Menor o igual a 100")
#     else:
#         print("Es mayor a 100")    

# () ? true: false

# if precio > 200:
#     print("si")
# else:
#     print("no")    

# print("si") if precio > 200 else print("no")   

# CICLOS

# c = 0 
# contador = c

# while contador < 3:
#     contador+=1
#     print(contador)
   
# while contador < 3:
#     print(contador)
#     contador+=1

# while True:
#     contador+=1
#     print("Hola")   
#     if contador == 3:
#         break

# desde = 0
# hasta = 10
# paso = 2

# for i in range(desde, hasta , paso):
#     print(f"Hola {i }")
    
# for i in range(0,6,1):
#     print(f"- {i }")


# for i in range(5):
#     if i==2:
#         continue
#     print(f"{i }")

# listas = []
# tuplas = ()
# diccionario = {}

# listas = [1, 2.5, True, "Rodolfo", ["a", "b", (7,2)], (1,  2, ["c", "d"]), {"clave1 ": 15, "clave2 ": 16}]

# print(listas)

# valor = listas[3]

# listas[2]= False

# valor2 = listas[4][1]
# valor3= listas[4][2][0]
# # valor4= listas[6]["clave1"]

# print(valor)
# print(valor2)
# print(valor3)
# # print(valor4)

# print(listas)


# listas[5][2][0]= "p"
# print(listas)

# print(" ")
# print("----------------------------")

# listas[6]["clave1"] = 8
# print(listas)


# nombre = input("Hola")
# precio = int(input("precio"))
# total = float(input("precio"))

# lista = [1,2,3,4]

# i = lista[2]
# print(i)

# for i in lista:
#     print(i)


# irregulares =[
#     [15, 2, 8, 5 , 3],
#     [3, 3, 7],
#     [9, 1, 16, 13],
#     [],
#     [5]
# ]

# for column in irregulares:
#     for item in column:
#         print(item, end=" ")
#     print()    

# matriz=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,["a",True,0.9]],
#     ]
# print("---------")

# for fila in range(len(matriz)):
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna], end=" ")
#     print()

# print("---------")

# sublista=matriz[2][2]
# for valor in sublista:
#     print(valor)   

# print("---------")     

# for fila in matriz:
#     for columna in fila:
#         print(columna, end="")
#     print()    

# print("---------") 

# [print([columna for columna in fila]) for fila in matriz ]


# print("---------") 

# [print([columna[fila] for columna in matriz]) for fila in range(len(matriz)) ]


# print(" ---------") 


# # lista multidimensional
# matriz.append([9,10,11])
# print(matriz)
# matriz[0].extend([12,13,14])
# print(matriz)
# matriz[1].reverse()
# matriz[2].reverse()
# print(matriz)


# nombres=[
#     [],
#     [],
#     []
# ]
# nombres.append(["Juanita", "soy", "Hola"])
# nombres.append([" De Bogotá"])
# print(nombres)
# nombres[2].extend([" hola gente"])
# print(nombres)
# nombres.reverse()
# print(nombres)
print("---------")

diccionario={
    "marca_vehículoa": "Mercedes Benz",
    "placa": "abc123",
    "tipo": "Sedan"
}
vehiculo=json.dumps(diccionario)
print(vehiculo)




















print(" ")
print("----------------------------")