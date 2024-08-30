print("-"*60)


def saludar():
    print("Hola, gente")
saludar()


def saludar1(nombre):
    print(f"Hola, {nombre}")
saludar1("Alice")

def suma(a, b):
    return a + b

resultado=suma(3,5)
print(resultado)

# def suma2():
#     return 

resultado=suma(a=10, b=7)
print(resultado)


def cuadrado(numero):
    return numero ** 2
resultado=cuadrado(4)
print(resultado)


def ejemplo_ambito():
    variable_local=10
    print(variable_local)


variable_global=20
ejemplo_ambito()
print(variable_global)

cuadrado=lambda x: x **2
resultado=cuadrado(5)
print(resultado)


numeros=[1,2,3,4,5]
cuadrados=list(map(lambda x: x ** 2, numeros))
print(cuadrados)

for cuadr in cuadrados:
    print(cuadr)

# Ejemplo 1: Función para Calcular el Factorial

def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)
    
resultado_factorial = calcular_factorial(7)
print(f"El factorial de 5 es: {resultado_factorial}")    

print("-"*60)
# Ejemplo 2: Función Lambda para Filtrar Números Pares
numero=[1,2,3,4,5,6,7,8,9,10]
es_par=lambda x: x % 2 == 0
numeros_pares=list(filter(es_par, numero)) 
print("Lista Original:", numeros)
print("Números Pares:",  numeros_pares)

# 2 FOR

num=[1,2,3,9]
num1=[4,5,6]

for nume, nume1 in zip(num, num1):
    print(nume, nume1)

mi_diccionario={
    "nombre": "Carmen",
    "edad": 25,
    "ciudad": "New York"
}

print("Nombre:", mi_diccionario["nombre"])
print("Edad:", mi_diccionario["edad"])

mi_diccionario["edad"] = 19

mi_diccionario["profesion"] = "Programadora"

# for mi_dicc in mi_diccionario:
#     print(mi_diccionario)

del mi_diccionario["ciudad"]
# for mi_dicc in mi_diccionario:
print(mi_diccionario)

print("Diccionario actualizado:", mi_diccionario)


print("-"*60)

# ‘get’: Retorna el valor asociado a una clave, o un
# valor predeterminado si la clave no está presente.
valor=mi_diccionario.get("edad",0)


# ‘keys’: Retorna una lista con todas las claves del
# diccionario.
todas_las_keys=mi_diccionario.keys()

# ‘items’: Retorna una lista de tuplas, cada una
# conteniendo un par clave-valor.
todos_los_items=mi_diccionario.items()


# ‘pop’: Elimina un elemento dado su clave y
# retorna su valor.
valor_eliminado=mi_diccionario.pop("profesion")

# values’: Retorna una lista con todos los valores del
# diccionario.
todas_las_claves=mi_diccionario.values()

# ‘update’ : Actualiza el diccionario con otro
# diccionario o con pares clave-valor

mi_diccionario={}
otro_diccionario={"ciudad":"Los Angeles", "hobbies": ["lectura", "viajes"]}
mi_diccionario.update(otro_diccionario)

print(valor)
print(todas_las_keys)
print(todos_los_items)
print(valor_eliminado)
print(todas_las_claves)
print(mi_diccionario)

# Ejemplo 3: Información del estudiante
estudiante={
    "nombre": "Ana",
    "edad": 20,
    "materia_favoritas": ["Matemáticas", "Historia", "Programación"]
}

print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Materias Favoritas", estudiante["materia_favoritas"])

# Ejemplo 4: Registro de productos
productos={
    "productos1": {"nombre": "Laptop", "precio": 300, "stock": 10}, 
    "productos2": {"nombre": "Mouse", "precio": 20, "stock": 50},
    "productos3": {"nombre": "Teclado", "precio": 20, "stock": 30}
}

print("Producto 1:", productos["productos1"])
print("Precio del producto 2:", productos["productos2"]["precio"])














print("-"*60)