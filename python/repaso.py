import json
import os
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
# print("---------")

# diccionario={
#     "marca_vehículo": "Mercedes Benz",
#     "placa": "abc123",
#     "tipo": "Sedan"
# }
# # ensure_ascii=False -- mantener acentos como tíldes
# vehiculo=json.dumps(diccionario, ensure_ascii=False)
# vehiculo1=json.dumps(diccionario)
# print(vehiculo)
# print(vehiculo1)

# print("---------")

# print(json.dumps({"nombre": "Luicina", "edad": 23}))
# print(json.dumps(["Coco", "Durazno"]))
# print(json.dumps(("Coco", "Durazno")))
# print(json.dumps("Hola"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# print("------------------")


# Tipos de datos

# diccionario={
#     "nombre": "Carolina",
#     "edad": 19,
#     "soltera": False,
#     "independiente": True,
#     "padres": ("Samuel", "Eva"),    
#     "hijos": None,
#     "mascotas": [
#         {"tipo": "gato", "edad": 3},
#         {"tipo": "perro", "edad": 2}
#     ] 
# }


# datos1 = json.dumps(diccionario)
# datos2 = json.dumps(diccionario, ensure_ascii=False)
# datos3 = json.dumps(diccionario, indent=4, sort_keys=True, separators=(". ", " = "))

# print(datos1)
# print(datos2)
# print(datos3)


# Deserializar



pais="""
{
    "pais": "Alemania",
    "continente": "Europa",
    "moneda": "Euro"

}
"""

# diccionario= json.loads(pais)

# print(diccionario)
# print(diccionario["pais"])
# print(diccionario["continente"])
# print(diccionario["moneda"])


print("------------------")

# # Escritura y lectura

# contactos=[
#     ("Carla", "Analista de Java", "carla@java.com"),
#     ("José", "ux/ui", "jose@uxui.com"),
#     ("Mariana", "Programadora Python", "mar@python.com"),
#     ("Nicolás", "Front End", "nico@front.com"),
#     ("Marta", "Back End", "marta@back.com"),
#     ("Lorena", "Analista de datos", "lore@data.com"),
# ]

# datos = []

# for nombre, empleo, email in contactos:
#     datos.append({"nombre": nombre, "empleo": empleo, "email": email})

# with open("contactos.json", "w"  , encoding="utf-8") as archivoJson:
#     json.dump(datos, archivoJson )

# with open("contactos.json", "r" , encoding="utf-8") as archivoJson:
#     datos = json.load(archivoJson)
#     for contacto  in datos:
#         print(contacto["nombre"], contacto["empleo"], contacto["email"])

# print(datos)


# with open("contactoss.txt", "w", encoding="utf-8") as texto:
#     print(texto.write(pais))

# with open("contactoss.txt", "r", encoding="utf-8")  as texto:
#     print(texto.readline())    
#     print(texto.readline())    
#     print(texto.readline())    

# with open("contactoss.txt", "r", encoding="utf-8") as texto:
#     print(texto.readline())


# with open("contactoss.txt", "r", encoding="utf-8") as texto:
#     print(list(texto))


# with open("contactoss.txt", "r", encoding="utf-8") as texto:
#     for linea in texto:
#         print(linea)


# with open("contactoss.txt", "w", encoding="utf-8")  as nTexto:
#     print(nTexto.write("Alemania"))

# with open("contactoss.txt", "w", encoding="utf-8") as nTexto:
#     nTexto.writelines(["Alemania\n", "Fundamentos de Automovilismo\n", str(2024) + "\n"])   


# with open("contactoss.txt", "a" , encoding="utf-8") as nTexto:
#     nTexto.writelines("Autos de Lujo")

# with open("contactoss.txt", "r", encoding="utf-8") as texto:
#     caracteres=texto.read()
#     print(len(caracteres))
#     print(caracteres[:8])

# print( "---------------------------------")    

# with open("contactoss.txt", "r", encoding="utf-8") as texto:
#     cuenta = 0
#     for linea in texto:
#         cuenta+=1
#         if linea.startswith("F"):
#             print(linea)
#         print(cuenta)

# print( "---------------------------------")  
# with open("contactoss.txt", "r", encoding="utf-8") as texto:
#     for linea in texto:
#         linea=linea.rstrip()
#         if not linea.startswith("20"):
#             continue
#         print(linea)


# def leer_archivo(nombre_archivo):
#     try:
#         abrir_archivo = open("D:/SENA/USA/BOOTCAMP/python/"+nombre_archivo+".txt", "r", encoding="utf-8") 
#     except:
#         print("El Archivo " , nombre_archivo, "no se puede abrir")
#         quit()

#     return abrir_archivo.read()

# nombre_archivo=input("Ingrese el nombre del archivo: ")
# print("")
# print(leer_archivo(nombre_archivo))    


print("---------------------")

# mision = """

# [{
#     "pais": "Alemania",
#     "continente": "Europa",
#     "moneda": "Euro"

# }]
# """
# with open("mision.txt", "w", encoding="utf-8") as mision:
#     print(mision.write("Hola"))

abrir_archivo = open("mision.txt", "r+", encoding="utf-8")

abrir_archivo.write("Hola Tripulante")
abrir_archivo.writelines(["\nsoy una linea"])
abrir_archivo.seek(35)
abrir_archivo.write("Mision tic")
abrir_archivo.seek(10)
print(abrir_archivo.read(15))
abrir_archivo.seek(0)
abrir_archivo.writelines("Ciclo 1")
abrir_archivo.close

print("-"*10)

abrir_archivo=open("mision.txt", "r", encoding="utf-8")
print(abrir_archivo.read(5))

abrir_archivo=open("mision3.txt", "x", encoding="utf-8")

abrir_archivo=open("mision4.txt", "a+", encoding="utf-8")



os.remove("mision2.txt")
os.rmdir("lacarpeta")
















print(" ")
print("----------------------------")
