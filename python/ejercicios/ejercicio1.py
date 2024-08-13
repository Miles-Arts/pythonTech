# Enunciado
# Ventas: 
# Realizar un programa que solicite las ventas 
# de 3 productos e imprima: El producto más costoso,
# el producto más económico y la media de los productos

# if producto1 >= producto2 or producto2 >= producto3 or producto1 >= producto3:
#     print(f"El Produto mayor es: {producto1}")
# elif producto1 <= producto2 or producto2 <= producto3 or producto1 <= producto3:
#     print(f"El Produto intermedio es: {producto1}")
# elif  producto1 <= producto2 or producto2 <= producto3 or producto1 <= producto3:
#     print(f"El Produto menor es: {producto1}")   

# precio = lista

lista = []

producto1 = float(input("Ingrese primer producto: "))
producto2 = float(input("Ingrese segundo producto: "))
producto3 = float(input("Ingrese tercero producto: "))


lista.append((producto1))
lista.append((producto2))
lista.append((producto3))

producto_mas_barato = min(lista)
media_productos = sum(lista) / 3
producto_mas_caro = max(lista)

print(f"El producto más barato es: {producto_mas_barato}")
print(f"El producto más caro es: {producto_mas_caro}")
print(f"Media de las ventas es: {media_productos:.2f}")


# producto1 = float(input("Ingrese primer producto: "))
# producto2 = float(input("Ingrese segundo producto: "))
# producto3 = float(input("Ingrese tercero producto: "))

# if producto1 > producto2 or producto2 > producto3 or producto1 > producto3:
#     print(f"El Produto mayor es: {producto1}")
# elif producto1 < producto2 or producto2 > producto3 or producto1 < producto3:
#     print(f"El Produto intermedio es: {producto2}")
# elif  producto1 < producto2 or producto2 < producto3 or producto1 < producto3:
#     print(f"El Produto menor es: {producto3}")   




























