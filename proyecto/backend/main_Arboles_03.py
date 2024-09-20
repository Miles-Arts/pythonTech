import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

datos_arboles=[
    {
        "id": id,
        "nombre": "Aliso",
        "descripcion": {
            "tamano": 30,
            "color": "Verde oscuro.",
            "caracteristica": "Fuerte.",
            "comportamiento": "Hábitat natural en los lugares húmedos."
        },
        "multimedia": {
            "fotos":    ["foto1.jpg", "foto2.jpg" ],
            "videos":   ["video1.mp4"]
        },
        "observaciones": [
            {"fecha": "2022-04-25", "lugar": "Boyacá - Tuta", "avistamientos": 400},
            {"fecha": "2023-09-10", "lugar": "Boyacá - Tuta", "avistamientos": 200}
        ]

    }
]


def mostrar_arboles():
    datos=[]

    for arbol in datos_arboles:
        
    
        observaciones_fecha=[observacion["fecha"] for observacion  in arbol["observaciones"]] 
        observaciones_lugar=[observacion["lugar"] for observacion  in arbol["observaciones"]] 
        observaciones_avistamientos=[observacion["avistamientos"] for observacion  in arbol["observaciones"]] 

        datos.append({
            "ID": arbol["id"],
            "Nombre": arbol["nombre"],
            "Tamaño":  arbol["descripcion"]["tamano"],
            "Color": arbol["descripcion"]["color"],
            "Caracteristica": arbol["descripcion"]["caracteristica"],
            "Comportamiento": arbol["descripcion"]["comportamiento"],
            "Fotos": ", ".join(arbol["multimedia"]["fotos"]),
            "Videos": ", ".join(arbol["multimedia"]["videos"]),
            "Fecha": ", ".join(map(str, observaciones_fecha)),
            "Lugar": ", ".join(map(str, observaciones_lugar)),
            "Avistamientos": ", ".join(map(str,observaciones_avistamientos))
        })

    df=pd.DataFrame(datos)
    print(df)    

def agregar_arbol():
    global id
    id+=1

    nombre=input("Ingrese el nombre: ")

    descripcion={}
    descripcion["tamano"]=int(input("Ingrese el tamaño del Árbol: "))
    descripcion["color"]=input("Ingrese el color del Árbol: ")
    descripcion["caracteristica"]=input("Ingrese la caracteristica del Árbol: ")
    descripcion["comportamiento"]=input("Ingrese la comportamiento del Árbol: ")

    multimedia={}
    multimedia["fotos"]=input("Ingrese los nombres de las fotos: (foto1.jpg , foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
    multimedia["videos"]=input("Ingrese los nombres de los vídeos: (videos1.mp3 , videos2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]

    observaciones=[] 
    while True:

        observacion={}  
        observacion["fecha"]=input("Ingrese la fecha de la observación (YYY-MM-DD) o 'fin' para terminar: ")
        
        if observacion["fecha"].lower() == "fin":
            break
         
        observacion["lugar"]=input("Ingrese el lugar de la observación: ")
        observacion["avistamientos"]=input("Ingrese el números de avistamientos: ")
        
        observaciones.append(observacion)
  
    datos_arboles.append({
        "id": id,
        "nombre": nombre,
        "descripcion": descripcion,
        "multimedia": multimedia,
        "observaciones": observaciones

    })
    
def actualizar_arbol():
    id_arbol= int(input("Ingrese el ID del Árbol que desea actualizar: "))
    arbol_encontrado= False

    for arbol in datos_arboles:
        if id_arbol == arbol["id"]:
            arbol_encontrado=True
            print("Seleccione la opción que desea actualizar: ")
            print("1. Descrpción")
            print("1. Multimedia")
            print("1. Obervaciones")

            opcion=input()

            if opcion == "1":
                descripcion={}
                descripcion["tamano"]=int(input("Ingrese el nuevo tamaño del Árbol: "))
                descripcion["color"]=input("Ingrese el nuevo color del Árbol: ")
                descripcion["caracteristica"]=input("Ingrese las nuevas caracteristica del Árbol: ")
                descripcion["comportamiento"]=input("Ingrese el nuevo comportamiento del Árbol: ")
                arbol["descripcion"]=descripcion
                
            elif opcion == "2":   
                multimedia={}
                multimedia["fotos"]=input("Ingrese los nombres de las nuevas fotos: (foto1.jpg , foto2.jpg): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
                multimedia["videos"]=input("Ingrese los nombres de los nuevos vídeos: videos1.mp3 ,videos2.mp3): ").split(",") # ["ruta/foto1.jpg , ruta/foto2.jpg"]
                arbol["multimedia"]=multimedia

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

                    arbol["observaciones"]=observaciones    
                    
                print("Ave agregada")
    

    if not arbol_encontrado:
        print("Nombre no encontrado.")    

def eliminar_arbol():
    id_arbol= int(input("Ingrese el ID del ave que desea actualizar: "))
    longitudAnterior = len(datos_arboles)
        
    datos_arboles[:]=[arbol for arbol in datos_arboles if id_arbol != arbol["id"]]  
    
    if longitudAnterior > len(datos_arboles):
        print("Árbol eliminada")
    else:
        print("ID no encontrado.")    

def analisis_datos():
    observaciones=[]

    for arbol in datos_arboles:
        for observacion in arbol["observaciones"]:
            observaciones.append({
                "Nombre": arbol["nombre"],
                "Fecha": observacion["fecha"],
                "Lugar": observacion["lugar"],
                "Avistamientos": observacion["avistamientos"]
            })

    df=pd.DataFrame(observaciones)
    print(df) 

    if df.empty:
        print("No hay datos disponibles para el análisis.")       
        return
    
    print("\nAnálisis de datos.")
    print("\nEstadistica descriptivas antes de la limpieza.")
    print(df.describe(include="all"))

    df=df.drop_duplicates()
    print(df)

    df=df.dropna(subset=["Nombre","Fecha"])
    print(df)

    df["Avistamientos"]=df["Avistamientos"].fillna(df["Avistamientos"].median())
    print(df)

    df["Fecha"]=pd.to_datetime(df["Fecha"])
    print(df)

    df=df[ ( df["Avistamientos"]>0 ) & ( df["Avistamientos"] <= 100 ) ]
    print(df)

    print("\nEstadistica descriptivas despues de la limpieza.")
    print(df.describe(include="all"))

    # Establecer la fecha como índice DF
    df.set_index("Fecha", inplace=True)
    print(df)

    print("\nTendencia a lo largo del tiempo por mes.")
    tendencia=df.resample("ME").sum(numeric_only=True)
    print(tendencia)


    print("\nDistribución de avistamientos por lugar")
    distribucion=df.groupby("Lugar").sum(numeric_only=True)
    print(distribucion)

    print("\nAvistamientos proyecto árbol")
    avistamientos=df.groupby("Nombre").sum(numeric_only=True)
    print(avistamientos)

    # grafica

    print("Crear grafica")

    fig= plt.figure(figsize=(14,10))
    fig.canvas.manager.set_window_title("Análisi de datos arboles")
   
    plt.subplot(2,2,1)
    tendencia["Avistamientos"].plot(kind="line", marker="o", color="red")
    plt.title("Tendencia a lo largo del tiempo por mes")
    plt.xlabel("Fecha")
    plt.ylabel("Avistaiento")

    plt.subplot(2,2,2)
    distribucion["Avistamientos"].plot(kind="bar",color="blue")
    plt.title("distribucion de avistamientos por lugar")
    plt.xlabel("Lujar")
    plt.ylabel("Avistamiento")

    plt.subplot(2,2,3)
    avistamientos["Avistamientos"].plot(kind="hist", bins=10, color="purple", alpha=0.7)
    plt.title("Avistamientos promedio por ave")
    plt.xlabel("Avistamientos")
    plt.ylabel("Frecuencia")

    plt.tight_layout()
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()

    plt.subplot(2,2,4)
    colores=plt.cm.Paired(np.arange(len(avistamientos)))
    avistamientos["Avistamientos"].plot(kind="pie", color= colores, startangle=90)
    plt.title("Avistamientos promedio por árbol")
    plt.ylabel("Avistamientos") 

def cargar_datos():
    global id, datos_arboles

    try: 
        df=pd.read_csv("datos_arboles.csv")

        datos_arboles=[]
        arboles={}

        for _, row in df.iterrows():
            id_arbol=row["ID"]

            if id_arbol not in arboles:
                arboles[id_arbol]= {
                    "id": id_arbol,
                    "nombre": row["Nombre"], 
                    "descripcion": {
                        "tamano": row["Tamaño"],
                        "color": row["Color"],
                        "caracteristica": row[ "Caracteristica"],
                        "comportamiento": row[ "Comportamiento"]
                    },
                    "multimedia": {
                        "fotos": row[ "Fotos"].split(", "),
                        "videos": row[ "Videos"].split(", ")
                    },
                    "observaciones": [ ] 
                }

            arboles[id_arbol]["observaciones"].append({
                "fecha": row["Fecha"],
                "lugar": row["Lugar"],
                "avistamientos": row["Avistamientos"]
                })
            
        # print(aves)        

        datos_arboles=list(arboles.values())  
        id=max(arboles.keys())

        print(datos_arboles)  

        print("Datos cargados desde el archivo.")
    except  FileNotFoundError:
        print("No se encuentra el archivo. Generando datos")   
        generarDatos(datos_arboles, 5)

def guardar_datos():
    datos=[]

    for arbol in datos_arboles:
        for observaciones in arbol["observaciones"]:
            datos.append({
                "ID": arbol["id"],
                "Nombre": arbol["nombre"],
                "Tamaño":  arbol["descripcion"]["tamano"],
                "Color": arbol["descripcion"]["color"],
                "Caracteristica": arbol["descripcion"]["caracteristica"],
                "Comportamiento": arbol["descripcion"]["comportamiento"],
                "Fotos": ", ".join(arbol["multimedia"]["fotos"]),
                "Videos": ", ".join(arbol["multimedia"]["videos"]),
                "Fecha": observaciones["fecha"],
                "Lugar": observaciones["lugar"],
                "Avistamientos": observaciones["avistamientos"]
            })

    df=pd.DataFrame(datos)
    df.to_csv("datos_arboles.csv", index=False)
    print("Datos gurdados en el archivo datos_arboles.csv")    

def generarObservaciones():
    pass

def generarDatos():
    pass

def menu():
    cargar_datos()

    while True:
        print("\n---Menú gestión de Árboles---")
        print("\n1. Ver todos los Árboles.")
        print("2. Agregar nuevo Árbol.")
        print("3. Actualizar datos de un Árbol.")
        print("4. Eliminar un Árbol.")
        print("5. Análisis de datos.")
        print("6. Guardar datos.")
        print("7. Salir.")
        print("")
        opcion = input("Selecione una opción: ")
        print("")

        if opcion == "1":
            mostrar_arboles()
        elif opcion == "2":
            agregar_arbol()
        elif opcion == "3":
            actualizar_arbol()
        elif opcion == "4":
            eliminar_arbol()
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




























print("-"*50)