# Enunciado
# Base de datos de clientes: 
# Escribir un programa que permita gestionar 
# la base de datos de clientes de una empresa. 

# Los clientes se guardarán en un diccionario 
# en el que la clave de cada cliente será su NIT, 
# y el valor será otro diccionario con los datos 
# del cliente 
# (nombre, dirección, teléfono, correo, preferencial), 
# dónde preferencial 
# tendrá el valor True si se trata de un 
# cliente preferencial. 
# El programa debe preguntar al usuario por una opción del siguiente menú: 
# (1) Añadir cliente, (2) Eliminar cliente, 
# (3) Mostrar cliente, (4) Listar todos los clientes, 
# (5) Listar clientes preferenciales, (6) Terminar. 
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
# 1. Preguntar los datos del cliente, 
# crear un diccionario con los datos y 
# añadirlo a la base de datos.
# 2. Preguntar por el NIT del cliente y 
# eliminar sus datos de la base de datos.
# 3. Preguntar por el NIT del cliente y mostrar sus datos.
# 4. Mostrar lista de todos los clientes 
# de la base datos con su NIT y nombre.
# 5. Mostrar la lista de clientes preferenciales 
# de la base de datos con su NIT y nombre.
# 6. Terminar el programa.


base_datos_clientes=[ 
    {
        "nit" :12345, 
        "cliente": {
        "nombre": "Juan", 
        "direccion" : "123", 
        "telefono": 54321,
        "correo" : "juan@gmail.com",
        "preferencial": True
        }}
]

def anadir_cliente():
    base_datos={}
    print("Agregar Cliente: ")
    nit=int(input("Ingrese NIT: "))
    nombre=input("Ingrese nombre: ")
    direccion=input("Ingrese dirección Cliente: ")
    telefono=input("Ingrese teléfono:")
    correo=input("Ingrese correo: ")
    preferencial=bool(input("Preferencial marque 1: "))
    base_datos["nit": nit]={
        "nombre": nombre, 
        "direccion": direccion, 
        "telefono": telefono, 
        "correo": correo,
        "preferencial": preferencial
        }
    base_datos_clientes.append(base_datos)
    

def eliminar_cliente():
    print("Eliminar Cliente")
    eliminar_cliente=(input("Ingrese Nit del cliente a eliminar: "))
    clientes_antes=len(base_datos_clientes)
    base_datos_clientes[:]=[cliente for cliente in base_datos_clientes if eliminar_cliente != cliente["nit"]]
    if clientes_antes > len(base_datos_clientes):
        print("Cliente Eliminado")
    else:
        print("Escriba un parámetro válido")    

def mostrar_cliente():
    print(base_datos_clientes)
    # print("hola")

def lista_clientes():
    pass

def preferencial_lista_clientes():
    pass

def terminar():
   print("---FIN---")
   pass


def menu_clientes():    
    while True:
            print("\n---Menú---\n")
            print("1. Añadir Clientes")
            print("2. Eliminar Cliente")
            print("3. Mostrar Cliente")
            print("4. Listar todos los clientes")
            print("5. Listar clientes preferenciales")
            print("6. Terminar Programa")
            opcion=int(input("Ingrese el número de la opción: "))
            # print("\n-------\n")

            if opcion == 1:
                anadir_cliente()
            elif opcion == 2:
                eliminar_cliente()
            elif opcion == 3:
                mostrar_cliente()        
            elif opcion == 4:
                lista_clientes()
            elif opcion == 5:
                preferencial_lista_clientes()
            elif opcion == 6:
                terminar()
                break
            else:
                print("\nIngrese un parámetro válido\n")
            

             

menu_clientes()



















