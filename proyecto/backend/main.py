datos_arboles=[
    {
        "nombre_comun": "Aliso",
        "descripcion": {
            "tamano": "30 m",
            "color": "Verde oscuro",
            "caracteristicas": "Fuerte",
            "comportamiento": "Hábitat natural son los lugares húmedos"
        },
        "nombre_comun": {
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
    pass

def agregar_arbol():
    pass

def actualizar_arbol():
    pass

def eliminar_arbol():
    pass    

def menu():
    while True:
        print("---Menú Árboles---")
        print("\n\t1. Ver todos los árboles.")
        print("\n2. Agregar nuevo árbol.")
        print("\n3. Actualizar datos árbol")
        print("\n4. eliminar árbol.")
        print("\n5. Terminar.")
        print("")
        opcion=input("Selecciona una opción: ")
        print("")

        if opcion == "1":
            mostrar_arbol()
        elif opcion == "2":
            agregar_arbol()       
        elif opcion == "3":
            actualizar_arbol()
        elif opcion == "4":
            eliminar_arbol()
        elif opcion == "5":
            print("Salir.")
            break
        else:
            print("Opción no válida.")

        print("")

menu()    

