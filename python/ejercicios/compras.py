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

def compras():
    articulos={}
    continuar="fin"
    while continuar=="fin":
        print("\n---Pruductos---\n")
        producto=str(input("Ingrese Productos"))
        precio=float(input("Ingrese precio: "))
        articulos[producto]=(precio)
        continuar=input("Para terminar escriba (FIN)").lower()
    return articulos

def imprimir(articulos):
    print("\n ---Productos--- \n")
    print(f"Articulo  1: {articulos["producto"]}. Valor : ${articulos["precio"]}")
    print(f"Articulo  2: {articulos["producto"]}. Valor : ${articulos["precio"]}")
    print(f"Articulo  3: {articulos["producto"]}. Valor : ${articulos["precio"]}")


lista_productos=compras()
imprimir(lista_productos)





















