# # CLICOS BUCLES 
# print("hola")

# # Repetir una acción varias veces

# # FOR Bucle

# # FOR cantidad de veces = FOR
# # i contador
# c = 0

# #  range donde arranca 0, hasta donde va 5, y el paso 1
# for i in range(0,3,1):
#      c = c + 1
#     # c += 1

# print(c)    


# print("---------------")
# print("")
# # For con String o List
# # String también tiene su posición,

# for i in "Mision TIC 2024":
#     print(i)
#     # print(i(2))

# print("---------------")
# print("")

# for i in range(5):
#     print(i)

# print("---------------")
# print("")

# for x in range(2,30,3):
#     print(x)

# print("---------------")
# print("")

# for x in range(2, 6):
#     print(x)        

# print("---------------")
# print("")


# # el FOR hace el recorrido de la LIST edades
# edades = [10, 12, 11, 10, 9]
# c = 0

# for i in edades:
#     c += i

# promedio = c / 5

# print(c)
# print(promedio)

# print("---------------")
# print("")

# for multi in [1,2,3,4,5,6,7,8,9,19]:
#     numero = 2
#     print(f"{numero} * {multi} = {numero * multi}")



# print("---------------")
# print("")

# letras = ["A", "B", "C"]

# for i in letras:
#     print(i, end = " ")

# print("---------------")
# print("")

# for i in range(len(letras)):
#     print("Posición: ", i , end = "")
#     print(" con valor: ", letras[i])

# # PDF 110 VER VER
#  i es un contador

# for valor in [1,2,3]:
#     print(valor)

# print("-----------")

# for valor in ("a",2,True):
#     print(valor)
# print("-----------")

# for claves in {"clave1": "a", "clave2":"2", "clave3":True}.values():
#     print(claves)
# print("-----------")

# # "DEsacople de Tuplas"
# x, y = ("a", "b")


# for claves, valor in {"clave1": "a", "clave2":"2", "clave3":True}.items():
#     print(claves, valor)

# print("-----------")

# for claves in {"clave1": "a", "clave2":"2", "clave3":True}.keys():
#     print(claves)

# print("-----------")

# for letras in "Mercedes Benz":
#     print(letras)

# print("-----------")

# nombre = "Mercedes Benz"

# for letras in nombre:
#     print(letras[0])

# print(len(nombre))    

# for letras in nombre:
#     print(letras)

# for letras in range(len(nombre)):
#     print(letras)

# Palabra para variables y letra para contadores
#  i  contador
#  variables NOMBRE = "Juanita"

# Tuplas y List sólo tiene valores

# Items trae ambos - Claves y valores


# generar_coordenadas_aleatorias = 10

# for _ in range(10):

#     x_coord, y_coord = generar_coordenadas_aleatorias()

#     print(f"Coordenadas aleatorias: ({x_coord:.2f}, {y_coord:.2f})")



# RANGE

# nombre = "Canada"


# longitud = len(nombre)
# # print(len(nombre))

# for i in range(5):
#     print(i)

# print("------------")

# for i in range(1,5):
#     print(i)

# print("------------")

# for i in range(1,5,2):
#     print(i)

# print("------------")

# for i in range(10):
#     print(i)

# print("------------")

# # for i in range(1,10,8):
# #     print(i)


# nombre = "Canada"


# longitud = len(nombre)
# # print(len(nombre))

# for i in range(longitud):
#     print(nombre[i])

# print("------------")

# for letra in "Canada":
#     print(letra)

# # print("------------")

# c = 0

# for _ in range(3):
#     print(c)
#     c += 1

# print(c)


# print("------------")

# lista = [5,10,15,20,25]

# c = 0

# for numero in lista:

#     c += numero

# promedio = c / len(lista)

# print("------------")
# print(promedio)
# print("------------")
# print(c)
# print("------------")
# print(numero)

#  end="" le quita el salto de línea de print
# for numero in lista:
#     print(numero, end=" ")

# #lista[i]= "x"  X es asignado a x
# for i in range(len(lista)):
#     lista[i]= "x"
#     # lista[i]= input("Ingrese un valor: ")

# print(lista)    

# for i in range(len(lista)):
#    if lista[i] == 15:
#         del lista[i]
#         break
#         # continue


# print(lista)

# print(lista) 

# BREAK romper
# CONTINUE pasar al otro ciclo


# lista = ["Mariana"]

# for i in range(2):
#     nombre = input("Ingrese un nombre: ")
#     lista.append(nombre)
# print(lista)    


# letras = ["A", "B", "C"]

# print(letras)
# #REcorrer atras hacia delante
# for i in range(len(letras) -1, -1, -1):
#     if letras[i] == "B":
#         del letras[i]
#     print(letras)    




# letras = ["A", "B", "C"]

# for i in range(len(letras) -1, -1, -1):
#     print("Posición: ", i, end="")
#     print(" con valor: ", letras[i])



# letras = [] 
# for i in range(5):
#     letras.append(i)
# print(letras)    

# letras = [9, 8]

# for i in range(5):
#     letras.append(i)
# print(letras)

# letras = [9, 8]

# for i in range(0,5,1):
#     letras.append(i)
# print(letras)

# frutas = ["manzanas", "banana", "melon"]

# [print(valor) for valor in frutas]

# print("----------------")

# frutas = ["manzanas", "banana", "melon"]

# lista=[valor for valor in frutas if "l" in valor]

# print(lista)

# frutas = ["manzanas", "banana", "melon"]

# lista = []

# for valor in frutas:
#     if "l" in valor:
#         lista.append(valor)
# print(lista) 

# lista = [valor for valor in frutas if "l" in valor]

# print(valor)


# registro = ["Alberto", "Carmen"]
# nuevoRegistro=[]

# [nuevoRegistro.append(valor.lower()) for valor in registro]


# letras= ["a", "b", "c"]

# lista= []

# for letra in letras:
#     lista.append(letra)

# lista= [ letra for letra in letras ]    

# print(lista)

# nombres = ["pepe", "maria", "juan"]


# for nombre in nombres:
#     print(nombre)


# [print(nombre) for nombre in nombres]





# listaNumeros = [1,2,3,4,5,6,7,8,9,10]

# listaNumeroPar = []

# for numero in listaNumeros:

#     if numero % 2 == 0:

#         listaNumeroPar.append(numero)

# print(listaNumeroPar)



# frutas = ["banana", "pera", "coco"]

# lista = []

# for fruta in frutas:
#     if "banana" in frutas:
#         lista.append(fruta)

# print(lista)        


# lista = [ fruta for fruta in frutas   if "banana" in frutas]

# print(lista) 


# nombres = ["Alberto", "Carmen"]

# registros=[]

# for nombre in nombres:
#     registros.append(nombre.lower())

# registros = [nombre.lower() for nombre in nombres ]    

# print(registros)

# # [registro.append(valor.lower()) for valor in registro]

# usuario = input("Ingrese nombre: ")

# if usuario.lower() not in registros:
#     print("No Encontrado")
# else:
#     print("Encontrado: ")    



# nombres = ["pepe", "maria", "juan"]

# for nombre in nombres:
    
#     if nombre == "juan":
#         break



# nombres = ["pepe", "maria", "juan"]

# for nombre in nombres:
    
#     if nombre == "maria":
#        continue

#     print(nombre)

# else:
#     print("Final")    


# if 1<2:
#     pass
# elif 2 >1:
#     print("2 es mayor que 1")
# else:
#     print("Es igual")    


# diccionario = {"clave1": 1, "clave2": 2, "clave3": 3}

# valor = diccionario["clave1"]

# for clave in diccionario:
#     print(clave)

# print("-----------------")

# for clave in diccionario.keys():
#     print(clave)

# print("-----------------")

# for clave in diccionario.values():
#     print(clave)

# print("-----------------")

# for tupla in diccionario.items():
#     print(tupla)

# print("-----------------")



# for clave in diccionario:
#     print(diccionario[clave])

# print("-----------------")

# for clave, valor in diccionario.items():
#     print(clave, valor)



# lista = []

# diccionario1 = {"nombre": "pepe", "edad": 12, "genero": "hombre"}
# diccionario2 = {"nombre": "maria", "edad": 25, "genero": "mujer"}
# diccionario3 = {"nombre": "carlos", "edad": 30, "genero": "otro"}

# lista.append(diccionario1)
# lista.append(diccionario2)
# lista.append(diccionario3)

# print(lista)
# print(lista[0])
# print(lista[1])
# print(lista[2])

# for diccionario in lista:
#     print(diccionario["nombre"], diccionario["edad"], diccionario["genero"])
    # print(diccionario["edad"])
    # print(diccionario["genero"])

# for dicc in lista:
#     print("ciclo interno: ")
#     for clave, valor in dicc.items():
#         print(clave, valor)


# for letra in ["a", "b", "c"]:
#     print(letra)

# for i in range(0,15,3):
#     print(i)    



# i = 1

# while i < 6:
#     print(i)
#     i+=1

# condicion = 3

# i = 0

# while i < 5:
#     print("Hola")
#     i += 1
#     # break

# lista = ["a", "b", "c"]    

# c = 0

# while c < len(lista):
#     print(lista[c])
#     c+=1

# while True:
#     print("Hola")
#     break

# i = 1
# while i < 6:
#     print(i)
#     i+=1


# CON WHILE VERDADERO o FALSO
# CON WHILE TRUE o FALSE

# resultado = 0
# x = 5

# while x > 0:
#     resultado+=x
#     x-=1
#     print("...", x, end="... ")
#     # break
# print(resultado)    


# x = 1

# while x <= 5:
#     print(x, end=" ")

# i = 1

# while i < 6:
#     print(i)
#     if(i == 3):
#         break
#     i += 1


# i = 1

# while i < 6:
#     print(i)
#     if i == 4:
#         break
#     i += 1


# i = 1

# while i < 6:
#     print(i)
#     i +=1
# else:
#     print("i no es menor que 6")    


i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i no es menor que 6")    



frutas = ["manzana", "banana", "melon"]    

valor = 0

while valor < len (frutas):
    print(frutas[valor])
    valor+=1


