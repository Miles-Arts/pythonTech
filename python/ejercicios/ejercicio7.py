# Enunciado 
# Realizar un programa que pida al usuario digitar un día de la semana
# * Si es lunes, sábado o domingo imprimir el día de la semana y un mensaje
# * Si es viernes imprima el día de la semana y “Ya vemos cerca el fin de semana”
# De lo contrario imprima “Avancemos que ya es”, día de la semana
# 

dia_semana = str(input("Ingrese un día de la semana: ").lower())


if dia_semana == "viernes":
    print(f"¡Es {dia_semana} ya vemos cerca el fin de semana!")
# elif dia_semana == "jueves" or  dia_semana == "miercoles":
elif dia_semana in ["jueves", "miercoles"]:
    print(f"¡Es {dia_semana} si se puede!")
# elif dia_semana == "lunes" or  dia_semana == "sabado" or  dia_semana == "domingo":
elif dia_semana in ["lunes", "sabado", "domingo"]:
    print(f"Avancemos que ya es {dia_semana}")    
