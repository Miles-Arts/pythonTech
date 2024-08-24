import numpy as np


# lista=[1,2,3]
# print(lista)
# #array multidimensional
a=np.array([1,2,3])
print(a)

# escalarProducto=a*2
# print(escalarProducto)

# seno=np.sin(a)
# print(seno)

# logaritmo=np.log(a)
# print(logaritmo)

# b=np.array([[1,2,3]])
#Una 2x3 DOS filas 3 COLUMNAS- filas primeros, comulnas depues
b=np.array([[1,2,3],[4,5,6]])
print(b)

print("")

# 3 Filas 2 Columnas
# modifica la matriz
cambiar_array=b.reshape((3,2))
print(cambiar_array)

lista=["a","b","c","d","e"]
print(lista[:5])

primera_fila=b[1,:2]
print(primera_fila)




