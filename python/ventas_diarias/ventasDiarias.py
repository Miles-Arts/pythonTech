import csv 

datos_vetas=[["Día", "Ventas"],
             ["Lunes", 450],
             ["Martes", 300],
             ["Miércoles", 200],
             ["Jueves", 400],
             ["Viernes", 600]]

with open("ventas_semanales.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(datos_vetas)

# ventas=[]
# with open("ventas_semanales.csv")












