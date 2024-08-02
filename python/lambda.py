# # LAMBDAS

# print("---------------------")
# # print("")

# def doblar(numero):
#     resultado=numero*2
#     return resultado

# def doblar(numero):
#     return numero*2

# def doblar(numero): return numero*2

# lambda numero: numero*2

# doblar_numero=lambda numero: numero*2

# print(doblar_numero(5))


# print("---------------------")

# impar=lambda numero: numero%2 != 0
# print(impar(5)) 

# revertir=lambda cadena: cadena[::-1]

# print(revertir("hola"))

# sumar = lambda x,y: x+y

# print(sumar(5,2))


# print("---------------------")

# print("Calculadora")
# print("Ingrese números a sumar")

# numero1=int(input("Ingrese un numero: "))
# numero2=int(input("Ingrese un numero: "))

# sumar=lambda numero1,numero2: numero1 + numero2

# print(f"Resultado: {sumar(numero1,numero2)}")
# print(f"---Fin---")

# print("---------------------")
# print("---------------------")


# print("-----CALCULAR ÁREA RECTÁNGULO------")

# area_rectangulo=lambda base,altura: base*altura

# print(f"El área del rectágulo es: {area_rectangulo(15,10)}")

# print("-----------")
# print("----CALCULAR ÁREA DEL CIRCULO-------")

# radio=int(input("Ingrese el radio delcículo: "))
# area_circulo=lambda radio: (radio ** 2) * 3.141592 

# print(f"El área es: {area_circulo(radio)}")
# print(f"---Fin---")

print(f"--------------")
print(f"------RELACIÓN-------")

mayor1=int(input("Ingrese un numero: "))
mayor2=int(input("Ingrese un numero: "))

# numeros=lambda numero: " 1" if numero == 1 

# if mayor1 == mayor2:
#     print("0")
# elif mayor1 > mayor2:
#     print("1")
# elif mayor1 < mayor2:
#     print("-1")
# else:
#     print("Ingrese un parámetro correcto")

comparar=lambda mayor1, mayor2: 0 if mayor1 == mayor2 else (1 if mayor1 > mayor2 else -1)        

print(comparar(mayor1,mayor2))

print("---Fin---") 


