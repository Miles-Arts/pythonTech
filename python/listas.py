# producto = []

# lista = ["p1", "p2", "p3", 2, True, []]

# print(lista[0])
# print(lista[-4])

# # LIST---------------------------

# producto1 = "p1"
# producto2 = "p1"
# producto3 = "p1"

# # Siempre inician en posición 0 Cero
# lista = ["p2", 2, 3.5, True, []]


# Menor 1 -1  Para llamar al último valor
#  Listas tienen corchetes []

# Singular
# Nombre = "Juanita"
# Nombre1 = "Alonso"
# Nombre2 = "Pepe"

# #List en plural
# nombres = [Nombre, Nombre1, Nombre2, 'Paty']

# print(nombres)
# # print(nombres[0])
# # print(nombres[1])
# # print(nombres[-1])
# # print(nombres[-2])

# # res = Nombre2[2]
# print(nombres[:])
# print(nombres[1:])
# print(nombres[2:])
# print(nombres[:3])
# print(nombres[1:3])
# print(nombres[-1:])
# print(nombres[-2:])

# nombres[2] = 'Sara'
# print(nombres)

# nombre1 = 'Cata'
# print(nombres)

# nombres = ["Maria", "Rodolfo", [ 'Carlos', 'Diana']]
# edades = [ 26, 29]


# Matriz LIST con LIST
# lista = [nombres, edades]

# print(lista)
# print(lista[0])
# print(lista[0])
# print(lista[0][0])
# print(lista[0][2][1])

# # edades = edades + [ 18 ]
# # Aisgnar un nuevo VALOR
# edades += [ 18 ]

# lista = nombres + edades
# print(lista)

# Singular
# Nombre = "Juanita"
# Nombre1 = "Alonso"
# Nombre2 = "Pepe"

# #List en plural
# nombres = [Nombre, Nombre1, Nombre2, 'Paty']
# # print(nombres[4])
# print(nombres)

# nombresList = ["Rodolfo", "Maria"]

# nombre = input("Ingrese nombre: ")

# # Si nombre ESTA in nombresList
# if nombre in nombresList:
#     print("si")
# else:
#     print("No")    

# lista = list()


# factura = ["Pan", "Queso", "Huevos", 100, 1234]
# factura.remove("Huevos")
# print(factura)
# factura.pop(1)
# print(factura)
# factura.pop()
# print(factura)
# factura.clear()
# print(factura)
# del factura[0]
# print(factura)
# del factura
# print(factura)


notas = ["a", "c","e","a","d","b","c","a","c",]

print(notas)
print(len(notas))
print(min(notas))
print(max(notas))
notas.append("b")
print(notas)
notas.insert(2, "d")
print(notas)
print(notas.count("a"))
notas.extend(["b", "c", "d"])
print(notas)
print(notas.index("c", 4))
print(notas.pop(2))
print(notas)
notas.remove("a")
print(notas)
notas.reverse()
print(notas)
nuevaLista = notas.copy()
print(nuevaLista)
nuevaLista.sort()
print(nuevaLista)
nuevaLista.clear()
print(nuevaLista)







