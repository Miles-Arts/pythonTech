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
    print("Mostrar Aves.")
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
    multimedia["fotos"]=input("Ingrese los nombres de las fotos: (foto1.jpg , foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
    multimedia["sonidos"]=input("Ingrese los nombres de los sonidos: (sonido1.mp3 , sonido2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
    aveNueva["multimedia"]=multimedia

    observaciones=[] 
    while True:

        res=input("¿Desea agr3gar una observación?: \n1. Sí  \n2. No \n : ")
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
    # pass
    print("Actualizar Ave.")
    nombreComun= input("Ingrese el nombre común del ave que desea actualizar: ")
    aveEncontrada= False

    for ave in datosAves:
        if nombreComun == ave["nombreComun"]:
            aveEncontrada=True
            print("Seleccione la opción que desea actualizar: ")
            print("1. Descrpción")
            print("1. Multimedia")
            print("1. Obervaciones")

            opcion=input()

            if opcion == "1":
                descripcion={}
                descripcion["tamano"]=input("Ingrese el nuevo tamaño del Ave: ")
                descripcion["color"]=input("Ingrese el nuevo color del Ave: ")
                descripcion["caracteristica"]=input("Ingrese las nuevas caracteristica del Ave: ")
                descripcion["comportamiento"]=input("Ingrese el nuevo comportamiento del Ave: ")
                ave["descripcion"]=descripcion
                
            elif opcion == "2":   
                multimedia={}
                multimedia["fotos"]=input("Ingrese las rutas de las nuevas fotos: (ruta/foto1.jpg , ruta/foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
                multimedia["sonidos"]=input("Ingrese las rutas de los nuevos sonidos: (ruta/sonido1.mp3 , ruta/sonido2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
                ave["multimedia"]=multimedia

            elif opcion == "3":
                observaciones=[]
                while True:
                    res=input("¿Desea agrgar una observación?: \n1. Sí  \n2. No \n : ")
                    if res == "2":
                        break  

                    observacion={}    
                    observacion["fecha"]=input("Ingrese la nueva fecha de la observación (YYY-MM-DD):")
                    observacion["lugar"]=input("Ingrese el nuevo lugar de la observación: ")
                    observacion["avistamientos"]=input("Ingrese el números de nuevos avistamientos: ")
                    
                    observaciones.append(observacion)

                    ave["observaciones"]=observaciones    
                    datosAves.append(ave)
                print("Ave agregada")

            # else:
            #     print("Opción no válida")   

            # print("Ave actualizada.")     

    if not aveEncontrada:
        print("Nombre común no encontrado.")    

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









