import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

fechas=pd.date_range("20240101", periods=6)
# # print(fechas)

valores=np.random.randn(6,4)

# datos=pd.DataFrame(np.random.randn(6,4))
# print(datos)

columnas=list("ABCD")
print(columnas)

datos=pd.DataFrame(valores, index=fechas, columns=columnas)
print(datos)

datos["Ventas"]=datos["A"].cumsum() + 10
print(datos)

datos["Costos"]=datos["B"].cumsum() + 8
print(datos)

print("-"*50)

fig, ax=plt.subplots(figsize=(10,6))
# print(fig)
# print(ax)

ax.plot(datos.index, datos["Ventas"], label="Ventas", color="blue", marker="o" )
ax.bar(datos.index, datos["Costos"],label="Costos", color="red", alpha=0.5 )
ax.set_title("Ventas y Costo por Fecha")
ax.set_xlabel("Fecha")
ax.set_ylabel("Cantidad")
ax.grid(True)
ax.legend()


# plt.xticks(rotation=45)
plt.show()
# print()







