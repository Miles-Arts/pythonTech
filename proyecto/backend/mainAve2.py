import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import random
# import matplotlib as plt
# import matplotlip as plt


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
    observaciones=[]

    for ave in datosAves:
        for observacion in ave["observaciones"]:
            observaciones.append({
                "Nombre": ave["nombre"],
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

    print("\nAvistamientos proyecto ave")
    avistamientos=df.groupby("Nombre").sum(numeric_only=True)
    print(avistamientos)

    # grafica

    print("Crear grafica")

    fig= plt.figure(figsize=(14,10))
    fig.canvas.manager.set_window_title("Análisi de datos aves")
   
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
    plt.title("Avistamientos promedio por ave")
    plt.ylabel("Avistamientos")
 

def cargar_datos():
    global id, datosAves

    try: 
        df=pd.read_csv("datos_aves.csv")
        # print(df)

        datosAves=[]
        aves={}

        # for data_df, row in df.iterrows():
        for _, row in df.iterrows():
            id_ave=row["ID"]

            if id_ave not in aves:
                aves[id_ave]= {
                    "id": id_ave,
                    "nombre": row["Nombre"], 
                    "descripcion": {
                        "tamano": row["Tamaño"],
                        "color": row["Color"],
                        "caracteristica": row[ "Caracteristica"],
                        "comportamiento": row[ "Comportamiento"]
                    },
                    "multimedia": {
                        "fotos": row[ "Fotos"].split(", "),
                        "sonidos": row[ "Sonidos"].split(", ")
                    },
                    "observaciones": [ ] 
                }

            aves[id_ave]["observaciones"].append({
                "fecha": row["Fecha"],
                "lugar": row["Lugar"],
                "avistamientos": row["Avistamientos"]
                })
            
        # print(aves)        

        datosAves=list(aves.values())  
        id=max(aves.keys())

        print(datosAves)  

        print("Datos cargados desde el archivo.")
    except  FileNotFoundError:
        print("No se encuentra el archivo. Generando datos")   
        generarDatos(datosAves, 5)

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


def generarObservaciones():
    pass



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









