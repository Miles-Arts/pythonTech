datosAves=[
    {"especie": "Águila", "departamento": "Boyacá", "avistamiento": 5},
    {"especie": "Colibrí", "departamento": "Cundinamarca", "avistamiento": 10},
    {"especie": "Tucán", "departamento": "Boyacá", "avistamiento": 8}
]

def mostrarAves():
    print("Mostrar Aves.")
    print(datosAves)

def agregarAve():
    print("Agregar Ave.")

    especie = input("Ingrese la especie: ")
    departamento = input("Ingrese el departamento: ")
    avistamiento = input("Ingrese los avistamiento: ")
    ave={"especie": especie, "departamento": departamento, "avistamiento": avistamiento}
    datosAves.append(ave)


def actualizarAve():
    print("Actualizar Ave.")

def eliminarAve():
    print("Eliminar Ave.")     

def menu():
    while True:
        print("\n---Menú gestión de Aves---")
        print("\n1. Ver todas las aves")
        print("2. Agregar nueva ave")
        print("3. Actualizar datos de una ave")
        print("4. Eliminar un ave")
        print("5. Salir")
        print("")
        opcion = input("Selecione una opción: ")
        print("")


        if opcion == "1":
            mostrarAves()
        elif opcion == "2":
            agregarAve()
        elif opcion == "3":
            actualizarAve()
        elif opcion == "4":
            eliminarAve()
        elif opcion == "5":
            print("Salir.")
            break    
        else: 
            print("Opción no válida")

        print("")

menu()
mostrarAves()    
# agregarAve()
# actualizarAve()
# eliminarAve()



