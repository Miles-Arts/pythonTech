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

cargar()

