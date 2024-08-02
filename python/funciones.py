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

# # ------------------------------------

# def miFuncion(*args):
#     for valor in args:
#         print(valor)

# retorno = miFuncion("Código ", 2024, [0,1,2,3,4] )   

# # print(retorno)
# # ------------------------------

# def miFuncionN(**keywordargs):
#     for valor in keywordargs:
#         print(valor)

# miFuncionN(nombre = "Código ", año = 2024, numero = [0,1,2,3,4] )   

# print(retorno)

# def sumar(*args):
#     print(args)
#     respuesta = args[0] + args[1]

#     return respuesta

# resultado = sumar(2,4,6,8)

# print(resultado)

# ---------------------------
# Desempaquetado de tuplas
# def sumar(**args):
#     print(args)
#     # n1,n2,n3,n4 = args
#     # respuesta = args[0] + args[1]
#     # respuesta = n1 + n2
#     # return respuesta

# # resultado = sumar(2,4,6,8)
# resultado = sumar(n1 = 2, n2 = 4, n3 = 6, n4 = 8)

# print(resultado)

# def sumar(**args):
#     print(args)
#     res = args["n1"]+args["n2"]
#     return res

# resultado = sumar(n1 = 0, n2 = 4, n3 = 6, n4 = 8)

# print(resultado)

# #-------------------------
# print("----------------------------")

# def miFuncion3(*args, **keywordsargs):
#     total = 0
#     for valor in args:
#         total += valor
#     print("Sumatorial:", total)

#     for valor in keywordsargs:
#         print(valor, keywordsargs[valor])

# miFuncion3(10, -2, 1.5, celular ="315230000", edad = "18")         

# #-------------------------
# print("----------------------------")

# def restar(a,b):
#     return a - b, "Naranja", 3500

# respuesta = restar(30,10)
# # print(respuesta)
# print("---------------------------")

# def calcularIva():
#     iva = 12
#     costo = int(input("¿Cual es el monto a Calcular?: "))
#     calculo = (costo * iva)/ 100
#     print("El calculo de IVA es: " + str(calculo) + "\n")

# calcularIva()    

# print("---------------------------")

# # PROCESO
# def calcularIva(costo, iva):
#     # calculo = 0
#     # calculo = (costo * iva)/ 100
#     # return calculo
#     return (costo * iva)/ 100

# # ENTRADA
# costo = float(input("¿Cual es el monto a Calcular?: $ "))
# iva = 12

# # SALIDA
# resultado = calcularIva(costo, iva)    
# # print("El calculo de IVA es: $" + str(resultado) + "\n")
# # print("El calculo de IVA es: $" , (resultado) , "\n")
# print(f"El calculo de IVA es: ${resultado:.2f} \n")

print("---------------------------")


# def sumar(n1,n2):
#     return n1+n2

# suma = sumar(1,2)
# print(suma)

# exepciones


notas = ["a","b","c","d","a","b","c","d""a","b","c","d"]

while True:
    letra = input("Ingrese letra: ")
    indiceInicio = input("Ingrese Indice inicio: ")
    indiceFinal = input("Ingrese Indice final: ")
    noExiste=False


    try:
        indiceInicio = int(indiceInicio)
        indiceFinal = int(indiceFinal)
        try:
            posicion=notas.index(letra, indiceInicio, indiceFinal)
        except ValueError as mensajeError:
            noExiste = True
            # print(mensajeError)
            raise
        # else:
        #     print(posicion)
        # finally:
        #     print("No Existe")

    except ValueError as mensajeError:
        if noExiste:
            ("Elemento no encontrado")
        else:    
            print("Erro Se debe ingresar numeros")

        print(mensajeError)  
        2
    else:
        print(f"La letra esta en la posición {posicion}")
        res=None
        while res != "2":
            print("¿Desea ingresar otra letra? \n1. si\n2. no")
            res=input()
            if res == "1":
                break
            elif res == "2":
                continue
            else:
                print("Opción no válida")
        else:
            break    



# indiceInicio = input("Ingrese Indice inicio: ")  
# indiceInicio = int(indiceInicio)  

# print(indiceInicio)
print("---------------------------")


