# Enunciado Múltiplo: Escriba un programa que pida 
# dos números enteros e imprima si el mayor es múltiplo del menor

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

if numero1 > numero2:
    resultado = numero1 % numero2
    if  resultado == 0:
        print(f"El número mayor { numero1 } es multiplo de {numero2} y resultado {resultado}")
         
elif numero1 < numero2:
    resultado = numero2 % numero1
    if resultado == 0:
        print(f"El número mayor { numero2 } es multiplo de {numero1} y resultado {resultado}")
        
