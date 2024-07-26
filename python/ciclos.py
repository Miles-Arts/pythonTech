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

for valor in [1,2,3]:
    print(valor)

print("-----------")

for valor in ("a",2,True):
    print(valor)
print("-----------")

for claves in {"clave1": "a", "clave2":"2", "clave3":True}.values():
    print(claves)
print("-----------")

# "DEsacople de Tuplas"
x, y = ("a", "b")


for claves, valor in {"clave1": "a", "clave2":"2", "clave3":True}.items():
    print(claves, valor)

print("-----------")

for claves in {"clave1": "a", "clave2":"2", "clave3":True}.keys():
    print(claves)

print("-----------")

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

# for i in range(1,10,8):
#     print(i)


nombre = "Canada"


longitud = len(nombre)
# print(len(nombre))

for i in range(longitud):
    print(nombre[i])

print("------------")

for letra in "Canada":
    print(letra)








