# Enunciado Múltiplo: Escriba un programa que pida 
# dos números enteros e imprima si el mayor es múltiplo del menor

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 > num2:
    resultado = num1 % num2
    if  resultado == 0:
        print(f"El número mayor { num1 } es multiplo de {num2} y resultado {resultado}")
         
elif num1 < num2:
    resultado = num2 % num1
    if resultado == 0:
        print(f"El número mayor { num2 } es multiplo de {num1} y resultado {resultado}")

# if num1 > num2 and num1 % num2 == 0:
#     print(f"{num1} es múltiplo de {num2}.")
# elif num2 > num1 and num2 % num1 == 0:
#     print(f"{num2} es múltiplo de {num1}.")
# else:
#     print("El mayor no es múltiplo del menor.")
        
