datosAves=[
    {
        "nombreComun": "Colibrí",
        "descripcion": {
            "tamaño": "9 cm",
            "color": "Verde y Rojo",
            "caracteristicas": "Pequeño",
            "comportamiento": "Se alimenta de néctar"
        },
        "multimedia":{
            "fotos": ["ruta/foto1.jpg", "ruta/foto2.jpg"],
            "sonidos": ["ruta/sonido1.mp3"]
        },
        "observaciones": [
            {"fecha": "2024-05-01", "lugar": "Boyacá", "avistamientos": 5},
            {"fecha": "2024-04-01", "lugar": "Cundinamarca", "avistamientos": 10}
        ]
    }
]


def mostrarAves():
    print("Mostrar aves")
    print(datosAves)


def agregarAve():
    print("Agregar ave")
    aveNueva= {}

    nombreComun= input("Ingrese el nombre común: ")
    aveNueva["nombreComun"]= nombreComun

    descripcion= {}
    descripcion["tamaño"]= input("Ingrese el tamaño: ")
    descripcion["color"]= input("Ingrese el color: ")
    descripcion["caracteristicas"]= input("Ingrese las caracteristicas: ")
    descripcion["comportamiento"]= input("Ingrese los comportamiento: ")
    aveNueva["descripcion"]= descripcion

    multimedia= {}
    multimedia["fotos"]= input("Ingrese las rutas de las fotos (ruta/foto1.jpg,ruta/foto2.jpg): ").split(",")
    multimedia["sonidos"]= input("Ingrese las rutas de los sonidos (ruta/sonido1.mp3,ruta/sonido2.mp3): ").split(",")
    aveNueva["multimedia"]= multimedia

    observaciones= []
    while True:
        res= input("¿Desea agregar una observación?: \n1. Si \n2. No ")
        if res == "2":
            break

        observacion= {}
        observacion["fecha"]= input("Ingrese la fecha de la observación (YYYY-MM-DD): ")
        observacion["lugar"]= input("Ingrese el lugar de la observación: ")
        observacion["avistamientos"]= input("Ingrese el numero de avistamientos: ")

        observaciones.append(observacion)

    aveNueva["observaciones"]= observaciones
    datosAves.append(aveNueva)
    print("Ave agregada")
    

def actualizarAve():
    print("Actualizar ave")
    nombreComun= input("Ingrese la nombre comun del ave que desea actualizar: ")
    aveEncontrada= False

    for ave in datosAves:
        if nombreComun == ave["nombreComun"]:
            aveEncontrada= True
            print("Seleccione la opción que desea actualizar: ")
            print("1. Descripción")
            print("2. Multimedia")
            print("3. Observaciones")

            opcion= input()

            if opcion == "1":
                descripcion= {}
                descripcion["tamaño"]= input("Ingrese el nuevo tamaño: ")
                descripcion["color"]= input("Ingrese el nuevo color: ")
                descripcion["caracteristicas"]= input("Ingrese las nuevas caracteristicas: ")
                descripcion["comportamiento"]= input("Ingrese los nuevos comportamiento: ")
                ave["descripcion"]= descripcion

            elif opcion == "2":
                multimedia= {}
                multimedia["fotos"]= input("Ingrese las rutas de las nuevas fotos (ruta/foto1.jpg,ruta/foto2.jpg): ").split(",")
                multimedia["sonidos"]= input("Ingrese las rutas de los nuevos sonidos (ruta/sonido1.mp3,ruta/sonido2.mp3): ").split(",")
                ave["multimedia"]= multimedia

            elif opcion == "3":
                observaciones= []
                while True:
                    res= input("¿Desea agregar una observación?: \n1. Si \n2. No ")
                    if res == "2":
                        break

                    observacion= {}
                    observacion["fecha"]= input("Ingrese la nueva fecha de la observación (YYYY-MM-DD): ")
                    observacion["lugar"]= input("Ingrese el nuevo lugar de la observación: ")
                    observacion["avistamientos"]= input("Ingrese el nuevo numero de avistamientos: ")

                    observaciones.append(observacion)

                ave["observaciones"]= observaciones

            print("Ave actualizada")
            
    
    if not aveEncontrada:
        print("Nombre comun no encontrado.")
           

    
def eliminarAve():
    print("Eliminar ave")
    nombreComun= input("Ingrese la nombre comun del ave que desea eliminar: ")
    longitudAnterior= len(datosAves)
   
    datosAves[:]= [ave for ave in datosAves if nombreComun != ave["nombreComun"]]

    if longitudAnterior > len(datosAves):
        print("Ave eliminada")
    else:
        print("Nombre comun no encontrado")


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