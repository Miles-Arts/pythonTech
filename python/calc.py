#  + - * /
"""
(1)  Suma
(2)  Resta
(3)  Multiplicación
(4)  División
"""

print("---Elija una operación---")
print("(1)  Suma")
print("(2)  Resta")
print("(3)  Multiplicación")
print("(4)  División")


op = input("Ingrese la operación: ")
num1 = input("Ingrese valores: " )
num2 = input("Ingrese valores: " )

op = int(op)
num1 = int(num1)
num2 = int(num2)

uno = "suma" 

def calculadora(num1, num2, op):
   
    if op == 1:
        print(f"El resultado de la suma es: {num1 + num2}")
        
        return num1 + num2 
    elif op == 2:
        print()
        return num1 - num2
    elif op == 3:
        print()
        return num1 * num2
    elif op == 4:
        print()
        return num1 / num2
    else:
        print(f"Ingresa un número correcto")

resultado = calculadora(num1, num2, op)  
print(f"El resultado de la {resultado}")



