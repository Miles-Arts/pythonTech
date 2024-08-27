import pandas as pd

# Ventas diarias
# El problema consiste en gestionar y analizar una serie de datos de ventas semanales utilizando la
# biblioteca pandas de Python. Se debe manipular una serie de datos de ventas diarias para una
# tienda, realizando varias operaciones como cálculos básicos, filtrado de datos, actualización y
# manejo de valores faltantes. A continuación, se presenta el problema estructurado en pasos:
# Paso 1: Crear una Serie de Ventas
# • Crea una serie de pandas llamada ventas con los datos de ventas d

ventas = pd.Series([450,300,200,400,600], index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])

# Paso 2: Guardar la Serie en un Archivo CSV
# • Asigna un nombre al índice de la serie para indicar que representa los días de la semana.
# • Convierte la serie a un DataFrame para poder guardarla en un archivo CSV, ya que pandas
# no permite guardar directamente series en este formato.
# • Guarda la serie en un archivo llamado ventas_semanales.csv


ventas.index.name = "Día"
ventas.to_frame("Ventas").to_csv("ventas_semanales1.csv", header=True)









