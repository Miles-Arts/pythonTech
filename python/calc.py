#  + - * /
"""
(1)  Suma
(2)  Resta
(3)  Multiplicación
(4)  División
"""

# print("(1)  Suma")
# print("(2)  Resta")
# print("(3)  Multiplicación")
# print("(4)  División")

# op = input("Ingrese la operación: ")

# calculadora(op)

def calculadora(num1, num2, op):

    # op = input("Ingrese numero")
    # num1 = int(input("Ingrese valores: " )) 
    # num2 = int(input("Ingrese valores: " )) 

    if op == 1:
        print(f"Resultado de la Suma:  { num1 + num2}")
    
    elif op == 2:
        print(f"Resultado de la Resta:  { num1 - num2}")
     
    elif op == 3:
        print(f"Resultado de la Multiplicación:  { num1 * num2}")
    
    elif op == 4:
        print(f"Resultado de la División:  { num1 / num2}")
    
    else:
        print(f"Ingresa un número correcto")


# calculadora(45, 30, 3)  
   
(calculadora(45, 30, 3))

# valores ==

