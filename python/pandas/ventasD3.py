import pandas  as pd
import numpy as np

datos_ventas={"Día":    ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], 
              "Ventas": [450,         300,      200,      400,         600  ]}

df_ventas =pd.DataFrame(datos_ventas)
df_ventas.to_csv("ventas_semanales3.csv", index=False)

df_ventas=pd.read_csv("ventas_semanales3.csv")
print("Datos de ventas leídos del CSV:\n", df_ventas)







# print(df_ventas)









