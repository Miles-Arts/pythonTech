import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


id= 1

datosAves=[
    {
        "id": id,
        "nombre": "Colibrí",
        "descripcion": {
            "tamaño": 9,
            "color": "Verde y Rojo",
            "caracteristica": "Pequeño",
            "comportamiento": "Se alimenta de néctar"
        },
        "multimedia":{
            "fotos": ["foto1.jpg", "foto2.jpg"], 
            "sonidos": ["sonido1.mp3"]
        },
        "observaciones": [
            {"fecha": "2024-05-01", "lugar": "Boyacá", "avistamientos": 5},
            {"fecha": "2024-04-01", "lugar": "Cundinamarca", "avistamientos": 10}
        ]
    }
]


def mostrarAves():
    datos= []

    for ave in datosAves:
        
        obsFecha= [obs["fecha"] for obs in ave["observaciones"]]
        obsLugar= [obs["lugar"] for obs in ave["observaciones"]]
        obsAvistamientos= [obs["avistamientos"] for obs in ave["observaciones"]]

        datos.append({
            "ID": ave["id"],
            "Nombre": ave["nombre"],
            "Tamaño": ave["descripcion"]["tamaño"],
            "Color": ave["descripcion"]["color"],
            "Caracteristica": ave["descripcion"]["caracteristica"],
            "Comportamiento": ave["descripcion"]["comportamiento"],
            "Fotos": ", ".join(ave["multimedia"]["fotos"]),
            "Sonidos": ", ".join(ave["multimedia"]["sonidos"]),
            "Fecha": ", ".join(map(str, obsFecha)),
            "Lugar": ", ".join(map(str, obsLugar)),
            "Avistamientos": ", ".join(map(str, obsAvistamientos))
        })


    df= pd.DataFrame(datos)
    print(df)


def agregarAve():
    global id

    id+=1

    nombre= input("Ingrese el nombre: ")

    descripcion= {}
    descripcion["tamaño"]= int(input("Ingrese el tamaño: "))
    descripcion["color"]= input("Ingrese el color: ")
    descripcion["caracteristica"]= input("Ingrese las caracteristica: ")
    descripcion["comportamiento"]= input("Ingrese los comportamiento: ")

    multimedia= {}
    multimedia["fotos"]= input("Ingrese los nombres de las fotos (foto1.jpg,foto2.jpg): ").split(",") 
    multimedia["sonidos"]= input("Ingrese los nombres de los sonidos (sonido1.mp3,sonido2.mp3): ").split(",")

    observaciones= []
    while True:
        observacion= {}
        observacion["fecha"]= input("Ingrese la fecha de la observación (YYYY-MM-DD) o 'fin' para terminar: ")

        if observacion["fecha"].lower() == "fin":
            break
                
        observacion["lugar"]= input("Ingrese el lugar de la observación: ")
        observacion["avistamientos"]= input("Ingrese el numero de avistamientos: ")

        observaciones.append(observacion)


    datosAves.append({
        "id": id,
        "nombre": nombre,
        "descripcion": descripcion,
        "multimedia": multimedia,
        "observaciones": observaciones
    })
    
    print("Ave agregada")
    

def actualizarAve():
    idAve= int(input("Ingrese el id de la ave que desea actualizar: "))
    aveEncontrada= False

    for ave in datosAves:
        if idAve == ave["id"]:
            aveEncontrada= True
            print("Seleccione la opción que desea actualizar: ")
            print("1. Descripción")
            print("2. Multimedia")
            print("3. Observaciones")

            opcion= input()

            if opcion == "1":
                descripcion= {}
                descripcion["tamaño"]= int(input("Ingrese el nuevo tamaño: "))
                descripcion["color"]= input("Ingrese el nuevo color: ")
                descripcion["caracteristica"]= input("Ingrese las nuevas caracteristica: ")
                descripcion["comportamiento"]= input("Ingrese los nuevos comportamiento: ")
                ave["descripcion"]= descripcion

            elif opcion == "2":
                multimedia= {}
                multimedia["fotos"]= input("Ingrese los nombres de las nuevas fotos (foto1.jpg,foto2.jpg): ").split(",")
                multimedia["sonidos"]= input("Ingrese los nombres de los nuevos sonidos (sonido1.mp3,sonido2.mp3): ").split(",")
                ave["multimedia"]= multimedia

            elif opcion == "3":
                observaciones= []
                while True:
                    observacion= {}
                    observacion["fecha"]= input("Ingrese la fecha de la observación (YYYY-MM-DD) o 'fin' para terminar: ")

                    if observacion["fecha"].lower() == "fin":
                        break

                    observacion["lugar"]= input("Ingrese el nuevo lugar de la observación: ")
                    observacion["avistamientos"]= input("Ingrese el nuevo numero de avistamientos: ")

                    observaciones.append(observacion)

                ave["observaciones"]= observaciones

            print("Ave actualizada")
            
    
    if not aveEncontrada:
        print("Ave no encontrada.")
           

def eliminarAve():
    idAve= int(input("Ingrese id del ave que desea eliminar: "))
    longitudAnterior= len(datosAves)
   
    datosAves[:]= [ave for ave in datosAves if idAve != ave["id"]]

    if longitudAnterior > len(datosAves):
        print("Ave eliminada")
    else:
        print("id no encontrado")


def analisisDatos():
    pass


def cargarDatos():
    global id, datosAves

    try:
        df= pd.read_csv("datos_aves.csv")
        
        datosAves= []
        aves= {}
        
        for _, row in df.iterrows():
            idAve= row["ID"]

            if idAve not in aves:
                aves[idAve]=  {
                    "id": idAve,
                    "nombre": row["Nombre"],
                    "descripcion": {
                        "tamaño": row["Tamaño"],
                        "color": row["Color"],
                        "caracteristica": row["Caracteristica"],
                        "comportamiento": row["Comportamiento"]
                    },
                    "multimedia":{
                        "fotos": row["Fotos"].split(", "), 
                        "sonidos": row["Sonidos"].split(", ")
                    },
                    "observaciones": []
                }

            aves[idAve]["observaciones"].append({
                "fecha": row["Fecha"], 
                "lugar":row["Lugar"], 
                "avistamientos": row["Avistamientos"]
                })


        datosAves= list(aves.values())
        id= max(aves.keys())
        
        print("Datos cargados desde el archivo.")
    except FileNotFoundError:
        print("No se encuentra el archivo")
    


def guardarDatos():
    datos=[]

    for ave in datosAves: 
        for obs in ave["observaciones"]: 
            datos.append({
                "ID": ave["id"],
                "Nombre": ave["nombre"],
                "Tamaño": ave["descripcion"]["tamaño"],
                "Color": ave["descripcion"]["color"],
                "Caracteristica": ave["descripcion"]["caracteristica"],
                "Comportamiento": ave["descripcion"]["comportamiento"],
                "Fotos": ", ".join(ave["multimedia"]["fotos"]),
                "Sonidos": ", ".join(ave["multimedia"]["sonidos"]),
                "Fecha": obs["fecha"],
                "Lugar": obs["lugar"],
                "Avistamientos": obs["avistamientos"]
            })

    df= pd.DataFrame(datos)
    df.to_csv("datos_aves.csv", index= False)

    print("Datos guardados en el archivo 'datos_aves.csv'.")


def menu():
    cargarDatos()

    while True:
        print("\nMenú de Gestión de Aves")
        print("1. Ver todas las aves")
        print("2. Agregar nueva ave")
        print("3. Actualizar datos de una ave")
        print("4. Eliminar una ave")
        print("5. Análisis de datos")
        print("6. Guardar datos")
        print("7. Salir")

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
            analisisDatos()
        elif opcion == "6":
            guardarDatos()
        elif opcion == "7":
            print("Salir")
            break
        else:
            print("Opción no valida")

menu()