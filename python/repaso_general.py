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

# Ejemplo 1: Función para Calcular el Factorial

for cuadr in cuadrados:
    print(cuadr)




































print("-"*60)