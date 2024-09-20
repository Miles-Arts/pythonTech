datos_arboles=[
    {
        "nombre_comun": "Aliso",
        "descripcion": {
            "tamanio": "30 metros.",
            "color": "Verde oscuro.",
            "caracteristicas": "Fuerte.",
            "comportamiento": "Hábitat natural en los lugares húmedos."
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
    print("--- Mostrar Árboles ---")
    print(datos_arboles)

def agregar_arbol():
    print("--- Agregar nuevo árbol ---")
    nuevo_arbol={}

    nombre_comun=input("Ingrese el nombre común: ")
    nuevo_arbol["nombre_comun"]=nombre_comun

    descripcion={}
    descripcion["tamanio"]=input("Ingrese el tamaño del árbol: ")
    descripcion["color"]=input("Ingrese el color del árbol: ")
    descripcion["caracteristica"]=input("Ingrese características del árbol: ")
    descripcion["comportamiento"]=input("Ingrese comportamiento del árbol: ")
    nuevo_arbol["descripcion"]=descripcion

    multimedia={}
    multimedia["fotos"]=input("Ingrese las rutas de las fotos: (ruta/foto1.jpg , ruta/foto2.jpg): ").split(",")
    multimedia["videos"]=input("Ingrese las rutas de los vídeos: (ruta/video1.mp4 , ruta/video2.mp4): ").split(",")
    nuevo_arbol["multimedia"]=multimedia

    observaciones=[]
    while True:

        respuesta=input("Agregar nueva observación: \n\t1. Sí  \n\t2. No \n\t\t --> : ")
        if respuesta == "2":
            break

        observacion={}
        observacion["fecha"]=input("Ingrese fecha de observación (YYYY-MM-DD): ")   
        observacion["lugar"]=input("Lugar de la observación: ")    
        observacion["avistamientos"]=input("Número de avistamientos: ")    
        
        observaciones.append(observacion)

    nuevo_arbol["observaciones"]=observaciones
    datos_arboles.append(nuevo_arbol)
    print("--- Árbol Agregado ---")

def actualizar_arbol():
    print("--- Actualizar Árbol ---")
    nombre_comun=input("\nIngrese nombre común del árbol: ")
    arbol_encontrado=False

    for arbol in datos_arboles:
        if nombre_comun == arbol["nombre_comun"]:
            arbol_encontrado = True
            print("-"*40)
            print("\nIngrese opción a actualizar: ")
            print("\n\t1. Descripción.")
            print("\t2. Multimedia.")
            print("\t3. Observaciones.")

            opcion=input("\t\t--> : ")

            if opcion == "1":
                descripcion={}
                descripcion["tamanio"]=input("Ingrese el tamaño del árbol: ")
                descripcion["color"]=input("Ingrese el color del árbol: ")
                descripcion["caracteristica"]=input("Ingrese características del árbol: ")
                descripcion["comportamiento"]=input("Ingrese comportamiento del árbol: ")
                arbol["descripcion"]=descripcion

            elif opcion == "2":
                multimedia={}
                multimedia["fotos"]=input("Ingrese las rutas de las fotos: (ruta/foto1.jpg , ruta/foto2.jpg): ").split(",")    
                multimedia["videos"]=input("Ingrese las rutas de los vídeos: (ruta/video1.mp4 , ruta/video2.mp4): ").split(",")    
                arbol["multimedia"]=multimedia

            elif opcion == "3":
                observaciones=[]
                while True:
                    respuesta=input("Agregar nueva observación: \n\t1. Sí  \n\t2. No \n\t : ")
                    if respuesta == "2":
                        break  

                    observacion={}
                    observacion["fecha"]=input("Ingrese fecha de observación (YYYY-MM-DD): ")   
                    observacion["lugar"]=input("Lugar de la observación: ")    
                    observacion["avistamientos"]=input("Número de avistamientos: ") 

                    observaciones.append(observacion)

                    arbol["observaciones"]=observaciones
                    datos_arboles.append(arbol)
                    
                print("--- Árbol Actualizado ---")

            else:
                print("Opción no válida")   
            print("--- Árbol actualizado ---")     

    if not arbol_encontrado:
        print("Nombre común de árbol no encontrado.")                
            
def eliminar_arbol():
    print("--- Eliminar Árbol ---") 
    nombre_comun=input("Ingrese el árbol a eliminar:  ")
    longitud_anterior=len(datos_arboles)

    datos_arboles[:]=[arbol for arbol in datos_arboles if nombre_comun != arbol["nombre_comun"]]
    if longitud_anterior > len(datos_arboles):
        print("--- Árbol Eliminado ---")
    else:
        print("Nombre de árbol común no encontrado.")  

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
