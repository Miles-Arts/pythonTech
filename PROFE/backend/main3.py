import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

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
    observaciones= []

    for ave in datosAves:
        for obs in ave["observaciones"]:
            observaciones.append({
                "Nombre": ave["nombre"],
                "Fecha": obs["fecha"],
                "Lugar": obs["lugar"], 
                "Avistamientos": obs["avistamientos"]
            })

    df= pd.DataFrame(observaciones)
    print(df)

    if df.empty:
        print("No hay datos disponibles para el análisis")
        return
    
    # Limpieza de datos
    print("\nAnálisis de datos")
    print("\nEstadisticas descriptivas antes de la limpieza")
    print(df.describe(include="all"))

    df= df.drop_duplicates()
    print(df)

    df= df.dropna(subset=["Nombre", "Fecha"])
    print(df)
    
    df["Avistamientos"]= df["Avistamientos"].fillna(df["Avistamientos"].median())
    print(df)

    df["Fecha"]= pd.to_datetime(df["Fecha"])
    print(df)

    df= df[(df["Avistamientos"]>0) & (df["Avistamientos"]<=100)]

    print("\nEstadisticas descriptivas despues de la limpieza")
    print(df.describe(include="all"))

    #Establecer la fecha como el indice del df
    df.set_index("Fecha", inplace=True)
    print(df)

    print("\nTendencia a lo largo del tiempo por mes")
    tendencia= df.resample("ME").sum(numeric_only=True)
    print(tendencia)

    print("\nDistribucion de avistamientos por lugar")
    distribucion= df.groupby("Lugar").sum(numeric_only=True)
    print(distribucion)

    print("\nAvistamientos promedio por ave")
    avistamientos= df.groupby("Nombre").sum(numeric_only=True)
    print(avistamientos)

    # Graficar
    print("Crear grafica")
    fig= plt.figure(figsize=(14, 10))
    fig.canvas.manager.set_window_title("Análisis de datos de aves")

    plt.subplot(2, 2, 1)
    tendencia["Avistamientos"].plot(kind="line", marker="o", color="red")
    plt.title("Tendencia de avistamientos a lo largo del tiempo por mes")
    plt.xlabel("Fecha")
    plt.ylabel("Avistamientos")

    plt.subplot(2, 2, 2)
    distribucion["Avistamientos"].plot(kind="bar", color= "blue")
    plt.title("Distribucion de avistamientos por lugar")
    plt.xlabel("Lugar")
    plt.ylabel("Avistamientos")

    plt.subplot(2, 2, 3)
    avistamientos["Avistamientos"].plot(kind="hist", bins=10, color="purple", alpha=0.7)
    plt.title("Avistamientos promedio")
    plt.xlabel("Avistamientos")
    plt.ylabel("Frecuencia")

    plt.subplot(2, 2, 4)
    colores= plt.cm.Paired(np.arange(len(avistamientos)))
    avistamientos["Avistamientos"].plot(kind="pie", color= colores, startangle=90)
    plt.title("Avistamientos promedio por ave")
    plt.ylabel("")

    plt.tight_layout()
    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()


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
        print("No se encuentra el archivo. Generando nuevos datos")
        generarDatos(datosAves, 5)
    

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


def generarObservaciones():
    fechas = ['2023-04-01', '2023-04-15', '2023-05-01', '2023-05-15', '2023-06-01', None]
    lugares = ['California', 'Nevada', 'Oregon', 'Washington', 'Arizona', None]
    avistamientos= [random.randint(1, 20), None]

    observaciones = []

    for _ in range(random.randint(1, 2)):
        observaciones.append({
            'fecha': random.choice(fechas),
            'lugar': random.choice(lugares),
            'avistamientos': random.choice(avistamientos)
        })

    return observaciones


def generarDatos(datos, cantidad):
    global id

    nombres = ['Colibrí rubí', 'Jilguero dorado', 'Gorrión melódico', 'Pájaro carpintero', 'Mirlo acuático']
    tamaño= [random.randint(8, 15), None]
    colores = ['Verde brillante y rojo', 'Azul y negro', 'Amarillo y blanco', 'Naranja y marrón', 'Gris y azul', None]    
    caracteristica = ['Diminuto, gorjeador rápido', 'Plumaje colorido, vuelo ágil', 'Pico largo y curvado', 'Canto melodioso', 'Patas cortas, alas largas', None]
    comportamientos = ['Se alimenta de néctar', 'Se alimenta de insectos', 'Canta al amanecer', 'Construye nidos en árboles', 'Vuela en bandadas', None]
    
    for _ in range(cantidad):
        id += 1

        ave = {
            'id': id,
            'nombre': random.choice(nombres),
            'descripcion': {
                'tamaño': random.choice(tamaño),
                'color': random.choice(colores),
                'caracteristica': random.choice(caracteristica),
                'comportamiento': random.choice(comportamientos)
            },
            'multimedia': {
                'fotos': [f'foto{random.randint(1, 10)}.jpg' for _ in range(random.randint(1, 3))],
                'sonidos': [f'sonido{random.randint(1, 10)}.mp3' for _ in range(random.randint(1, 3))]
            },
            'observaciones': generarObservaciones()
        }

        datos.append(ave)



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