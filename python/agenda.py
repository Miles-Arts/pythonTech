#AGENDA EJEMPLO

def cargar():
    agenda={}
    continua1 = "s"
    while continua1 == "s":
        fecha = input("Ingrese la fecha con formato dd/mm/aa: ")
        continua2 = "s"
        lista = []
        while continua2 == "s":
            hora = input("Ingrese la hora de la activiad con formato hh:mm ")
            actvidad = input ("Ingrese la descrpción de la actividad: ")
            lista.append((hora,actvidad))
            continua2 = input("Ingrese otra actividad para la misma fecha[s/n] ")
        agenda[fecha]=lista
        continua1 = input("Ingrese otra fecha[s(n)]: ")    
    return agenda    

# cargar()

def imprimir(agenda):
    print("Listado completa de la agenda")
    for fecha in agenda:
        print("Para la fecha: " , fecha)
        for hora, actividad in agenda[agenda]:
            print(hora, actividad)    

def consultar_fecha(agenda):
    fecha = input("Ingrese la fecha que desea consultar: ")
    if fecha in agenda:
        for hora, actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")                   