# def pegarDuro():
#     print("golpe")
#     print("")

# pegarDuro()    

# numero1 = input("Ingrse un numero: ")
# numero2 = input("Ingrse un numero: ")

# numero1 = int(numero1)
# numero2 = int(numero2)

# # Parámetros argumentos
# def sumar(numero1, numero2):
#     suma = numero1 + numero2
#     print(suma)

    

# Argumentos
# resultado = sumar(numero1, numero2)


# def saludo(nombre):

#     print("hola ", nombre)
# saludo("Luciana")    


# def resta(a,b):
#     return a - b
# resultado = resta(30,10)
# print(resultado)


# def resta(a,b):
#     return a * b
# resultado1 = resta(a = 30, b = 40)
# print(resultado1)



# def resta(a = None, b = None):
#     if a == None or b == None:
#         return "Error, se debe enviar numeros"
#     return  a - b

# respuesta4 = resta()
# print(respuesta4)

# def restando(a, b):
#     return a - b

# respuesta2 = restando(a = 3, b = 40)
# print(respuesta2)

# # -------------------------------

# def sumar(numero1, numero2):
#     suma = numero1 + numero2
#     return suma

# numero1 = 2
# numero2 = 4

# respuesta = sumar(numero1,numero2)

# print(respuesta)

# ------------------------------------

def miFuncion(*args):
    for valor in args:
        print(valor)

retorno = miFuncion("Código ", 2024, [0,1,2,3,4] )   

# print(retorno)
# ------------------------------

def miFuncionN(**keywordargs):
    for valor in keywordargs:
        print(valor)

miFuncionN(nombre = "Código ", año = 2024, numero = [0,1,2,3,4] )   

# print(retorno)

def sumar(*args):
    print(args)
    respuesta = args[0] + args[1]

    return respuesta

resultado = sumar(2,4,6,8)

print(resultado)

# ---------------------------
# Desempaquetado de tuplas
def sumar(**args):
    print(args)
    # n1,n2,n3,n4 = args
    # respuesta = args[0] + args[1]
    # respuesta = n1 + n2
    # return respuesta

# resultado = sumar(2,4,6,8)
resultado = sumar(n1 = 2, n2 = 4, n3 = 6, n4 = 8)

print(resultado)