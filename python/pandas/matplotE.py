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

















