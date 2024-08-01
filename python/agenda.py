# #AGENDA EJEMPLO

# def cargar():
#     agenda={}
#     continua1 = "s"
#     while continua1 == "s":
#         fecha = input("Ingrese la fecha con formato dd/mm/aa: ")
#         continua2 = "s"
#         lista = []
#         while continua2 == "s":
#             hora = input("Ingrese la hora de la activiad con formato hh:mm ")
#             actvidad = input ("Ingrese la descrpción de la actividad: ")
#             lista.append((hora,actvidad))
#             continua2 = input("Ingrese otra actividad para la misma fecha[s/n] ")
#         agenda[fecha]=lista
#         continua1 = input("Ingrese otra fecha[s(n)]: ")    
#     return agenda    

# # cargar()

# def imprimir(agenda):
#     print("Listado completa de la agenda")
#     for fecha in agenda:
#         print("Para la fecha: " , fecha)
#         for hora, actividad in agenda[agenda]:
#             print(hora, actividad)    

# def consultar_fecha(agenda):
#     fecha = input("Ingrese la fecha que desea consultar: ")
#     if fecha in agenda:
#         for hora, actividad in agenda[fecha]:
#             print(hora,actividad)
#     else:
#         print("No hay actividades agendadas para dicha fecha")       

# agenda = cargar()
# imprimir(agenda)
# consultar_fecha(agenda)

print("---Agende su cita Médica---")

def organizador():
    diario=[]
    continuar1="s"
    while continuar1=="s":
        fecha=input("Ingrese día de la semana")
        continua2="s"
        lista=[]
        while continua2=="s":
            try:
                dia=str(input("Ingrese día de la cita: "))
                hora=int(input("ingrese hora de cita: "))
                nombre=str(input("Ingrese su nombre: "))
                lista.append((dia,hora,nombre))
                continua2=str(input("Agendar otra cita para el mismo día? [s/n]"))
            except TypeError:
                print("Ingrese parámetro correcto") 
        diario[fecha]=lista
        try:
            continuar1=str(input("Ingresa otra fecha[s/n]"))
        except TypeError:
            print("Ingrese parámetro correcto")  
    return diario        

def imprimir(diario):
    print("Lista completa de citas: ")
    for fecha in diario:
        print("Para el día: ", fecha)
        for dia,hora in dia[fecha]:
            print(dia,hora)
    

def consultar_dia(diario):
    fecha=str(input("El día que desea consultar")) 
    if fecha in diario:
        for 
    













