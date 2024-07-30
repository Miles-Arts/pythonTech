#  + - * /
"""
(1)  Suma
(2)  Resta
(3)  Multiplicación
(4)  División
"""

print("(1)  Suma")
print("(2)  Resta")
print("(3)  Multiplicación")
print("(4)  División")

# 

# calculadora(op)

op = input("Ingrese la operación: ")
num1 = input("Ingrese valores: " )
num2 = input("Ingrese valores: " )

op = int(op)
num1 = float(num1)
num2 = float(num2)



def calculadora(num1, num2, op):
    
    if op == 1:
        print("Suma")
        return num1 + num2
    elif op == 2:
        print()
        return num1 + num2
    elif op == 3:
        print()
        return num1 + num2
    elif op == 4:
        print()
        return num1 + num2
    else:
        print(f"Ingresa un número correcto")


# calculadora(45, 30, 3)  
resultado = calculadora(num1, num2, op)  

print(f"El resultado de la {resultado}")

# valores ==

