print("-"*60)

carros = [
    {"marca": "Mercedes Benz", "modelo": "C300", "tipo": "Sedan" },
    {"marca": "BMW", "modelo": "328i", "tipo": "Cabriolet" },
    {"marca": "Audio", "modelo": "Q4", "tipo": "Sedan" },
    {"marca": "Porsche", "modelo": "Cayenne", "tipo": "Camioneta" }
]

def mostrar_vehiculo():
    print("Mostrar Vehículos")
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
    print("eliminar")        


def menu_vehiculos():
   while True:
        print("---Menú Gestión de Vehículos---")
        print("1. Ver.")
        print("2. Agregar Vehículo.")
        print("3. Editar Vehículo.")
        print("4. Eliminar Vehículo.")
        print("5. Salir.")
        print("")
        opcion = input("Seleciones una opción: ")
        print("")

        if opcion == "1":
            mostrar_vehiculo()
        elif opcion == "2":
            agregar_vehiculo()
        elif opcion == "3":
            actualizar_vehiculo()
        elif opcion == "4":
            eliminar_vehiculo()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")        


menu_vehiculos()
# mostrar_vehiculo()
# agregar_vehiculo()
# editar_vehiculo()
# eliminar_vehiculo()
