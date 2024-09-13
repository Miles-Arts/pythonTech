import pandas as pd
import numpy as np
import matplotlib as plt

id = 1

datosAves=[
    {
        "id": id,
        "nombre": "Colibrí", 
        "descripcion": {
            "tamano": 9,
            "color": "Verde y Rojo",
            "caracteristica": "Pequeño",
            "comportamiento": "Se alimenta de neétar"
        },
        "multimedia": {
            "fotos": ["foto1.jpg","foto2.jpg" ],
            "sonidos": ["sonidos1.mp3"]
        },
        "observaciones": [
            {"fecha": "2024-05-01", "lugar": "Boyacá", "avistamientos": 5},
            {"fecha": "2024-04-01", "lugar": "Cundinamarca", "avistamientos": 10}
        ] 
    }
]

def mostrarAves():
    datos=[]
    # datos=[{"id": 1, "nombre": "Perro", "tamano": 10, "color": "rojo", "caracteristicas": "peludo", "comportamiento": "ladrar" }]

    for ave in datosAves:
        
        #Para guardar o sacar infromaicón de una 
        #Lista utilizamos bucle.,
        observaciones_fecha=[observacion["fecha"] for observacion  in ave["observaciones"]] 
        observaciones_lugar=[observacion["lugar"] for observacion  in ave["observaciones"]] 
        observaciones_avistamientos=[observacion["avistamientos"] for observacion  in ave["observaciones"]] 

        datos.append({
            "ID": ave["id"],
            "Nombre": ave["nombre"],
            "Tamaño":  ave["descripcion"]["tamano"],
            "Color": ave["descripcion"]["color"],
            "Caracteristica": ave["descripcion"]["caracteristica"],
            "Comportamiento": ave["descripcion"]["comportamiento"],
            "Fotos": ", ".join(ave["multimedia"]["fotos"]),
            "Sonidos": ", ".join(ave["multimedia"]["sonidos"]),
            "Fecha": ", ".join(map(str, observaciones_fecha)),
            "Lugar": ", ".join(map(str, observaciones_lugar)),
            "Avistamientos": ", ".join(map(str,observaciones_avistamientos))
        })

    df=pd.DataFrame(datos)
    print(df)    

def agregarAve():
    global id
    id+=1

    nombre=input("Ingrese el nombre: ")

    descripcion={}
    descripcion["tamano"]=int(input("Ingrese el tamaño del Ave: "))
    descripcion["color"]=input("Ingrese el color del Ave: ")
    descripcion["caracteristica"]=input("Ingrese la caracteristica del Ave: ")
    descripcion["comportamiento"]=input("Ingrese la comportamiento del Ave: ")

    multimedia={}
    multimedia["fotos"]=input("Ingrese los nombres de las fotos: (foto1.jpg , foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
    multimedia["sonidos"]=input("Ingrese los nombres de los sonidos: (sonido1.mp3 , sonido2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]

    observaciones=[] 
    while True:

        observacion={}  
        observacion["fecha"]=input("Ingrese la fecha de la observación (YYY-MM-DD) o 'fin' para terminar: ")
        
        # res=input("¿Desea agr3gar una observación?: \n1. Sí  \n2. No \n : ")
        if observacion["fecha"].lower() == "fin":
            break
         
        observacion["lugar"]=input("Ingrese el lugar de la observación: ")
        observacion["avistamientos"]=input("Ingrese el números de avistamientos: ")
        
        observaciones.append(observacion)
  
    datosAves.append({
        "id": id,
        "nombre": nombre,
        "descripcion": descripcion,
        "multimedia": multimedia,
        "observaciones": observaciones

    })
    
def actualizarAve():
    id_ave= int(input("Ingrese el ID del ave que desea actualizar: "))
    aveEncontrada= False

    for ave in datosAves:
        if id_ave == ave["id"]:
            aveEncontrada=True
            print("Seleccione la opción que desea actualizar: ")
            print("1. Descrpción")
            print("1. Multimedia")
            print("1. Obervaciones")

            opcion=input()

            if opcion == "1":
                descripcion={}
                descripcion["tamano"]=int(input("Ingrese el nuevo tamaño del Ave: "))
                descripcion["color"]=input("Ingrese el nuevo color del Ave: ")
                descripcion["caracteristica"]=input("Ingrese las nuevas caracteristica del Ave: ")
                descripcion["comportamiento"]=input("Ingrese el nuevo comportamiento del Ave: ")
                ave["descripcion"]=descripcion
                
            elif opcion == "2":   
                multimedia={}
                multimedia["fotos"]=input("Ingrese los nombres de las nuevas fotos: (foto1.jpg , foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
                multimedia["sonidos"]=input("Ingrese los nombres de los nuevos sonidos: (sonido1.mp3 , sonido2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
                ave["multimedia"]=multimedia

            elif opcion == "3":
                observaciones=[]
                while True:
                    observacion={} 
                    observacion["fecha"]=input("Ingrese la nueva fecha de la observación (YYY-MM-DD):")

                    if observacion["fecha"].lower() == "fin":
                        break  

                    observacion["lugar"]=input("Ingrese el nuevo lugar de la observación: ")
                    observacion["avistamientos"]=input("Ingrese el números de nuevos avistamientos: ")
                    
                    observaciones.append(observacion)

                    ave["observaciones"]=observaciones    
                    # datosAves.append(ave)
                print("Ave agregada")

            # else:
            #     print("Opción no válida")   

            # print("Ave actualizada.")     

    if not aveEncontrada:
        print("Nombre no encontrado.")    

def eliminarAve():
    id_ave= int(input("Ingrese el ID del ave que desea actualizar: "))
    longitudAnterior = len(datosAves)
        
    datosAves[:]=[ave for ave in datosAves if id_ave != ave["id"]]  
    
    if longitudAnterior > len(datosAves):
        print("Ave eliminada")
    else:
        print("ID 4no encontrado.")    

def analisis_datos():
    pass     

def cargar_datos():
    global id, datosAves

    try: 
        df=pd.read_csv("datos_aves.csv")
        print(df)

        print("Datos cargados desdeel archivo.")
    except  FileNotFoundError:
        print("No se encuentra el archivo")   




def guardar_datos():
    datos=[]

    for ave in datosAves:
        for observaciones in ave["observaciones"]:
            datos.append({
                "ID": ave["id"],
                "Nombre": ave["nombre"],
                "Tamaño":  ave["descripcion"]["tamano"],
                "Color": ave["descripcion"]["color"],
                "Caracteristica": ave["descripcion"]["caracteristica"],
                "Comportamiento": ave["descripcion"]["comportamiento"],
                "Fotos": ", ".join(ave["multimedia"]["fotos"]),
                "Sonidos": ", ".join(ave["multimedia"]["sonidos"]),
                "Fecha": observaciones["fecha"],
                "Lugar": observaciones["lugar"],
                "Avistamientos": observaciones["avistamientos"]
            })

    df=pd.DataFrame(datos)
    df.to_csv("datos_aves.csv", index=False)
    print("Datos gurdados en el archivo datos_aves.csv")    
     

def menu():
    cargar_datos()

    while True:
        print("\n---Menú gestión de Aves---")
        print("\n1. Ver todas las aves.")
        print("2. Agregar nueva ave.")
        print("3. Actualizar datos de una ave.")
        print("4. Eliminar un ave.")
        print("5. Análisis de datos.")
        print("6. Guardar datos.")
        print("7. Salir.")
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
            analisis_datos()
        elif opcion == "6":
            guardar_datos()
        elif opcion == "7":
            print("Salir.")
            break    
        else: 
            print("Opción no válida")

        print("")

menu()









