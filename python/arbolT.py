datos_arboles=[
    {
        "nombre_comun": "Duraznillo",
        "descripcion": {
            "tamano": "20 mt",
            "color": "Verde",
            "caracteristicas": "Mediano",
            "comportamiento": "Crecimiento rápido"
        },
        "multimedia": {
            "fotos": ["ruta/foto1.png", "ruta/foto2.png"],
            "video": ["ruta/video1.mp4", "ruta/video2.mp4"]
        },
        "observaciones": [
            {"fecha": "2024-06-08", "lugar": "Tuta - San Nicolás", "avistamiento": 20},
            {"fecha": "2024-08-20", "lugar": "Tuta - La Playa","avistamientos": 50}
        ]
    }
]


def mostrar_arboles():
    print(datos_arboles)

def agregar_arboles():
    arbol_nuevo={}

    nombre_comun=input("Ingrese el nombre del árbol: ")
    arbol_nuevo["nombre_comun"]=nombre_comun

    descripcion={}
    descripcion["tamano"]=input("Ingrese tamaño del árbol en mt: ")
    descripcion["color"]=input("Ingrese color del árbol: ")
    descripcion["caracteristicas"]=input("Ingrese caracteristicas del árbol: ")
    descripcion["comportamiento"]=input("Ingrese comportamiento del árbol: ")
    arbol_nuevo["descrpcion"]=descripcion


    multimedia={}
    multimedia["foto"]=input("Ingrese las rutas de las fotos ruta/foto1.png : ")
    multimedia["video"]=input("Ingrse las rutas de los videos ruta/video1.png : ")
    arbol_nuevo["mutimedia"]=multimedia

    observaciones=[]
    while True:
            
            

            observacion={}
            observacion["fecha"]=input("Ingrese fecha (YYYY-MM-DD)")
            observacion["lugar"]=input("Ingrese lugar.")
            observacion["avistamiento"]=input("Ingrese números de avistamientos")
            observaciones.append(observacion)

    arbol_nuevo["observaciones"]=observaciones   
    datos_arboles.append(arbol_nuevo)
    print("Árbol ingresado")     
   

def actualizar_arboles():
    pass

def eliminar_arboles():
    pass


def menu_arboles():
    while True:
        print("----Menú Árboles Tuta----\n")
        print("1. Mostrar Árboles.")
        print("2. Agregar Árboles.")
        print("3. Actualizar Árboles.")
        print("4. Eliminar Árboles.")
        print("5. Salir del menú.\n")
        opcion = input(("Ingrese un numero del menú: "))

        if opcion == "1":
            mostrar_arboles()
        elif opcion == "2":
            agregar_arboles()
        elif opcion == "3":
            actualizar_arboles()
        elif opcion == "4":
            eliminar_arboles()
        elif opcion == "5":
            break
        print("Ingrese un número válido: ")                    








# print("Hola")
menu_arboles()