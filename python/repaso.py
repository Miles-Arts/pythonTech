print("----------------------------")

nombre_dia="Viernes"
nombre_producto="Libro"
precio=200
iva=0.19
estado=True

# print("El producto: " + nombre_producto + " tiene le precio de $" + str(precio))
# print("El producto:", nombre_producto , "tiene le precio de $" ,precio)
print(f"El producto: {nombre_producto} tiene le precio de ${precio } ")

precio_producto = precio + (precio * iva)
precio_producto =  (precio * iva)


print("----------------------------")
print(f"Total a pagar es: '\'{precio_producto }'\'")

# print(f"El total IVA: {precio_producto}")
# print(f"El total IVA: {precio + precio_producto}")


if precio > 200 and precio < 300:
    print("Entre 200 y 300")
elif precio > 200 and precio > 300:
    print("Es mayor de 200 y 300")
elif precio < 200 or precio == 200:
    print("Es menor o igual")    
else: 
    if precio <= 100:
        print("Menor o igual a 100")
    else:
        print("Es mayor")    





























































print("----------------------------")
