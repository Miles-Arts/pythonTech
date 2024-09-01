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
    # total = sum(productos["precio"])
    for producto in productos:
        print(f"Producto {producto["producto"]} Precio: {producto["precio"]}" )
        
    # print("Articulo  1:,", productos["precio"])
    # print(f"Articulo  1: {productos["producto"][0]}")
    # # print(f"Articulo  1: {articulos[:]}. Valor : ${articulos}")
    # # print(f"Articulo  2: {articulos["producto"]}. Valor : ${articulos["precio"]}")
    # # print(f"Articulo  3: {articulos["producto"]}. Valor : ${articulos["precio"]}")


lista_productos=compras()
imprimir(lista_productos)





















