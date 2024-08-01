#Ejemplo de STOCK

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto: "))
        descripcion=input("Ingrese la descripción: ")
        precio=float(input("Ingrese el precio: "))
        stock=int(input("Ingrese el stock actual: "))
        productos[codigo]=(descripcion,precio,stock)