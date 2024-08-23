datosAves=[
    {
        "nombreComun": "Colibrí", 
        "descripcion": {
            "tamano": "9 cm",
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

    nombreComun=input("Ingrese el nombre común: ")
    aveNueva["nombreComun"]=nombreComun

    descripcion={}
    descripcion["tamano"]=input("Ingrese el tamaño del Ave: ")
    descripcion["color"]=input("Ingrese el color del Ave: ")
    descripcion["caracteristica"]=input("Ingrese la caracteristica del Ave: ")
    descripcion["comportamiento"]=input("Ingrese la comportamiento del Ave: ")
    aveNueva["descripcion"]=descripcion

    multimedia={}
    multimedia["fotos"]=input("Ingrese las rutas de las fotos: (ruta/foto1.jpg , ruta/foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
    multimedia["sonidos"]=input("Ingrese las rutas de los sonidos: (ruta/sonido1.mp3 , ruta/sonido2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
    aveNueva["multimedia"]=multimedia

    observaciones=[] 
    while True:

        res=input("¿Desea agrgar una observación?: \n1. Sí  \n2. No \n : ")
        if res == "2":
            break
            
        observacion={}    
        observacion["fecha"]=input("Ingrese la fecha de la observación (YYY-MM-DD):")
        observacion["lugar"]=input("Ingrese el lugar de la observación: ")
        observacion["avistamientos"]=input("Ingrese el números de avistamientos: ")
        
        observaciones.append(observacion)

    aveNueva["observaciones"]=observaciones    
    datosAves.append(aveNueva)
    print("Ave agregada")


def actualizarAve():
    pass

def eliminarAve():
    print("Eliminar Ave.")   
    nombreComun= input("Ingrese la especie que desea eliminar: ")
    longitudAnterior = len(datosAves)
        
    datosAves[:]=[ave for ave in datosAves if nombreComun != ave["nombreComun"]]  
    if longitudAnterior > len(datosAves):
        print("Ave eliminada")
    else:
        print("Nombre común no encontrado.")    
            
     










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









