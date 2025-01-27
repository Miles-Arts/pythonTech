# print("Ingresa 3 numeros: ")
# numero1=float(input("primer número: "))
# numero2=float(input("segundo número: "))
# numero3=float(input("tercer número: "))

# suma=numero1+numero2+numero3
# promedio=suma / 3

# print("---Resultados---")
# print(f"La suma de los 3 números es: {suma:.2f}")
# print(f"El promedio de los tres numeros es: {promedio:.1f}")


# temperatura=float(input("Ingresa la termperatura en grados Celsius: "))

# fahrenheit=(temperatura*9/5) + 32
# kelvin=temperatura + float(273.15)

# print("---Conversor de temperaturas---")
# print(f"Temperatura en Celsius es: {temperatura} °C")
# print(f"Temperatura en Fahrenheit es: {fahrenheit} °F")
# print(f"Temperatura en Kelvin es: {kelvin:.2f} °K")

# medidas triangulo
# print("Ingresa las dimenciones del triángulo: ")
# base=float(input("Ancho: "))
# altura=float(input("Altura: "))
# print("\nIngresa las dimenciones de los bordes del triangulo: ")
# perimetro1=float(input("Medida base: "))
# perimetro2=float(input("Medida izquierda: "))
# perimetro3=float(input("Medida base: "))

# area=float(0.5) * base * altura
# area1=(base * altura) / 2

# perimetro_total=perimetro1+perimetro2+perimetro3
# perimetro_total1=2*(base+altura)

# print(f"El área del triángulo es: {area1:.2f}")
# print(f"El perímetro del triángulo es: {perimetro_total:.2f}")
# print(f"El perímetro del triángulo es: {perimetro_total1:.2f}")


# CONVEROS MINUTOS HORAS DIAS

# print("---Conversor  mMnutos a Horas y Días")
# minutos=float(input("Ingrese cantidad de minutos: "))

# horas=minutos / 60
# dias=minutos / 1440
# dias1=float(minutos / (60*24))


# print(f"Los {minutos} minutos.")
# print(f"Son {horas:.0f} horas. ")

# if dias1 >= 1.00 and dias1 <= 1.99:
#     print(f"Son {dias1:.0f} día.")
# elif dias1 >= 2.00:
#     print(f"Son {dias1:.0f} días.")
# else:
#     print(f"Son {dias:.2f} día. ")

print("---Sistema básico de Calificacion---")

estudiante=str(input("Ingrese nombre estudiante: ")).title()
print("Ingrese notas de cada asignatura")

nota1=float(input("Nota Inglés: "))
nota2=float(input("Nota Computación: "))
nota3=float(input("Nota Sociales: "))

promedio=(nota1+nota2+nota3) / 3

if promedio >= 3.0:
    print(f"El estudiante: {estudiante}")
    print(f"NOTAS:\n")
    print(f"Inglés: \t{nota1}")
    print(f"Computación: \t{nota2}")
    print(f"Sociales: \t{nota3}")
    print(f"\tPromedio: {promedio:.2f}")
    print(f"\t\tSemestre Aprobado.")
elif promedio <= 2.9:
    print(f"El estudiante: {estudiante}")
    print(f"NOTAS:\n")
    print(f"Inglés: \t{nota1}")
    print(f"Computación: \t{nota2}")
    print(f"Sociales: \t{nota3}")
    print(f"\tPromedio: {promedio:.2f}")
    print(f"\t\tSemestre Reprobado.")



















































































