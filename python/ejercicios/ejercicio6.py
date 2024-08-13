#   Enunciado Área: 
# Escriba un programa que 
# primero si se quiere calcular el área 
# de un triángulo (T o t) o la de un círculo (C o c). 
# Si contesta que quiere calcular el área de un triángulo 
# solicite base y altura, de lo contrario 
# solicite el radio e imprima el área correspondiente


print("¿Cuál Área desea calcular?")
# pregunta = str(input("Triángulo (T o t) o la de un Círculo (C o c): ").lower())
respuesta = str(input("Triángulo (T o t) o la de un Círculo (C o c): ").lower())

while True:
    if respuesta == "t":
        print("Ingrese las medidas para calcular área.")
        medida1 = float(input("Ingrese la base: "))
        medida2 = float(input("Ingrese la altura: "))
        # medida3 = int(input("Medida 3: "))
        area = (medida1 * medida2) / 2
        print(f"El área del Triángulo es: {area}")
        break

    elif respuesta == "c":
        print("Ingrese el radio del Círculo.")
        medida1 = float(input("Ingresea  radio: "))
        area = (medida1 ** 2) * 3.14
        print(f"El áreas del Círculo es: {area}")
        break
    elif respuesta != "t" and respuesta != "c":
        print("Ingrese un parámetro válido.")
        area = None
        break








