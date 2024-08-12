def guardar_puntajes(nombre_archivo, puntajes):
    archivo=open(nombre_archivo, "w")

    for nombre, puntaje, tiempo in puntajes:

        archivo.write(nombre+","+str(puntaje)+","+tiempo+"\n")

    archivo.close()

def recuperar_puntajes(nombre_archivo):

    puntajes=[]
    archivo=open(nombre_archivo, "r")

    for linea in archivo:
        nombre, puntaje, tiempo = linea.rstrip("\n").split(",")
        puntajes.append((nombre, int(puntaje), tiempo))

    archivo.close()

    return puntajes
