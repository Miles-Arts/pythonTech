import math
# Enunciado 
# Factorial: Realizar un programa que calcule 
# el factorial de un número que ingrese un usuario, 
# el número debe ser > 0 y < 20, de no ser así, 
# debe pedir el número tantas veces como sea necesario 
# hasta que cumpla la condición. Recuerda usar la librería math
# 

print("Ingrese los numero para calcular factorial")
print("Ingrese un número entre > 0 y < 20")

numero = int(input("Número: "))

if numero > 0 and numero < 20:
    resultado = math.factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
elif numero >= 21:
    print("Ingrese un número entre > 0 y < 20")


# math.factorial


# while True:
#     if numero > 0 and numero < 20:
#         for numero in range(1, numero, +1):
#             resultado =  numero * numero 
#             print(f"hola {resultado}")
#         break    
#     elif numero >= 21:
#         print("Ingrese un número entre > 0 y < 20")
#         break
              
#     continue
