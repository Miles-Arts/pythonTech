dinero_inversion=float(input("Ingrese la cantidad a Invertir: "))
interes_anual=float(input("Ingrese el interés anual: "))
anios_invertir=int(input("Años a inventir: "))

resultado_inversion = dinero_inversion * interes_anual
resultado_inversion = resultado_inversion * anios_invertir 

anio_ganancias= resultado_inversion / anios_invertir

print(f"Ganancia totales: {resultado_inversion}")
print(f"Ganancias por cada año: {anio_ganancias}")
