# entrada=str(input("Ingrese la frase: ")).lower()
# frase=entrada.split()
# frases={}

# for palabra in entrada:
#     if palabra in frases:
#         frases[palabra]+=1
#     else:
#         frases[palabra]=1

# print("Palabras Repetidas")

# for clave, valor in frases.items():
#     print(f"{clave} y {valor}")


# Escribir un programa que pregunte el nombre del 
# usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena 
# ¡Hola <nombre>!, donde 
# <nombre> es el nombre que el usuario haya introducido.

# ingrese_nombre=str(input("Hola, Ingresa tu nombre: "))

# print(f"¡Hola {ingrese_nombre}!")


# num1=3
# num2=2
# num3=2
# num4=5
# num5=2

# def operacion():
#     operacion_salida=  ((num1+num2) / (num3*num4)) ** num5
#     print(operacion_salida)


# operacion()




# ingrese_numero=int(input("Ingrese numero entero positivo: "))

# # for numero in range(0,ingrese_numero,1):
# #     numero= numero * (numero + 1) / 2
# #     # numero+=1
# #     print(numero)

# suma = ingrese_numero * (ingrese_numero + 1) / 2

# print(f"La suma de los números enteros desde 1 hasta + {ingrese_numero} es {suma}")


# MASA CORPORAL
# peso=float(input("Ingrese su peso kg: "))
# altura=float(input("Ingrese su altura Mt: "))

# imc= peso / (altura * altura)

# # print(f"Su altura de {altura}")
# # print(f"Su peso de {peso}")
# print(f"Tu índice de masa corporal es {imc:.2f}")

# COCIENTE
# entero0=int(input("Ingrese el primer numero entero: "))
# entero1=int(input("Ingrese el segundo numero entero: "))


# division= entero0 / entero1
# cociente= entero0 % entero1

# print(f"{entero0} entre {entero1} da un cociente {division:.2f} y un resto {cociente}")

# INVERSION DINERO

# dinero_inversion=float(input("Ingrese la cantidad a Invertir: "))
# interes_anual=float(input("Ingrese el interés anual (%): "))
# anios_invertir=int(input("Años a inventir: "))

# for anio in range(1, anios_invertir +1):
#     dinero_inversion *= 1 + (interes_anual / 100)
#     print(f"Año { anio}: Capital acumulado = {round(dinero_inversion, 2)}")

# dinero_invertir=float(input("Ingrese cantidad a invertir: "))
# anual_interes=float(input("Ingrese el interés anual (%): "))
# dinero_anios=int(input("Años a inventir: "))

# for anio in range(1,dinero_anios,1):
#     resultado = (dinero_invertir * (anual_interes / 100 + 1 ) ** dinero_anios)
# print(f"Año {dinero_anios}: Capital acumulado = {round(resultado, 2)}")
  
# PAYASOS Y MUÑECAS







