print("-"*60)

carros = [
    {"marca": "Mercedes Benz", "modelo": "C300", "tipo": "Sedan" },
    {"marca": "BMW", "modelo": "328i", "tipo": "Cabriolet" },
    {"marca": "Audio", "modelo": "Q4", "tipo": "Sedan" },
    {"marca": "Porsche", "modelo": "Cayenne", "tipo": "Camioneta" }
]

def mostrar_vehiculo():
    print("Mostrar Vehículos")
    print(carros)

def agregar_vehiculo():
    print("Agregar nuevo vehículo")
    modelo = input("\nIngrese un Modelo: ")
    marca = input("Ingrese una marca de Vehículo: ")
    tipo = input("Ingrese tipo: ")
    carro={"marca": marca, "modelo": modelo, "tipo": tipo}
    carros.append(carro)

def editar_vehiculo():
    print("editar")

def eliminar_vehiculo():
    print("eliminar")        


def menu_vehiculos():
   while True:
        print("---Menú Gestión de Vehículos---")
        print("1. Ver .")
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
            editar_vehiculo()
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
