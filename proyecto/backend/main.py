datos_arboles=[
    {
        "nombre_comun": "Aliso",
        "descripcion": {
            "tamanio": "30 metros.",
            "color": "Verde oscuro.",
            "caracteristicas": "Fuerte.",
            "comportamiento": "Hábitat natural son los lugares húmedos."
        },
        "multimedia": {
            "fotos":    ["ruta/foto1.jpg", "ruta/foto2.jpg" ],
            "videos":   ["ruta/video1.mp4","ruta/video2.mp4"]
        },
        "observaciones": [
            {"fecha": "2022-04-25", "lugar": "Boyacá - Tuta", "avistamientos": 400},
            {"fecha": "2023-09-10", "lugar": "Boyacá - Tuta", "avistamientos": 200}
        ]

    }
]


def mostrar_arbol():
    print("Motrar Árboles.")
    print(datos_arboles)

def agregar_arbol():
    print("Agrgar nuevo árbol.")
    nuevo_arbol={}

    nombre_comun=input("Ingrese el nombre común: ")
    nuevo_arbol["noombre_comun"]=nombre_comun

    descripcion={}
    descripcion["tamanio"]=input("Ingrese el tamaño del árbol: ")
    descripcion["color"]=input("Ingrese el color del árbol: ")
    descripcion["caracteristica"]=input("Ingrese caracteríticas del árbol: ")
    descripcion["comportamiento"]=input("Ingrese coportamiento del árbol: ")
    nuevo_arbol["descripcion"]=descripcion

    multimedia={}
    multimedia["fotos"]=input("Ingrese las rutas de las fotos: (ruta/foto1.jpg , ruta/foto2.jpg): ").split(",")
    multimedia["videos"]=input("Ingrese las rutas de los vídeos: (ruta/video1.mp4 , ruta/video2.mp4): ").split(",")
    nuevo_arbol["multimedia"]=multimedia

    observaciones=[]
    while True:

        respuesta=input("Agregar nueva obervación: \n\t1. Sí  \n\t2. No \n\t : ")
        if respuesta == "2":
            break

        observacion={}
        observacion["fecha"]=input("Ingrese fecha de obervación (YYYY-MM-DD): ")   
        observacion["lugar"]=input("Lugar de la obervación: ")    
        observacion["avistamientos"]=input("Numero de avistamientos: ")    
        
        observaciones.append(observacion)

    nuevo_arbol["observaciones"]=observaciones
    datos_arboles.append(nuevo_arbol)
    print("--- Árbol Agregado ---")


def actualizar_arbol():
    

def eliminar_arbol():
    pass    

def menu():
    while True:
        print("--- Menú Árboles ---")
        print("\n\t1. Ver todos los árboles.")
        print("\t2. Agregar nuevo árbol.")
        print("\t3. Actualizar datos árbol.")
        print("\t4. Eliminar árbol.")
        print("\t5. Terminar.")
        print("")
        opcion=input("Selecciona una opción: ")
        print("\n")

        if opcion == "1":
            mostrar_arbol()
        elif opcion == "2":
            agregar_arbol()       
        elif opcion == "3":
            actualizar_arbol()
        elif opcion == "4":
            eliminar_arbol()
        elif opcion == "5":
            print("--- FIN ---")
            break
        else:
            print("Opción no válida.")

        print("")

menu()    

