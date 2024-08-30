import pandas  as pd
import numpy as np

datos_ventas={"Día":    ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], 
              "Ventas": [450,         300,      200,      400,         600  ]}

df_ventas =pd.DataFrame(datos_ventas)
df_ventas.to_csv("ventas_semanales3.csv", index=False)

df_ventas=pd.read_csv("ventas_semanales3.csv")
print("Datos de ventas leídos del CSV:\n", df_ventas)

total_ventas=df_ventas["Ventas"].sum()
promedio_ventas=df_ventas["Ventas"].mean()
print("\nTotal de Ventas en la Semana:", total_ventas)
print("Promedio de Ventas Diarias:", promedio_ventas)

ventas_altas=df_ventas[df_ventas["Ventas"] > 300]
print("\nDías con ventas Mayores a 300:\n", ventas_altas)

df_ventas.loc[df_ventas["Día"] == "Lunes", "Ventas"] = 500
print("\nVentas Actualizadas:\n", df_ventas)
# print(df_ventas)

nueva_fila=pd.DataFrame({"Día": ["Sábado"], "Ventas": [350]})
df_ventas=pd.concat([df_ventas, nueva_fila], ignore_index=True)
print("\nVentas con Sábado Añadido:\n", df_ventas)

df_ventas.loc[df_ventas["Día"] == "Martes", "Ventas"] =np.nan
print("\nVentas con Dato Faltante:\n", df_ventas)
df_ventas_sin_nulos=df_ventas.dropna()
print("\nVentas sin Días Faltantes:\n", df_ventas_sin_nulos)


