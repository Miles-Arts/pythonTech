# #Ejemplo de STOCK

# def cargar():
#     productos={}
#     continua="s"
#     while continua=="s":
#         codigo=int(input("Ingrese el codigo del producto: "))
#         descripcion=input("Ingrese la descripción: ")
#         precio=float(input("Ingrese el precio: "))
#         stock=int(input("Ingrese el stock actual: "))
#         productos[codigo]=(descripcion,precio,stock)
#         continua=input("Desea cargar otro producto[s/n]")
#     return productos

# def imprimir(productos):
#     print("Listado completo de productos: ")
#     for codigo in productos:
#         print(codigo, productos[codigo][0],productos[codigo][1],productos[codigo][2])

# def consulta(productos):
#     codigo=int(input("Ingrese el código de artículo a consultar: "))
#     if codigo  in productos:
#         print(productos[codigo][0],productos[codigo][1],productos[codigo][2])

# def listado_stock_cero(productos):
#     print("Listado de artículos con stock en cero: ")
#     for codigo in productos:
#         if productos[codigo][2]==0:
#             print(productos[codigo][0],productos[codigo][1],productos[codigo][2])

# productos=cargar()
# imprimir(productos)
# consulta(productos)
# listado_stock_cero(productos)       

print("-------------------------------------------")

def transporte():
    vehiculos={}
    continuar="s"
    while continuar=="s":
        placa_Vehiculo=int(input("Ingrese placa vehículo: "))
        print("Bus - Colectivo - Moto - Taxi - Taxi Turismo")
        tipo_Vehiculo=input("Ingrese tipo de vehículo: ")
        precio_pasaje=int(input("Ingrese precio pasaje: "))
        hora_salida=int(input("Ingrese hora de salida: "))
        vehiculos=[placa_Vehiculo]=(tipo_Vehiculo,precio_pasaje,hora_salida)
        continuar=int("Desea ingresar otro vehiculo [s/n] ")
    return vehiculos

def imprimir(vehiculos):
    print("Listado de vehículos: ")
    for placa_Vehiculo in vehiculos:
        print(placa_Vehiculo, vehiculos[transporte][0],vehiculos[transporte][1],vehiculos[transporte][2])
        
def consultar(vehiculos):
    placa_Vehiculo=input("Ingrese placa vehículo a consultar: ")
    for placa_Vehiculo in vehiculos:
        print(vehiculos[placa_Vehiculo][0],vehiculos[placa_Vehiculo][1],vehiculos[placa_Vehiculo][2])

def listado_vehiculos(vehiculos):
    print("Listado de vehículos: ")
    for placa_Vehiculo in vehiculos:
        if vehiculos[placa_Vehiculo][2]==0:
            print(vehiculos[placa_Vehiculo][0],vehiculos[placa_Vehiculo][1],vehiculos[placa_Vehiculo][2])

vehiculos=transporte()
imprimir(vehiculos)
consultar(vehiculos)
listado_vehiculos(vehiculos)    




