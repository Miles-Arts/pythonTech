# Enunciado

# Cesta de compras: 
# Escribir un programa que cree un diccionario 
# simulando una cesta de la compra. El programa 
# debe preguntar el artículo y su precio y añadir 
# el par al diccionario, hasta que el usuario decida 
# terminar ingresando la palabra “FIN”. 

# Después se debe mostrar por pantalla la lista 
# de la compra y el coste total, de la siguiente manera

# Articulo 1 Valor
# Articulo 2 Valor
# Articulo 3 Valor
# TOTAL VALOR

# def compras():
#     articulos={}
#     continuar="fin"
#     while continuar=="fin":
#         print("\n---Lista Productos---\n")
#         producto=str(input("Ingrese Productos: "))
#         precio=float(input("Ingrese precio: "))
#         articulos[producto]=(precio)
#         continuar1=input("Para terminar escriba (FIN)").lower()
#         if continuar1 == "fin":
#             break 
#     return articulos

productos=[]
def compras():
    print("---Agregar Productos---")
    while True:
        nombre_producto=str(input("\nIngrese Producto: "))
        precio_producto=float(input("Ingrese precio: "))
        producto={"producto": nombre_producto, "precio": float(precio_producto)}
        productos.append(producto)
        print("\nPara continuar ( Enter )")
        terminar=input("Para terminar escriba -> ( FIN ): ").lower()
        if terminar == "fin":
            break
    return productos    
   

def imprimir(productos):
    print("\n ---Productos--- \n")
    valor_total=0
    for i, producto in enumerate(productos, start=1):
        
        print(f"Producto {i} {producto["producto"]} Precio: {producto["precio"]}" )
        valor_total += producto["precio"]
    print(f"Valor total compra: {valor_total}") 

lista_productos=compras()
imprimir(lista_productos)





















