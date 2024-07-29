# N productos / N Suministros como
# Informació adicional IVA
# 
#       N cantidad productos a procesar
#       Para cada producto Ingresar
#       Código del producto.
#       Nombre al Producto
#       Cantidad comprada.
#       Valor unitario (Si IVA)
#       Tipo de Iva, que puede ser:
#                   1- Excento de IVA
#                   2- Bienes IVA 5%
#                   3- General IVA 19%    
# 
# 
# 
# 

print("---------TIENDA EL PROGRESO----------")
print(" ")

productoPrecios = []

codigoProducto = input("Ingrese código producto: ")
productoNombre = [input("Ingrese Nombres productos cada uno con Coma , : ")]
productoPrecios = (input("Ingrese precio en COP: "))

# productoPrecios = [float(precio.strip()) for precio in productoPrecios]

ivaCinco = 0.5
ivaDienciNueve = 0.19


ivaBienes = (productoPrecios + (productoPrecios * ivaCinco))
ivaGeneral = (productoPrecios + (productoPrecios * ivaDienciNueve))

print("-------------------")

# for precio in productoPrecio:
if productoPrecios <= 99999:
    print(f"Código Producto: {codigoProducto}")
    print(f"Productos: {productoNombre}")
    print(f"Producto Excento de IVA {productoPrecios}")

elif  productoPrecios <= 100000:

    print(f"Código Producto: {codigoProducto}")
    print(f"Productos: {productoNombre}")
    print(f"Precio sin IVA ${productoPrecios}" ) 
    print(f"Con 5% IVA ${ivaBienes}") 

elif  productoPrecios >= 1000000:
    
    print(f"Código Producto: {codigoProducto}")
    print(f"Productos: {productoNombre}")
    print(f"Precio sin IVA ${productoPrecios}")
    print(f"Producto con 19% de IVA ${ivaGeneral}")
    print(f"Cantidad de productos {len(productoNombre)}")

     


print(" ")
print("---------Gracias Por Su Compra----------")














print("Reto")











