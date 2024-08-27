import csv 


# Ventas diarias
# El problema presentado consiste en manipular y analizar datos de ventas semanales utilizando
# Python, particularmente con el módulo csv. La secuencia de pasos descrita abarca desde la creación
# y almacenamiento de datos de ventas en un archivo CSV, hasta la actualización y el filtrado de estos
# datos, incluyendo el manejo de datos faltantes. A continuación, se detallan los pasos para resolver
# el problema:



print("\n----Ventas diarias----\n")

# Paso 1: Crear Datos de Ventas y Guardar en CSV
# • Define una lista de listas datos_ventas que contenga los datos de ventas diarias, incluyendo
# los encabezados.
# • Usa with open para crear y abrir un archivo ventas_semanales.csv en modo escritura.
# • Utiliza csv.writer para crear un objeto escritor.
# • Emplea el método writerows() del objeto escritor para escribir la lista datos_ventas en el
# archivo CSV.

datos_ventas=[["Día", "Ventas"],
             ["Lunes", 450],
             ["Martes", 300],
             ["Miércoles", 200],
             ["Jueves", 400],
             ["Viernes", 600]]

with open("ventas_semanales.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(datos_ventas)


# Paso 2: Leer Datos de Ventas desde el CSV
# • Inicializa una lista vacía ventas para almacenar los datos leídos.
# • Abre el archivo ventas_semanales.csv en modo lectura.
# • Crea un objeto lector con csv.reader.
# • Usa next(lector) para saltar la cabecera del archivo.
# • Itera sobre el objeto lector, convierte las ventas a enteros y añade los datos a la lista ventas
# en forma de diccionarios.

ventas=[]
with open("ventas_semanales.csv", "r", encoding="utf-8") as archivo:
    lector=csv.reader(archivo)
    next(lector)
    for fila in lector:
        ventas.append({"Día": fila[0], "Ventas": int(fila[1])})


# Paso 3: Cálculo del Total y Promedio de Ventas
# • Calcula el total_ventas sumando las ventas de cada día.
# • Halla el promedio_ventas dividiendo el total de ventas entre el número de días.
# • Imprime el total y el promedio de ventas.

total_ventas = sum(venta["Ventas"] for venta in ventas)
promedio_ventas = total_ventas / len(ventas)
print("Total de Ventas en la Semana: ", total_ventas)
print("Promedio de Ventas Diarias: ", promedio_ventas)

# Paso 4: Filtrar Días con Ventas Mayores a 300
# • Utiliza comprensión de lista para filtrar los días cuyas ventas superan los 300.
# • Imprime los días con ventas mayores a 300.

ventas_altas = [venta for venta in ventas if venta["Ventas"] > 300]
print(f"VENTAS {ventas_altas}")
print("\nDías con Ventas Mayores a 300: ")
for venta in ventas_altas:
    print(venta)

# Paso 5: Actualizar Ventas para un Día Específico y Añadir un Nuevo Día
# • Itera sobre la lista ventas para encontrar y actualizar las ventas de un día específico.
# • Añade un nuevo día de ventas al final de la lista ventas.

for venta in ventas:
    if venta["Día"] == "Lunes":
        venta["Ventas"] = 500      
ventas.append({"Día": "Sábado", "Ventas": 350})        
# print(ventas)

# Paso 6: Mostrar Ventas Actualizadas
# • Imprime todas las ventas actualizadas para verificar los cambios.

print("\nVentas Actualizadas: ")
for venta in ventas:
    print(venta)


# Paso 7: Tratar con Datos Faltantes
# • Supongamos que algunos datos están faltantes o son desconocidos.
# • Itera sobre ventas y usa None para marcar las ventas desconocidas.
# • Filtra los datos para excluir aquellos marcados como None.

for venta in ventas:
    if venta["Día"] == "Martes":
        venta["Ventas"] = None
# print(f"NONE {venta} ")

ventas_sin_nulos = [venta for venta in ventas  if venta["Ventas"] is not None]        
print("\nVentas sin días Faltantes:")
for venta in ventas_sin_nulos:
    print(venta)






