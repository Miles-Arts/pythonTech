# Contraseña: Cree un programa que solicite una contraseña 
# por teclado e indique si es correcta o no, 
# si es incorrecta, la solicite nuevamente. 
# La contraseña correcta es: "Ilovepython123"


contraseña = str(input("Ingrese una contraseña: "))

# clave = "Ilovepython123"

# if contraseña == clave:
#     print("Contraseña correcta")
# else: 
#     print("Ingrese contraseña incorrecta: ")


contraseña_correcta = "Ilovepython123"

while True:
    contraseña_ingresada = input("Ingrese la contraseña")
    if contraseña_ingresada == contraseña_correcta:
        print("Contraseña correcta. ¡Bienvenido!")
    else:
        print("Contraseña incorrecta. \n Intentalo de nuevo.")    