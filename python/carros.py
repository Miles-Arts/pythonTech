print("-"*60)

carros = [
    {"marca": "Mercedes Benz", "modelo": "C300", "tipo": "Sedan" },
    {"marca": "BMW", "modelo": "328i", "tipo": "Cabriolet" },
    {"marca": "Audio", "modelo": "Q4", "tipo": "Sedan" },
    {"marca": "Porsche", "modelo": "Cayenne", "tipo": "Camioneta" }
]

def mostrar_vehiculo():
    print("---Mostrar Vehículos---")
    print("")
    print(carros)

def agregar_vehiculo():
    print("Agregar nuevo vehículo")
    marca = input("\nIngrese una marca de Vehículo: ")
    modelo = input("Ingrese un Modelo: ")
    tipo = input("Ingrese tipo: ")
    carro={"marca": marca, "modelo": modelo, "tipo": tipo}
    carros.append(carro)

def actualizar_vehiculo():
    print("editar")
    marca =input("\nIngrese la marca que desea actualizar: ")
    for carro in carros:
        if marca ==  carro["marca"]:
            nuevo_modelo = input("Ingrese nuevo modelo: ")
            nuevo_tipo = input("Ingrese nuevo tipo: ")
            carro["modelo"]=nuevo_modelo
            carro["tipo"]=nuevo_tipo
            print("Automovil actualizado")
            return
    print("Marca no encontrada")    

def eliminar_vehiculo():
    print("Eliminar") 
    marca=input("Ingrese la marca a eliminar: ")
    cantidad_anterior = len(carros)
    carros[:]=[carro for carro in carros if carro != carros["marca"]]
    if cantidad_anterior > len(carros):
        print("Marca de vehículo eliminado")
    else:
        print("Marca no encontrada")
    print(carros)


def menu_salir():
    print("----FIN----")    


def menu_vehiculos():
   while True:
        print("---Menú Gestión de Vehículos---")
        print("\n1. Ver.")
        print("2. Agregar Vehículo.")
        print("3. Editar Vehículo.")
        print("4. Eliminar Vehículo.")
        print("5. Salir.")
        print("")
        opcion = input("Seleciones una opción: ")
        print("\n")

        if opcion == "1":
            mostrar_vehiculo()
        elif opcion == "2":
            agregar_vehiculo()
        elif opcion == "3":
            actualizar_vehiculo()
        elif opcion == "4":
            eliminar_vehiculo()
        elif opcion == "5":
            menu_salir()
            break
        else:
            print("Opción no válida.")        


menu_vehiculos()
# mostrar_vehiculo()
# agregar_vehiculo()
# editar_vehiculo()
# eliminar_vehiculo()
