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

# MEDICO

# print("---Agende su cita Médica---")
# print("")

# def organizador():
#     diario={}
#     continuar1="s"
#     while continuar1=="s":
#         try:
#             print("Lunes - Martes - Miércoles - Jueves - Viernes")
#             dia_semana=input("Ingrese día de la semana: ")
#         except TypeError:
#             print("Ingrese parámetro correcto")     
#         continua2="s"
#         lista=[]
#         while continua2=="s":
#             try:
#                 hora=int(input("Ingrese hora de cita [24h]: "))
#                 nombre=str(input("Ingrese su nombre: "))
#                 lista.append((hora,nombre))
#                 continua2=str(input("Agendar otra cita para el mismo día? [s/n] "))
#             except TypeError:
#                 print("Ingrese parámetro correcto") 
#         diario[dia_semana]=lista
#         continuar1=input("Ingresa otra fecha[s/n] ")
        
#     return diario        

# def imprimir(diario):
#     print("-------------------------")
#     print("Lista completa de citas: ")
#     for fecha in diario:
#         print("Día de la cita:", fecha)
#         for hora,nombre in diario[fecha]:
#             print(f"Nombre: {nombre}")
#             print(f"Hora: {hora}")
    

# def consultar_dia(diario):
#     fecha=str(input("¿Cuál día desea consultar? "))

#     if fecha in diario:
#         for hora,nombre in diario[fecha]:
#             print(f"Nombre: {nombre}.")
#             print(f"Hora: {hora}")
#     else:
#         print("-------------------------")
#         print("No hay citas para ese día")
#         print("---Gracias por consultar---")
        

# diario=organizador()
# imprimir(diario)
# consultar_dia(diario)              

# -------------    
# CINEMA 

print("---CINEMA 24 HORAS---")
print("")

def cine():
    entradas={}
    continuar="s"
    while continuar=="s":
        print("Acción - Misterio - Drama - Musical")
        ingrese_pelicula=str(input("Ingrese un genero de Películas: "))
        print("Lunes - Martes - Miércoles - Jueves - Viernes")
        continua2="s"
        lista=[]
        while continua2=="s":
            dia_pelicula=str(input("Escriba el día: "))
            hora_pelicula=int(input("Ingrese la hora: "))
            lista.append((dia_pelicula,hora_pelicula))
            entradas[ingrese_pelicula]=lista
            continua2=input("¿Desea añadir otra película?[s/n] ")
        continuar=input("¿Desea añadir otro día? ")    
    return entradas    

def imprimir(entradas):
    print("Lista completa de películas: ")
    for dia_pelicula in entradas:
        print(f"Día de la película: ", dia_pelicula )
        for dia_pelicula,hora_pelicula in entradas[dia_pelicula]:
            print(f"Día {dia_pelicula}")
            print(f"hora {hora_pelicula}")

def consultar_dia(entradas):
    ingrese_pelicula=str(input("Ingrese el día de la consulta: "))
    if ingrese_pelicula in entradas:
        for dia_pelicula,hora_pelicula in entradas[ingrese_pelicula]:
            print(f"Día {dia_pelicula}")
            print(f"Hora {hora_pelicula}")
    else:
        print("No hay películas para ese día")    

entradas=cine()  
imprimir(entradas)
consultar_dia(entradas)          















