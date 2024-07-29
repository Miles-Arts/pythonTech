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



productoNombre = [input("Ingrese producto ")]
productoPrecio = int(input("Ingrese precio: "))
cantidadComprada = int(input("Cantidad de producto: "))

ivaCinco = 0.05
ivaDienciNueve = 0.19

precio = 0

# for precio in productoPrecio:
if productoPrecio < 4:
    print(f"Productos: {productoNombre}")
    print("Producto Excento de Iva ")
elif  productoPrecio < 18:
    print(f"Productos: {productoNombre}")
    print("Con 5% IVA") 
elif  productoPrecio > 19:
    print(f"Productos: {productoNombre}")
    print("Producto con 19% de IVA")
     
















print("Reto")











