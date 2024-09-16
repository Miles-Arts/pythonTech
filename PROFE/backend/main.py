datosAves=[
    {"especie": "Águila", "departamento": "Boyacá", "avistamientos": 5},
    {"especie": "Colibrí", "departamento": "Cundinamarca", "avistamientos": 10},
    {"especie": "Tucán", "departamento": "Cundinamarca", "avistamientos": 8}
]


def mostrarAves():
    print("Mostrar aves")
    print(datosAves)


def agregarAve():
    print("Agregar ave")
    especie= input("Ingrese la especie: ")
    departamento= input("Ingrese el departamento: ")
    avistamientos= int(input("Ingrese los avistamientos: "))
    ave={"especie": especie, "departamento": departamento, "avistamientos": avistamientos}
    datosAves.append(ave)


def actualizarAve():
    print("Actualizar ave")
    especie= input("Ingrese la especie del ave que desea actualizar: ")
    for ave in datosAves:
        if especie == ave["especie"]:
            departamentoNuevo= input("Ingrese el departamento nuevo: ")
            avistamientosNuevos= int(input("Ingrese los avistamientos nuevos: "))
            ave["departamento"]= departamentoNuevo
            ave["avistamientos"]= avistamientosNuevos
            print("Ave actualizada")
            return

    print("Especie no encontrada")


def eliminarAve():
    print("Eliminar ave")
    especie= input("Ingrese la especie del ave que desea eliminar: ")
    longitudAnterior= len(datosAves)
   
    datosAves[:]= [ave for ave in datosAves if especie != ave["especie"]]

    if longitudAnterior > len(datosAves):
        print("Ave eliminada")
    else:
        print("Especie no encontrada")


def menu():
    while True:
        print("\nMenú de Gestión de Aves")
        print("1. Ver todas las aves")
        print("2. Agregar nueva ave")
        print("3. Actualizar datos de una ave")
        print("4. Eliminar una ave")
        print("5. Salir")

        opcion= input("Seleccione una opción: ")

        if opcion == "1":
            mostrarAves()
        elif opcion == "2":
            agregarAve()
        elif opcion == "3":
            actualizarAve()
        elif opcion == "4":
            eliminarAve()
        elif opcion == "5":
            print("Salir")
            break
        else:
            print("Opción no valida")

menu()

# listaSinEliminado= []
# for ave in datosAves:
#     if especie != ave["especie"]:
#         listaSinEliminado.append(ave)