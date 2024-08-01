# #Ejemplo de STOCK

# def cargar():
    # productos={}
    # continua="s"
    # while continua=="s":
    #     codigo=int(input("Ingrese el codigo del producto: "))
    #     descripcion=input("Ingrese la descripción: ")
    #     precio=float(input("Ingrese el precio: "))
    #     stock=int(input("Ingrese el stock actual: "))
    #     productos[codigo]=(descripcion,precio,stock)
    #     continua=input("Desea cargar otro producto[s/n]")
    # return productos

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
        try:     
            codigo_Vehiculo=int(input("Ingrese código de vehículo: "))
            print(" ")
            print("Bus - Colectivo - Moto - Taxi - Taxi Turismo")
            tipo_Vehiculo=input("Ingrese tipo de vehículo: ")
            precio_pasaje=float(input("Ingrese precio pasaje: $"))
            hora_salida=int(input("Ingrese hora de salida [24h]: "))   
            vehiculos[codigo_Vehiculo]=(tipo_Vehiculo,precio_pasaje,hora_salida)
            continuar=input("Desea ingresar otro vehiculo [s/n] ")
        except ValueError:
            print("Ingrese datos correctos")
            print("-----------------------")
        else:
            continue;            
    return vehiculos

def imprimir(vehiculos):
    print("Listado de vehículos: ")
    for codigo_vehiculo in vehiculos:
        print(codigo_vehiculo, vehiculos[codigo_vehiculo][0],vehiculos[codigo_vehiculo][1],vehiculos[codigo_vehiculo][2])
        
def consultar(vehiculos):
    # try:
        codigo_vehiculo=int(input("Ingrese placa vehículo a consultar: "))
    # except ValueError:
    #     print("Ingrese datos correctos")
    #     print("-----------------------")      
        if codigo_vehiculo in vehiculos:
            print(vehiculos[codigo_vehiculo][0],vehiculos[codigo_vehiculo][1],vehiculos[codigo_vehiculo][2])

def listado_vehiculos(vehiculos):
    print("Listado de vehículos:")
    for codigo_vehiculo in vehiculos:
        if vehiculos[codigo_vehiculo][2]==0:
            print(codigo_vehiculo, vehiculos[codigo_vehiculo][0],vehiculos[codigo_vehiculo][1],vehiculos[codigo_vehiculo][2])

vehiculos=transporte()
imprimir(vehiculos)
consultar(vehiculos)
listado_vehiculos(vehiculos)    




