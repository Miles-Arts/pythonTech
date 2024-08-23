datosAves=[
    {
        "nombreComun": "Colibrí", 
        "descripcion": {
            "tamaño": "9 cm",
            "color": "Verde y Rojo",
            "caracteristicas": "Pequeño",
            "comportamiento": "Se alimenta de neétar"
        },
        "multimedia": {
            "fotos": ["ruta/foto1.jpg","ruta/foto2.jpg" ],
            "sonidos": ["ruta/sonidos1.mp3"]
        },
        "observaciones": [
            {"fecha": "2024-05-01", "lugar": "Boyacá", "avistamientos": 5},
            {"fecha": "2024-04-01", "lugar": "Cundinamarca", "avistamientos": 10}
        ] 
    }
]

def mostrarAves():
    print("Mostrar Aves.")
    print(datosAves)


def agregarAve():
    print("Agregar Ave.")
    aveNueva={}

    nombre=input("Ingrese el nombre común: ")

    aveNueva["nombreComun"]=nombre
    




def actualizarAve():
    pass

def eliminarAve():
    pass

def menu():
    while True:
        print("\n---Menú gestión de Aves---")
        print("\n1. Ver todas las aves.")
        print("2. Agregar nueva ave.")
        print("3. Actualizar datos de una ave.")
        print("4. Eliminar un ave.")
        print("5. Salir.")
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









