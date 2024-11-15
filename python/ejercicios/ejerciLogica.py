import math
from math import sin, cos, tan, exp, log
# entrada=str(input("Ingrese la frase: ")).lower()
# frase=entrada.split()
# frases={}

# for palabra in entrada:
#     if palabra in frases:
#         frases[palabra]+=1
#     else:
#         frases[palabra]=1

# print("Palabras Repetidas")

# for clave, valor in frases.items():
#     print(f"{clave} y {valor}")


# Escribir un programa que pregunte el nombre del 
# usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena 
# ¡Hola <nombre>!, donde 
# <nombre> es el nombre que el usuario haya introducido.

# ingrese_nombre=str(input("Hola, Ingresa tu nombre: "))

# print(f"¡Hola {ingrese_nombre}!")


# num1=3
# num2=2
# num3=2
# num4=5
# num5=2

# def operacion():
#     operacion_salida=  ((num1+num2) / (num3*num4)) ** num5
#     print(operacion_salida)


# operacion()




# ingrese_numero=int(input("Ingrese numero entero positivo: "))

# # for numero in range(0,ingrese_numero,1):
# #     numero= numero * (numero + 1) / 2
# #     # numero+=1
# #     print(numero)

# suma = ingrese_numero * (ingrese_numero + 1) / 2

# print(f"La suma de los números enteros desde 1 hasta + {ingrese_numero} es {suma}")


# MASA CORPORAL
# peso=float(input("Ingrese su peso kg: "))
# altura=float(input("Ingrese su altura Mt: "))

# imc= peso / (altura * altura)

# # print(f"Su altura de {altura}")
# # print(f"Su peso de {peso}")
# print(f"Tu índice de masa corporal es {imc:.2f}")

# COCIENTE
# entero0=int(input("Ingrese el primer numero entero: "))
# entero1=int(input("Ingrese el segundo numero entero: "))


# division= entero0 / entero1
# cociente= entero0 % entero1

# print(f"{entero0} entre {entero1} da un cociente {division:.2f} y un resto {cociente}")

# INVERSION DINERO

# dinero_inversion=float(input("Ingrese la cantidad a Invertir: "))
# interes_anual=float(input("Ingrese el interés anual (%): "))
# anios_invertir=int(input("Años a inventir: "))

# for anio in range(1, anios_invertir +1):
#     dinero_inversion *= 1 + (interes_anual / 100)
#     print(f"Año { anio}: Capital acumulado = {round(dinero_inversion, 2)}")

# dinero_invertir=float(input("Ingrese cantidad a invertir: "))
# anual_interes=float(input("Ingrese el interés anual (%): "))
# dinero_anios=int(input("Años a inventir: "))

# for anio in range(1,dinero_anios,1):
#     resultado = (dinero_invertir * (anual_interes / 100 + 1 ) ** dinero_anios)
# print(f"Año {dinero_anios}: Capital acumulado = {round(resultado, 2)}")
  
# PAYASOS Y MUÑECAS

# cantida_payasos=float(input("Ingrese la cantidad de payasos vendidos: "))
# cantida_munecas=float(input("Ingrese la cantidad de muñecas vendidas: "))

# PESO_PAYASO = 112
# PESO_MUNECA = 75

# peso_total_payasos = cantida_payasos * PESO_PAYASO
# peso_total_munecas = cantida_munecas * PESO_MUNECA
# total_ventas = peso_total_payasos+peso_total_munecas

# if peso_total_payasos > 1000:
#     print(f"Peso Total del paquete es de: {total_ventas:.0f} kilos")
# else:
#     print(f"Peso Total del paquete es de: {total_ventas:.0f} gramos")

# PANADERIA - BARRAS PAN


# cantidad_pan_vendido = int(input("Ingrese la cantidad de pan vendido: "))
# UNIDAD_PAN_PRECIO = float(3.49)
# DESCUENTO = 60

# precio_pan_total = cantidad_pan_vendido * UNIDAD_PAN_PRECIO
# descuento_no_dia = float(precio_pan_total * (1- DESCUENTO / 100 ) )
# cantidad_descuento =   precio_pan_total - descuento_no_dia  

# print(f"Precio habitual del pan fresco es: {UNIDAD_PAN_PRECIO}€")
# print(f"Descuento no frescura del {DESCUENTO}%")
# print(f"Valor del descuento: {cantidad_descuento:.2f}€")
# print(f"Costo TOTAL: {descuento_no_dia:.1f}€")

# BUCLE USUARIO
# nombre_usuario=str(input("Ingrese su nombre: "))
# numero_entero=int(input("Ingrese nu numero entero: "))

# for numero in range(numero_entero):
#     print(nombre_usuario)

# NOMBRE USER MAYUSCULAS, MINUSCULAS Title CASE
# nombre_user=str(input("Ingrese su nombre: "))
# nombre_lowe=nombre_user.lower()
# nombre_upercase=nombre_user.upper()
# nombre_title_clase=nombre_user.title()

# print(nombre_lowe)
# print(nombre_upercase)
# print(nombre_title_clase)

# NOMBRE CANTIDAD LETRAS Y MAYUSCULA

# nombre_user=str(input("Ingrese nombre: ")).upper()

# nombre=len(nombre_user)
# print(f"Nombre: {nombre_user} tiene {nombre} letras")

# n=10
# print("Juan\n"*int(n))


# NÚMERO PREFIJO EMPRESA
# prefijo numero extención
# +34-913724710-56
# numero=(input("Ingrese un numero con su prefijo-número-extención: "))

# print(f"Número sin prefijo y sin extención: {numero[4:-3]}")


# LETRAS INVERTIDAS
# ingrese_frase=input("Ingrese una frase: ")
# print(ingrese_frase[::-1]["o"])


# VOCAL MAYUSCULA

# frase=str(input("Escriba una frase: "))
# vocal=str(input("Escriba una vocal: "))
# call="M"

# print(frase.replace(vocal, call.upper()))
# # print(frase.replace(vocal, vocal.upper()))


# EMAIL DOMINiO

# ingrese_email=input("Ingrese su email: ")
# domini="ceu.es"
# arroba="@"
# print(ingrese_email.replace(arroba, domini))

# ingrese_email=input("Ingrese su email: ")
# # print(ingrese_email[:ingrese_email.find('@')] + "@ceo.es")

# print(ingrese_email[:ingrese_email.find("@")] + "@que_loco_de_email.com")

# ingrese_email=input("Ingrese su email: ")
# print(ingrese_email[:ingrese_email.find("@")] + "@hola_gente.caspa.com")

# PRODUCTO EURO DECIMALES CENTIMOS.


# precio=input("Ingrese precio en euros: ")
# # print(f"{precio}€")

# print(precio[:precio.find(".")] , "euros y" , precio[precio.find(".")+1:], "centimos.") 

# precio=input("Ingrese precio: ")

# print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:]  ,"centimos" )


# INGRESE dd/mm/aaaa
# fecha=input("Ingrese su fecha de nacimiento dd/mm/aaaa : ")

# print(fecha[:fecha.find("/")],fecha[fecha.find("/0")+1:])

# 12/23/1234
# print("Día:",   fecha[:2])
# print("Mes:",   fecha[3:5])
# print("Año:",   fecha[6:])

# dia=fecha[:fecha.find("/")]
# mesaño = fecha[fecha.find("/")+1:]
# mes = mesaño[:mesaño.find("/")]
# año = mesaño[mesaño.find("/")+1:]

# print("Día", dia)
# print("Mes", mes)
# print("Año", año)


# Productos separados
# lista_productos=input("Ingrese lista produtos compra: ")

# listas=lista_productos.split(",")

# for lista in listas:
#     print(lista)
#     # print("\n",lista_productos,"\n")
# #     # print(lista)

# productos_lista=input("Ingrese lista productos, después (,) ")

# productos=productos_lista.split()

# for lista in productos:
#     print(lista)

# productos=input("Añada lista después (,): ")

# # lista=",".join(productos)
# print("\n".join(productos.split(",")))


# compras=input("Ingrese productos (,)")

# lista=compras.replace(",", "\n")

# print(lista)


# Productos USUARIO

# nombre_producto=input("Ingrese el nombre producto: ")
# precio_producto=float(input("Ingrese el precio producto: "))
# unidades_producto=int(input("Ingrese el número unidades producto: "))

# total_valor=precio_producto*unidades_producto

# # print(nombre_producto, precio_producto, unidades_producto, total_valor)
# print(f'{nombre_producto}: {unidades_producto:3d} unidades x {precio_producto:11.2f}€ = {total_valor:9.2f}€'.format(nombre_producto = nombre_producto, unidades_producto = unidades_producto, precio_producto = precio_producto, total_valor = total_valor))

# nombre=input("Nombre: ")
# edad=input("Edad: ")

# salida= "My name is {nombre}, I'm {edad}".format(nombre = nombre, edad = edad)
# salida1= "My name is {0}, I'm {1}".format(nombre, edad)
# salida2= "My name is {}, I'm {} ".format(nombre,edad)

# print(salida)
# print(salida1)
# print(salida2)

# MAYOR EDAD

# edad=int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Es mayor de edad.")
# else:
#     print("Es menor de edad.")    

# CONTRASEÑA

# password=input("Ingrese contraseña: ").lower()

# password_new=input("Introduca nuevamente su contraseña: ")

# if password == password_new:
#     print("Contraseña correcta")
# else:
#     print("Contraseña errónea")    


# DIVIISON EN CERO

# num1=float(input("Introduzca primer número: "))
# num2=float(input("Introduzca segundo número: "))

# division = float(num1 / num2)

# if division == 0:
#     print("¡Error! No se puede dividir por 0.")

# else:
#     print(f"Resultado: {division}")


# PAR E IMPAR

# num_par=float(input("Ingrese un numero: "))

# if num_par % 2 == 0:
#     print(f"El numero {num_par} es par")
# else:
#     print(f"El numero {num_par} es impar")    


# entero=int(input("Ingrese numero entero: "))

# if entero % 2 == 0:
#     print(f"Es número {entero} par.")
# else:
#     print(f"Es número {entero} impar.")    


# TRUBITAR IMPUESTO

# edad=int(input("Ingrese edad: "))
# ingresos=float(input("Ingresos mensuales: "))

# if edad >= 18 and ingresos >= 1000:
#     print("Tiene que tributar")
# else:
#     print("No tiene que tributar")    

# ALUMNOS COLEGIO

# nombre=str(input("Ingrese su numbre: ")).lower()
# sexo=str(input("Ingres su sexo: ")).lower()

# if sexo == "mujer" and  nombre[0] in ["a","b","c","d","e","f","g","h","i","j", "k","l"] :
#     print("Grupo A ")
# elif sexo == "hombre" and  nombre[0] in ["o","p","q","r","s", "t", "u","w", "x","y","z" ]:    
#     print("Grupo A")
# else: 
#     print("Grupo B")

# if letra <= "d":
#     print("letra entre abcd")
# elif letra >= "e":
#     print("Letras despues de la e hasta la z")

# nombre=input("Ingrese Nombre: ")
# sexo=input("Ingrese sexo: (M/H): ")
# grupo=""

# if sexo.lower() == "m":
#     if nombre.lower() < "m":
#        grupo = "A"
#     else:
#        grupo = "B"

# if sexo.lower() == "h":
#     if nombre.lower() > "n":
#        grupo = "A"    
#     else:
#        grupo = "B"   
# print(f"Tu grupo es: {grupo}")               


# nombre=input("Ingrese Nombre: ")
# sexo=input("Ingrese sexo: (M/H): ")
# sexo=sexo.upper()
# grupo=""

# if sexo == "M":
#     if nombre.lower() < "m":
#        grupo = "A"
#     else:
#        grupo = "B"
# else:
#     if nombre.lower() > "n":
#        grupo = "A"    
#     else:
#        grupo = "B"   
# print(f"Tu grupo es: {grupo}")     


# TRAMOS IMPOSITIVOS

# renta=float(input("Ingrese su renta anual: ")) 

# if renta < 10000:
#     print("Tipo impositivo del 5%")
# elif renta >= 10000 and renta < 20000:
#     print("Tipo impositivo del 15%")    
# elif renta >= 20000 and renta < 35000:
#     print("Tipo impositivo del 20%") 
# elif renta >= 35000 and renta < 60000:
#     print("Tipo impositivo del 30%")
# else:
#     print("Tipo impositivo del 45%")          

# renta=float(input("¿Cuál es tu renta anual? "))

# if renta < 10000:
#     tipo = 5
# elif renta < 20000:
#     tipo = 15
# elif renta < 35000:
#     tipo = 20
# elif renta < 60000:
#     tipo = 30
# else: 
#     tipo = 45

# print(f"tienes que pagar. {renta * tipo / 100}€")                    

# Puntuación empresa


# puntos=float(input("Ingrese los puntos obtenidos: "))
# bono= float(2400)
# inaceptable = float(0)
# aceptable = float(0.4)
# meritorio = float(0.6)


# if puntos == inaceptable:
#     nivel = "Inaceptable"
# elif puntos == aceptable:
#     nivel = "Aceptable"
# elif puntos >= meritorio:
#     nivel = "Meritorio"
# else:
#     nivel = ""

# if nivel == "":
#     print("Esta puntuaciónno no es válida.")
# else:
#     print("Tu nivel de rendimiento es %s" % nivel)    
#     print("Te correponde cobrar %.2f€" % (puntos * bono))


# JUEGOS FAMILIA

# edad=int(input("Ingrese la edad del usuario: "))

# if edad == 4:
#     # print("Menos de 4 años, entra gratis.")
#     precio = 0
# elif edad > 4 and edad < 18:
#     # print(f"Edad: {edad}. Debe pagar 5€.")
#     precio = 5
# elif edad >= 18:
#     # print(f"Mayor de 18 años debe pagar 10€.")
#     precio = 10

# print(f"El precio de la entrada es {precio}€")    


# PIZZERIA 

# tipo_pizza=input("¿Desea pizza vegetariana? (SI/NO) ").lower()


# if tipo_pizza.lower() == "no":
#     print("\nSolo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.")
#     ingredientes=input("\nIngredientes no vegetarianos: \n\tPeperoni. \n\tJamón. \n\tSalmón. \nIngrese 1 ingrediente extra: ")
    
#     if ingredientes.lower() == "peperoni":
#         print(f"Pizza No vegetariana de mozzarela y tomate con {ingredientes}")
#     elif ingredientes.lower() == ingredientes in ["Jamón", "Jamon", "jamon"]:
#         print(f"Pizza No vegetariana de mozzarela y tomate con {ingredientes}")
#     elif ingredientes.lower() == ingredientes in ["Salmón", "Salmon", "salmon"]:
#         print(f"Pizza No vegetariana de mozzarela y tomate con {ingredientes}")
#     else:
#         print("Valor no válido: ")    


# elif tipo_pizza.lower() == "si":
#     print("\nSolo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.")
#     ingredientes=input("\nIngredientes vegetarianos: \n\tPimiento \n\tTofu. \nIngrese 1 ingrediente extra: ")
#     if ingredientes.lower() == ingredientes in ["Pimiento", "pimiento"]:
#         print(f"Pizza de mozzarela y tomate con {ingredientes}")
#     elif ingredientes.lower() == ingredientes in ["Tofu", "tofu"]:
#         print(f"Pizza Vegetariana de mozzarela y tomate con {ingredientes}")   
#     else:
#          print("Valor no válido: ")  
# else:
#     print("Ingrese una respuesta correcta")


# BUCLES
# BUCLE PALABRA
# palabras=input("Ingrese una palabra: ")

# for palabra in range(10):
#     # palabra +=1
#     print(palabra, palabras)

# EDAD USUARIO

# ingrese_edad=int(input("Ingrese su edad: "))

# for i in range(0,ingrese_edad,1):
#     i+=1
#     # print(f"Años cumplidos: {i}")
#     print(f"Has cumplido {i} años")



# enerots y print impares

# num_entero=int(input("Ingrese un números entero positivo: "))

# for i in range(1,num_entero+1,2):

#     print(i, end=", ")

# ENTERO POSITIVO HACIA ATRÁS

# numero=int(input("Ingrese un número entero positivo: "))

# for i in range(numero,-1,-1):

#     print(i, end=", ")

# INVERSION

# dinero_invertir=float(input("Ingrese cantidad a invertir: "))
# anual_interes=float(input("Ingrese el interés anual (%): "))
# dinero_anios=int(input("Años a inventir: "))

# for anio in range(1,dinero_anios,1):
#     resultado = (dinero_invertir * (anual_interes / 100 + 1 ) ** dinero_anios)
# print(f"Año {dinero_anios}: Capital acumulado = {round(resultado, 2)}")

# inversion=float(input("Ingrese cantidad a invertir: "))
# interes_anual=float(input("Ingrese interés anual: "))
# anios_inversion=int(input("Años de inversion: "))

# for anio in range(1,anios_inversion+1,1):
#     resultado = (inversion * ( interes_anual / 100 + 1) ** inversion)
#     # print(resultado)
#     # # resultado += resultado
#     # print(f"\n\tInversión del año: {anio}")
#     # print(f"\tTotal { round(resultado, 2) }")

# print("------------------------------------------------------------------")    

# inversion=float(input("Ingrese cantidad a invertir: "))
# interes_anual=float(input("Ingrese interés anual: "))
# anios_inversion=int(input("Años de inversion: "))

# for i in range(anios_inversion):
#     inversion *=1 + interes_anual / 100
#     print(f"Capital tras {i+1} Año: {round(inversion, 2)} ")


# TRIANGULO

# numero=int(input("Ingrese un número entero: "))

# for i in range(1,numero):
#     # 
#     print("*")
#     # i+=1
#     for j in range(i):
#         # j+=1
#         print(end="* ")
#  BLUCES       # 
# numero=int(input("Ingrese un número entero: "))

# for i in range(numero):
#     for j in range(i+1):
#         casa=0
#         print("*", end=" ")
#     print("")    



# tabla multiplizar

# numero = 1
# fin = 11
# tabla=1
# salto=0

# for tabla in range(1,fin,1):
    

#     resultado= tabla * numero
    
#     tabla = tabla + salto

#     for num in range(1,fin,1):

#         print(f"{tabla} x {numero} = {resultado}")
        

#     # for tabla in range(1,fin,1):
#     #     # tabla+=1
#     #     # numero+=1
#     #     print(f"{tabla} x {numero} = {resultado}")

# MULTIPLIZAR

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print(" ")    

# numero=int(input("Ingrese número: "))

# for i in range(1,numero+1,2):
    
#     for j in range(i,0,-2):
#         # numero+=1
#         print(j, end=" ")
#     print()


# numero=int(input("Ingrese numero: "))

# for i in range(1, numero+1,2):
#     for j in range(i,0,-2):
#         print(j, end=" ")
#     print()    

#CONTRASEÑA  

# contrasena=input("Introduce una contraseña: ")

# while True:
#     contrasena_new=input("Ingrese nuevamente la contraseña: ")
#     if contrasena_new != contrasena:
#         print("\ncontraseña incorrecta!\n")
#     elif contrasena == contrasena:
#         print("\nContraseña Correcta!\n")
#         break

# key="contraseña"  
# password=""
# while  password != key:
#     password=input("Introduce la contraseña: ")
# print("Contraseña correcta")       

# NUMEROS PRIMOS

# numero=int(input("Introduce un numero entero: "))

# while  numero % 2 == 0:
       
#         print("No es primo")   
#         break
# else:
#      print("Es número primo")
   
# numero=int(input("Introduce núemros primso positivo mayor a 2: "))
# i = 2

# while numero % i != 0:
#     # print(i)
#     i+=1
# if i == numero:
#     print(str(numero) + " es primo.")
# else:
#     print(str(numero) + " no es primo.")        

# numero=int(input("Introduce núemros primso positivo mayor a 2: "))

# for i in range(2, numero):
#     if numero % i == 0:
#         break
# if (i + 1) == numero:
#     print(str(numero) + " es primo.")
# else:
#     print(str(numero) + " no es primo.")       

# Impresion letras desde atrás

# palabra=input("Ingrese palabra: ")

# for letras in palabra:
#         # print(letras)
#         for letra in range(letras, -1,-1):    
#             print(letra)

# palabra=input("Ingrese la palabra: ")

# for i  in range(len(palabra)-1,-1,-1):
#     print(palabra[i])

# frases letras

# frase=input("Ingrese una frase: ").split(",")
# letra=input("Ingrese una letra: ")

# for i in frase:
#     if letra == len(frase):
#         print(letra)
#     else:
#         print("No")    
   

# frase=input("Introduce frase: ")
# letra=input("Introduce letra: ")
# contador=0

# for  i in frase:
#     if i == letra:
#         contador+=1
# print(letra,contador,frase)    

# frase=input("Frase: ")
# letra=input("Letra: ")
# contador=0

# for i in frase:
#     if i == letra:
#         contador+=1
# print(f"Hay {contador} letras {letra} en {frase}")        

# eco=input("Introduce palabra: ")
# terminar="salir"
# bucle= 100

# while True:
    # for i in range(0,200):
# while 1 > 0:
#     salir=input("escribe [ salir ] : ")
#     while True:    
#         if 1 > 10:
#             print(eco)
#             print("escribe [ salir ] : ")
            
#         elif salir.lower() == terminar:
#             print("--fin--")
#             break       
#         else:    
#             print("escribe [ salir ] : ")

# while True:
#     frase=input("Introduce algo: ")
#     if frase == "salir":
#         break
#     print(frase)    

# LISTAS

# lista=input("Ingrese cada materias separadas con ( , ): ").split(",")
# materias=[]
# materias.append(lista)

# print(materias)

# materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# print(materias)

# Impresión de listas



# materias=input("Ingrse materias: ")

# listas_materias=[]
# listas_materias.append(materias)

# print(f"Yo estudio {listas_materias }")

# listas_materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for materias in listas_materias:
#     print(f"Yo estudio {materias}.")

# materias=input("Ingrese materias: ").split(", ")
# notas=input("Ingrese notas: ").split(", ")

# materias_lista=[]
# notas_listas=[]

# materias_lista.append(materias)
# notas_listas.append(notas)

# for materia in materias_lista:
#     for nota in notas_listas:
#         print(f"En {materia} has sacado la nota {nota}")


# materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas=[]

# for materia in materias:
#     nota=input(f"Que nota has sacado en {materia }:")
#     notas.append(nota)
# for i in range(len(materias)):
#     print(f"En {materias[i]} has  sacado {notas[i]}")    


# materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas=[]

# for materia in materias:
#     nota=input(f"Ingrese la nota de {materia}: ")
#     notas.append(nota)
# for i in range(len(materias)):
#     print(f"En {materias[i]} has sacdo la nota {notas[i]}")

# materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas=[]

# for materia in materias:
#     nota=input(f"Ingrese la nota de la materia {materia}: ")
#     notas.append(nota)
# for i in range(len(materias)):
#     print(f"En la materia {materias[i]} has scaado la nota {notas[i]}")    

# meses=["Enero", "Febrero", "Marzo", "Abril"]
# ventas=[]

# for mes in meses:
#     venta=input(f"Ingrese el total de ventas del mes {mes}: ")
#     ventas.append(venta)
# for i in range(len(ventas)):
#     print(f"Lan ventas del mes {meses[i]} fueron de ${ventas[i]}")    

# ventas=[300,400,500,234,333]
# meses=[]

# for venta in ventas:
#     mes=input(f"Ingrese mes de la siguiente venta {venta}: ")
#     meses.append(mes)
# for i in range(len(ventas)):
#     print(f"Las ventas {ventas[i]} son del mes {meses[i]}")    

# Numeros loteria

# numeros_loteria=input("Ingrese los numeros de loteria primitiva: ")
# numeros_lista=[]

# numeros_lista.append(numeros_loteria)

# for i in numeros_loteria:
#     # len(min(numero))
#     print(len(min(numeros_loteria)))

# numeros_loteria=[]

# for i in range(6):
#     # numeros_loteria.append(int(input("Introduce un número ganador: "))) 
# # numeros_loteria.sort()
# print(f"Los números ganadores son {numeros_loteria}")

# Numero inverso

# numericos=input("Ingrese numeros del 1 al 10, separados con comas (,) ").split(", ")

# numerico=[]
# numericos=(int(input("Ingrese numeros del 1 al 10, separados con comas (,) ").split()))
# numerico.append(numericos)
# numerico.sort()
# print(f"Lo numeros en orden son: {numerico} ")    

# numeros=[1,2,3,4,5,6,7,8.9,10]
# numeros.reverse()
# for numero in numeros:
#     print(numero, end=("* "))

# numericos=[1,2,3,4,5,6,7,8,9,10]
# for i in range(1,11):
#     print(numericos[-i], end=(", "))



# num=[500,323,2,67878,654,29,1,454,45567,87665,23,]
# for i in range(1,11):
#     print(num[-i], end=(", "))


# MATERIAS APROVADAS


# materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas=[]
# for materia in materias:
#     nota=int(input(f"Ingrese la nota ( 0-5 )de la materia {materia}: "))
#     notas.append(nota)
# for i in range(len(materias)):
#     if i >= 0 and i <= 3:
#         print(f"Ha perdido la materia {materias[i]} con la nota {notas[i]}")
#     else:
#         print("Ingrese nota correcta")    
#     # print(f"materia {materias[i]} and notas: {notas[i]}")
    
# materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas_aprobadas=[]
# for materia in materias:
#     nota=float(input(f"¿Qué nota sacaste en {materia}: "))
#     if nota >= 5:
#         notas_aprobadas.append(materia)
# for materia in notas_aprobadas:
#         materias.remove(materia)
# print("Tiene que repetir ", str(materias)) 
         
# materias_aprobadas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas_excelentes=[]

# for materia_lista in materias_aprobadas:
#      nota=float(input(f"¿Qué nota sacaste en {materia_lista}: "))
#      if nota >= 7:
#           notas_excelentes.append(materia_lista)
# for materia_lista in notas_excelentes:
#      materias_aprobadas.remove(materia_lista)
# print(f"Tiene que repetir {materias_aprobadas} ")    

# productos_personales=["Jabón","Champoo","Crema piel", "Acondicionador", "Perfume"]
# ventas_totales=[]

# for producto in productos_personales:
#      ventas=float(input(f"¿cuanto vendiste por mes para el siguiente producto? {producto}: "))
#      if ventas >= 50:
#           ventas_totales.append(producto)
# for product in ventas_totales:
#      productos_personales.remove(product)    
# print(f"Metas de ventas no logradas de los productos: {productos_personales}")           

# repuestos=["Llantas", "Tapa Gasolina", "Vidrio Panorámico", "Bomper Trasero", "Luces Delanteras"]
# cantidad_stock=[]

# for respuesto in repuestos:
#     cantidad=int(input(f"Ingrese ecantidad de stock para cada respuesto de {respuesto} "))
#     if cantidad >= 50:
#         cantidad_stock.append(respuesto)
# for stock in cantidad_stock:
#     repuestos.remove(stock)
# print(f"Queda isuficente de stock de {repuestos}.")    

# sabores_helado=["Chocolate", "Vainilla", "Arequipe", "Fresa", "Melocotón"]
# litros_helado=[]

# for sabores in sabores_helado:
#     litros=float(input(f"Ingrese la cantidad de litros disponibles de {sabores}: "))
#     if litros >= 50:
#         litros_helado.append(sabores)
# for litro in litros_helado:
#     sabores_helado.remove(litro)
# print(f"Actualizar pedido de helado para los sabores de {sabores_helado}")    

# prendas_ropa=["Pantalón", "Chaleco","Camiseta", "Pantaloneta", "Medias"]
# cantidad_prendas=[]

# for prendas in prendas_ropa:
#     cantidad=int(input(f"Ingrese la cantidad de prendas en bodega de {prendas}: "))
#     if cantidad >= 50:
#         cantidad_prendas.append(prendas)
# for total in cantidad_prendas:        
#     prendas_ropa.remove(total)
# print(f"Falta de stock en bodega de {prendas_ropa}")    

# ABCEDARIO LISTA



# abcedario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# numeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26]
# posicion=[]


# for abc in abcedario:
#     numero = float(numeros % 2 != 0)
#     if round(numero) != 0:
#         posicion.append(numero)
# for abc in abcedario:
#     abcedario.remove(posicion)
# print(abcedario)            
        
# abcedario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# for i in range(len(abcedario), 1,-1):
#     if i % 3 == 0:
#         abcedario.pop(i-1)
# print(abcedario)        

# letras=["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# for i in range(len(letras),1,-1):
#     if i % 3 == 0:
#         letras.pop(i-1)
# print(f"letras {letras}")        

# elementos=["Mesa", "Radio", "Libreta", "Silla"]
# for i in range(len(elementos),1,-1):
#     if i % 3==0:
#         elementos.pop(i-1)
# print(elementos)    

# dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo", "Lunes", "Martes"]

# for i in range(len(dias),1,-1):
#     if i % 3 == 0:
#         dias.pop(i-1)
# print(dias)        

# sabores=["Chocolate", "Fresa", "Mora","Melocotón", "Vainilla", "Frutos Rojos", "Mango"]

# for i in range(len(sabores), 1,-1):
#     if i % 3 == 0:
#         sabores.pop(i-1)
# print(sabores)        

# palindromo


# letra=input("Ingrese una palabra: ").split(", ")
# letra=input("Ingrese una palabra: ")
# palindromo=[]
# palindromo.append(letra)
# for i in range(len(palindromo),1,-1):
#     if i == letra:
#           print("Palindromo")
#     else:
#           print("No palindromo")
# else:
#     print("Error")            

# palabra=input("Introduce palabra: ").lower()
# reves_palabra = palabra
# palabra=list(palabra)
# reves_palabra=list(reves_palabra)
# reves_palabra.reverse()
# if palabra == reves_palabra:
#     print("Es Palíndromo")
# else:
#     print("No es Palíndromo")    

# palabra=input("Ingrese palabra: ").lower()
# reves_palabra=palabra
# palabra=list(palabra)
# reves_palabra=list(reves_palabra)
# reves_palabra.reverse()
# if palabra == reves_palabra:
#     print(f"Palíndromo {palabra} revés {reves_palabra}")
# else:
#     print(f"No Palíndromo {palabra} revés {reves_palabra}")    

# palabra=input("Ingrese palabra: ")
# palabra=list(palabra)

# for i in range(len(palabra)):
#     if i == palabra:
#         i+1
#         print(palabra.pop(i-1)) 
# # print(i)


# palabra=input("Introduce palabra: ").lower()
# vocales=["a","e","i","o","u"]

# for vocal in vocales:
#     veces = 0
#     for letra in palabra:
#         if letra == vocal:
#             veces+=1
#     print(f"La vocal {vocal} aparece {veces} veces")



# palabra=input("Introduce palabra: ").lower()
# vocales=["a","e","i","o","u"]

# for vocal in vocales:
#     veces=0
#     for letra in palabra:
#         if vocal == letra:
#             veces+=1
#     print(f"La vocal {vocal} esta {veces} veces")          

# palabras=(input("Introduce una frase: "))
# letras=["a", "b", "c","ch", "d", "e", "f", "g", "h", "i", "j", "k", "l","ll", "m", "n", "ñ", "o", "p", "q", "r","rr", "s", "t", "u","ü", "v", "w", "x", "y", "z"]


# for letra in letras:
#     veces=0
#     for palabra in palabras:
#         if letra == palabra:
#             veces+=1
#     print(f"La letra {letra} esta {veces} veces")        


# palabras=input("Introduce una frase: ").lower()
# letra=input("Introduce letras con (,) al final c/u: ").split(",")
# letras=[]
# letras.append(letra)

# for letraz in letras:
#     veces=0
#     for palabra in palabras:
#         if palabra == letraz:
#             veces+=1
#     print(f"Las letras {letraz} estan {veces} veces")        


# numeros=[]
# numericos=int(input("Introduce 6 números: "))
# numeros.append(numericos)
# enteros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

# for numero in numeros:
#     veces=0
#     for entero in enteros:
#         if numero == entero:
#             veces+=1
#     print(f"Los número {numero} estan {veces} veces ")        


# numeros=input("Introduce 6 números: ")
# enteros=["0","1","2","3","4","5","6","7","8","9"]

# for entero in enteros:
#     veces=0
#     for numero in numeros:
#         if numero == entero:
#             veces+=1
#     print(f"Los números {entero} estan {veces} veces ")        


# palabras=input("Ingrese palabras: ").split(" ")
# con_censura=["malo","violencia","negativo"]

# for censura in con_censura:
#     veces=0
#     for palabra in palabras:
#         if palabra == censura:
#             veces+=1
#     print(f"La palabra {censura} esta {veces} veces")        

#  PRECIOS PRODUCTOS MENOR Y MAYOR

# precios=[50,75,46,22,80,65,8]

# precios_min=min(precios)
# precios_max=max(precios)

# print(f"El valor máximo es: {precios_max}")
# print(f"El valor mínimo es: {precios_min}")


# precios=[50,75,46,22,80,65,8]

# min = max = precios[0]
# for precio in precios:
#     if precio < min:
#         min = precio
#     elif precio > max:
#         max = precio
# print(f"El mínimo es {min}")            
# print(f"El máximo es {max}")            

# inventarios=[2,50,75,46,22,80,65,8,500,10,4,900,1]
# min = max = inventarios[0]

# for inventario in inventarios:
#     if  inventario < min:
#         min = inventario
#     elif  inventario > max:
#         max = inventario        
# print(f"Stock Mínimo {min}")
# print(f"Stock Máximo {max}")

# inventarios = [2, 50, 75, 46, 22, 80, 65, 8, 500, 10, 4, 900, 1]
# stock_minimo = min(inventarios)
# stock_maximo = max(inventarios)
# print(f"Stock Mínimo {stock_minimo}")
# print(f"Stock Máximo {stock_maximo}")



# inventarios = [2, 50, 75, 46, 22, 80, 65, 8, 500, 10, 4, 900, 1]
# stock_minimo = min(inventarios)
# stock_maximo = max(inventarios)
# print(f"Stock Mínimo {stock_minimo}")
# print(f"Stock Máximo {stock_maximo}")



# edades=[30,50,30,40,19,90]
# min = max = edades[0]

# for edad in edades:
#     if edad < min:
#         min = edad
#     elif edad > max:
#         max = edad
# print(f"Edad menos {min}")            
# print(f"Edad mayor {max}")            

# letras=["a", "b", "c","ch", "d", "e", "f", "g", "h", "i", "j", "k", "l","ll", "m", "n", "ñ", "o", "p", "q", "r","rr", "s", "t", "u","ü", "v", "w", "x", "y", "z"]
# min = max = letras[0]

# for letra in letras:
#     if letra < min:
#         min = letra
#     elif letra > max:
#         max = letra 

# print(f"{min}")        
# print(f"{max}")        
# palabras=["Mesa", "Días", "hola", "sol", "Maestría", "Píngüno","Esternocleidomastoideo", "Zebra", "Wyz"]
# min = max = palabras[0]

# for palabra in palabras:
#     if palabra < min:
#         min = palabra
#     elif palabra > max:
#         max = palabra
# print(f"{min}")        
# print(f"{max}")        

# vocales=["a","e","i","o","u","á","é","í","ó","ú", "ü"]

# min = max = vocales[0]

# for vocal in vocales:
#     if vocal < min:
#         min = vocal
#     elif vocal > max:
#         max = vocal
# print(f"{min}")        
# print(f"{max}")  




# vocales=["a","e","i","o","u"]
# min = max = vocales[0]

# for vocal in vocales:
#     if vocal < min:
#         min = vocal
#     elif vocal > max:
#         max = vocal
# print(f"{min}")        
# print(f"{max}")        

# vocales=[30,60,40,60]
# min = max = vocales[0]

# for vocal in vocales:
#     if vocal < min:
#         min = vocal
#     elif vocal > max:
#         max = vocal
# print(f"Precio menor ${min} USD")        
# print(f"Precio mayor ${max} USD")   


# vector1=[1,2,3]
# vector2=[-1,0,2]

# vector3 = vector1 + vector2
# vector1.append(vector2)

# print(vector3)
# print(vector1)

# lista1 = (1,2,3)
# lista2 = (-1,0,2)

# producto=0
# for i in range(len(lista1)):
#     producto += lista1[i]*lista2[i]
# print(f"El producto de los vestores {lista1} y {lista2} es: {producto}")    
# # MULTIPLIZAR  UN NÚMERO positivo con uno NEGATIVO SIEMPRE EL RESULTADO ES NEGATIVO

# num = (1) * (-1) 
# print(num)

# lista1=(3,4,5,)
# lista2=(-3,4,5,)

# resultado=0

# for i in range(len(lista1)):
#     resultado += lista1[i] * lista2[i]
# print(f"El resultado de tupla 1 {lista1} y tupla 2{lista2} es: {resultado}")    

# # Mulitiplzai precios

# precios_semana1 = (10, 20, 30, 40 )
# precios_semana2 = (10, 20, 30, 40 )

# total_semanas=0

# for i in range(len(precios_semana1)):
#     total_semanas += precios_semana1[i] * precios_semana2[i]
# print(f"Semana 1 {precios_semana1 } Semana 2. \n\tTotal: {total_semanas}")    



# clientes_nuevos1=(1,3,4,5)
# clientes_nuevos2=(1,3,4,5)
# # clientes_nuevosx=(1,3,4,5)
# # clientes_nuevos2=(1,3,4,5)

# total_clientes=0

# for i in range(len(clientes_nuevos1)):
#     total_clientes += clientes_nuevos1[i] + clientes_nuevos2[i]
# print(f"Clientes 1 {clientes_nuevos1} Clientes 2 {clientes_nuevos2} Total clientes {total_clientes}")    


# ventas_semana1=(10,20,30,40)
# ventas_semana2=(10,20,30,40)
# total_ventas=0

# for i in range(len(ventas_semana1)):
#     total_ventas += ventas_semana1[i] + ventas_semana2[i]
# print(f"Ventas mes Enero {ventas_semana1} ventas mes Febrero {ventas_semana2} Total ventas {total_ventas}")    


# Matrices 

# lista_1=[(1,2,3),(4,5,6)]
# lista_2=((-1,0),(0,1),(1,1))

# # for i in lista_1:
# #     for j in lista_2:
# #         print(i,j)

# lista_1.append(lista_2)
# # print(lista_1)

# for i in range(len(lista_1)):
#     print(lista_1[i])


# print(lista_1 , lista_2)


# lista_1=((1,2,3),
#          (4,5,6))
# lista_2=((-1,0),
#         (0,1),
#         (1,1))
# resultado=[[0,0],
#            [0,0]]
# for i in range(len(lista_1)):
#     for j in range(len(lista_2[0])):
#         for k in range(len(lista_2)):
#             resultado[i][j] += lista_1[i][k] * lista_2[k][j]
#             print(resultado)
# for i in range(len(resultado)):
#     resultado[i] = tuple(resultado[i])
# resultado = tuple(resultado)
# for i in range(len(resultado)):
#     print(resultado[i])    

# ----------------

# lista_1=((1,2,3),
#          (4,5,6))
# lista_2=((-1,0),
#         (0,1),
#         (1,1))
# resultado=[[0,0],
#            [0,0]]

# for i in range(len(lista_1)):
#     for j in range(len(lista_2[0])):
#         for k in range(len(lista_2)):
#             resultado[i][j] += lista_1[i][k] * lista_2[k][j]
# for i in range(len(resultado)):
#     resultado[i] = tuple(resultado[i])      
# resultado = tuple(resultado)
# for i in range(len(resultado)):
#     print(resultado)          

# tupla1=((1,2,3),
#         (4,5,6))
# tupla2=((-1,0),
#         (0,1),
#         (1,1))
# resultado=[[0,0],
#            [0,0]]

# for i in range(len(tupla1)):
#     for j in range(len(tupla2[0])):
#         for k in range(len(tupla2)):
#             resultado[i][j] +=  tupla1[i][k] * tupla2[k][j]
# for i in range(len(resultado)):
#     resultado[i]= tuple(resultado[i]) 
# resultado= tuple(resultado)
# for i in range(len(resultado)):
#     print(resultado[i])    

# tupla1=((1,2,3),
#         (4,5,6))
# tupla2=((-1,0),
#          (0,1),
#          (1,1))
# resultado=[[0,0],
#            [0,0]]

# for i in range(len(tupla1)):
#     for j in range(len(tupla2[0])):
#         for k in range(len(tupla2)):
#             resultado[i][j] += tupla1[i][k]  * tupla2[k][j]
# for i in range(len(resultado)):
#     resultado[i] = tuple(resultado[i])
# resultado = tuple(resultado)
# for i in range(len(resultado)):
#     print(resultado[i])                


# tupla1=((1,2,3),
#         (4,5,6))
# tupla2=((-1,0),
#         (0,1),
#         (1,1))
# resultado=[[0,0],
#            [0,0]]

# for i in range(len(tupla1)):
#     for j in range(len(tupla2[0])):
#         for k in range(len(tupla2)):
#             resultado[i][j] += tupla1[i][k] * tupla2[k][j]
# for i in range(len(resultado)):
#     resultado[i] = tuple(resultado[i])
# resultado = tuple(resultado)
# for i in range(len(resultado)):
#     print(resultado[i])           


# numero separados comas

# muestra_numeros=float(input("Ingrese una lista de nuemros separados por (,) "))
# muestra_numeros=input("Ingrese una lista de nuemros separados por (,) ")
# muestra_numeros = muestra_numeros.split(',')
# muestra_lista=[]
# muestra_lista.append(muestra_numeros)

# for i  in range(len(muestra_lista)):
#     promedio = len(muestra_lista)
#     resultado = (promedio / muestra_lista) 
#     print(resultado)





# numeros_list=input("Ingrese una muestra de números separados por comas (,) : ")
# numeros_list= numeros_list.split(',')
# numero = len(numeros_list)
# for i  in range(numero):
#     numeros_list[i] = int(numeros_list[i])
# numeros_list = tuple(numeros_list)
# sum=0
# sumsq=0
# for i in numeros_list:
#     sum  += i
#     sumsq += i **2
# promedio = sum/numero
# desviacion=(sumsq/numero-promedio**2)**(1/2)
# print(f"La media es: {promedio} y la desviación es: {desviacion}")      


# numeras_lista=["1.0","2.0","3.0","4.0","5.0"]
# numeras_listas=["1.0","2.0","3.0","4.0","5.0"]
# numeras = len(numeras_lista)

# for i in range(numeras,):
#     numeras_listas[i] = int(numeras_listas[i])
#     numeras_lista[i] = float(numeras_lista[i])
# print(numeras_lista,numeras_listas)

# lista_num=["2","4","6","7","90","3","9",]
# lista_total=len(lista_num)

# for i in range(lista_total):
#     lista_num[i] = int(lista_num[i])
#     print(lista_num)    
# print(lista_num)    




# lista_num=["2","4","6","7","90","3","9",]
# lista_len=len(lista_num)

# for i in range(lista_len):
#     lista_num[i] = float(lista_num[i])
# print(lista_num)    

# lista_num=["2","43","6","7","90","31"]

# len_lista=len(lista_num)

# for i in range(len_lista):
#     lista_num[i] = int(lista_num[i])
# print(lista_num)    


# DICCIONARIOS


# moneda={"Euro":"€", "Dollar":"$", "Yen":"¥"}
# monedas={"Euro":"€", "Dollar":"$", "Yen":"¥"}
# pregunta=input("Ingrese la divisa: ").title()

# print(monedas.get(pregunta.title(), "NO"))

# if  pregunta == moneda["Euro"]:
#     print("€")
# elif pregunta == moneda["Dollar"]  :
#     print("$")
# elif pregunta == moneda["Yen"]:
#     print("¥")
# else:
#     print(f"La divisa {pregunta} no está en el diccionario")        

# monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda=input("Introduce una divisa: ")
# if moneda.title() in monedas:
#     resultado = monedas[moneda.title()]
#     print(resultado)
# else:
#     print(f"La divisa {moneda.title()} no está.")    


# monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda=input("Introduce una divisa: ")

# if moneda.title() in monedas:
#     resultado = monedas[moneda.title()]
#     print(resultado)
# else:
#     print(f"La modena {moneda.title()} no está.")    




# print(monedas.get(moneda.title(), "No hay esa divisa"), moneda.title())


# monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda=input("Introduce una divisa: ")

# print(monedas.get(moneda.title(), "No se encuentra la divisa:"), moneda.title())


# monedas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda=input("Introduce una divisa: ")

# if moneda.title() in monedas:
#     resultado= monedas[moneda.title()]
#     print(resultado)
# else:
#     print(f"La moneda {moneda.title()} no se encuentra. ")


# Usuarios Lista





# nombre=input("Ingrese nombre: ")
# edad=input("Ingrese edad: ")
# direccion=input("Ingrese dirección: ")
# telefono=input("Ingrese teléfono: ")

# datos_personales={
#     "nombre": nombre,
#     "edad": edad,
#     "direccion": direccion,
#     "telefono": telefono
# }

#     # datos_personales={
#     #     "nombre": "nombre",
#     #     "edad": "edad",
#     #     "direccion": "direccion",
#     #     "telefono": "telefono"
#     # }
   
#     # datos_personales["nombre"]=datos1
#     # datos_personales["edad"]=datos2
#     # datos_personales["direccion"]=datos3
#     # datos_personales["telefono"]=datos4

# print(f"\n{datos_personales["nombre"]} tiene {datos_personales["edad"]} años, vive en {datos_personales["direccion"]} y su números de teléfono es {datos_personales["telefono"]}")


# nombre=input("Ingrese su nombre: ")
# edad=input("Ingrese su edad: ")
# direccion=input("Ingrese su dirección: ")
# telefono=input("Ingrese su teléfono: ")

# datos_personales={
#     "nombre": nombre,
#     "edad": edad,
#     "direccion": direccion,
#     "telefono": telefono
# }

# print(f"{datos_personales["nombre"]} tiene {datos_personales["edad"]} años, vive en {datos_personales["direccion"]} y su número de teléfono es {datos_personales["telefono"]}.")



# nombre=input("Ingrese su nombre: ")
# edad=input("Ingrese su edad: ")
# direccion=input("Ingrese su dirección: ")
# telefono=input("Ingrese su teléfono: ")

# datos_personales={
#     "nombre": "nombre",
#     "edad": "edad",
#     "direccion": "direccion",
#     "telefono": "telefono"
# }

# datos_personales["nombre"]=nombre
# datos_personales["edad"]=edad
# datos_personales["direccion"]=direccion
# datos_personales["telefono"]=telefono

# print(f"{datos_personales["nombre"]} tiene {datos_personales["edad"]} años, vive en {datos_personales["direccion"]} y su número de teléfono es {datos_personales["telefono"]}.")


# frutas={
#     "Platano": 1.35,
#     "Manzana": 0.80,
#     "Pera": 0.85,
#     "Naranja": 0.70
# }

# nombre=input("Ingrese Fruta: ")
# kilos=input("Ingrese kilos: ")

# for fruta in range(len(frutas)):
#     precio = frutas.values()
#     float(kilos * precio)
#     # kilos * fruta[]
#     nombre == fruta
#     # print(f"{fruta} {kilos}")
#     print(f"{kilos}")

# frutas={
#     "Platano": 1.35,
#     "Manzana": 0.80,
#     "Pera": 0.85,
#     "Naranja": 0.70
# }

# fruta=input("Ingrese Fruta: ").title()
# kilos=float(input("Ingrese kilos: "))

# if fruta in frutas:
#     print(f"{kilos} Kilos de {fruta} valen {frutas[fruta]*kilos}€.")
# else:
#     print(f"Los siento, la fruta {fruta} no está disponible.")


# frutas={
#     "Platano": 1.35,
#     "Manzana": 0.80,
#     "Pera": 0.85,
#     "Naranja": 0.70
# }

# fruta=input("Ingrese la fruta: ").title()
# kilos=float(input("Ingrese kilos: "))

# if fruta in frutas:
#     print(f"{kilos} kilos de {fruta} cuestan {frutas[fruta]*kilos}")
# else:
#     print(f"La fruta {fruta} no está disponible.")    


# ventas_acciones={
#     "Lunes": 1.35,
#     "Martes": 0.80,
#     "Miercoles": 0.85,
#     "Jueves": 0.70,
#     "Viernes": 3.01
# }

# dia_venta=input("Ingrese el día de la venta: ").title()
# venta=float(input("Ingrese la cantidad de ventas: "))

# if dia_venta in ventas_acciones:
#     total_ventas = ventas_acciones[dia_venta]*venta
#     print(f"{venta} ventas del día {dia_venta} son {total_ventas:.2f}")
# else:
#     print(f"No hay ventas para el día {dia_venta}.")    


# acciones_banco={
#     "Lunes": 1.35,
#     "Martes": 0.80,
#     "Miercoles": 0.85,
#     "Jueves": 0.70,
#     "Viernes": 3.01
# }

# accion_dia=input("Ingrese el día de compra acciones: ").title()
# cantidad=float(input("Ingrese la cantidad de acciones compradas: "))

# if accion_dia in acciones_banco:
#     total_compra = acciones_banco[accion_dia]*cantidad
#     print(f"\n{cantidad} acciones se compraron el día {accion_dia}. \nEl valor total de las acciones compradas son: ${total_compra:.2f}")
# else:
#     print(f"El día {accion_dia} no se encuentra. ")


# print("Ingrese la fecha  dd/mm/aaaa ")
# dia=int(input("Ingrese día:  "))
# mes=int(input("Ingrese mes: "))
# anio=int(input("Ingrese año: "))
# fecha_anio={
#     "dia": "dia",
#     "mes": "mes",
#     "anio": "anio"
# }

# fecha_anio["dia"]=dia
# fecha_anio["mes"]=mes
# fecha_anio["anio"]=anio

# print(f"{fecha_anio["dia"]} de {fecha_anio["mes"]} de {fecha_anio["anio"]}")



# meses = {
#     1:'enero', 
#     2:'febrero', 
#     3:'marzo', 
#     4:'abril', 
#     5:'mayo', 
#     6:'junio', 
#     7:'julio', 
#     8:'agosto', 
#     9:'septiembre', 
#     10:'octubre', 
#     11:'noviembre',
#     12:'diciembre'
# }

# fecha=input("Ingrese una fecha formato: dd/mm/aaaa: ")
# fecha = fecha.split("/")
# print(f"{fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}")


# meses = {
#     1:'enero', 
#     2:'febrero', 
#     3:'marzo', 
#     4:'abril', 
#     5:'mayo', 
#     6:'junio', 
#     7:'julio', 
#     8:'agosto', 
#     9:'septiembre', 
#     10:'octubre', 
#     11:'noviembre',
#     12:'diciembre'
# }

# mes=input("Ingrese fecha dd/mm/aaaa: ")
# fecha= mes.split("/")

# print(f"{fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}")


# meses = {
#     1:'Enero', 
#     2:'Febrero', 
#     3:'Marzo', 
#     4:'Abril', 
#     5:'Mayo', 
#     6:'Junio', 
#     7:'Julio', 
#     8:'Agosto', 
#     9:'Septiembre', 
#     10:'Octubre', 
#     11:'Noviembre',
#     12:'Diciembre'
# }

# consulta=input("Ingrese fecha de consulta dd/mm/aaaa: ")
# fecha=consulta.split("/")

# print(f"{fecha[0]} de {meses[int(fecha[1])]} del {fecha[2]}.")


# materias={
#     "Matemáticas": 6,
#     "Física": 4,
#     "Química": 5,
# }

# for i in materias:
#     total=0
#     total += materias[i]
#     print(f"{i} tiene {materias[i]} créditos" )
# print(f"Total créditos {total}")    


# materias={
#     "Matemáticas": 6,
#     "Física": 4,
#     "Química": 5,
# }
# tota_creditos=0

# for materia, creditos in materias.items():
#     print(f"{materia} tiene {creditos} créditos")
#     tota_creditos += creditos
# print(f"Número total de créditos del curso: {tota_creditos}")    


# ventas={
#     "Lunes": 26,
#     "Martes": 14,
#     "Miércoles": 35,
#     "Jueves": 45,
#     "Viernes": 15
# }
# total_ventas=0

# for dia, cantidad in ventas.items():
#     print(f"{dia} tuvo {cantidad} ventas.")
#     total_ventas += cantidad
# print(f"Total ventas de la semana {total_ventas}")    


# ventas={
#     "Lunes": 26,
#     "Martes": 14,
#     "Miércoles": 35,
#     "Jueves": 45,
#     "Viernes": 15
# }
# total_productos=0

# for dia, cantidad_productos in ventas.items():
#     print(f"El dia {dia} se vendieron {cantidad_productos} productos.")
#     total_productos+=cantidad_productos
# print(f"Se vendieron {total_productos} productos en total en la semana.")    


# while True:
    
#     datos_personales={}
#     dato_nombre=input("Ingrese nombre: ")
#     dato_edad=input("Ingrese edad: ")
#     dato_genero=input("Ingrese genero: ")
#     dato_telefono=input("Ingrese telefono: ")
#     dato_email=input("Ingrese email: ")

#     datos_personales[
#         "nombre":dato_nombre,
#         "edad":dato_edad,
#         "genero":dato_genero,
#         "telefono":dato_telefono,
#         "email":dato_email
#         ]
    
#     for datos, informacion in datos_personales.items():
#         print(f"{datos}{informacion}")

# persona={}
# continuar=True
# while continuar:
#     clave=input("Que Dato quiere introducir: ")
#     valor=input(f"{clave}: ")
#     persona[clave]=valor
#     print(persona)
#     continuar=input("¿Quiere añadir más información (Si/No)? ").title() == "Si"
# print("Gracias por su visita.")    

# persona={}
# continuar=True
# while continuar:
#     clave=input("¿Qué dato desea ingresar? ")
#     valor=input(f"{clave}: ")
#     persona[clave]=valor
#     print(persona)
#     continuar=input("¿Desea gregar un nuevo dato (Si/No)? ").title() == "Si"
# print("Gracias por su visita")    


# productos={}
# continuar=True
# while continuar:
#     print("Ingrese nombre y valor producto.")
#     clave=input("Ingrese nombre producto: ").title()
#     print("Ingrese valor producto.")
#     valor=input(f"{clave}: ")
#     productos[clave]=valor
#     print(productos)
#     continuar=input("¿Añadir nuevo producto? (Si/No) ").lower() == "si"
# print("Gracias por su visita.")    

# productos={}
# continuar=True
# while continuar:
#     clave=input("Ingrese nombre producto: ").title()
#     valor=input(f"Ingrese precio de {clave}: ")
#     productos[clave]=valor
#     print(productos)
#     continuar=input(f"DEsea agregar un nuevo producto (Si/No): ").lower() == "si"
# print("Gracias por su vista")    

# compras={}
# continuar=True

# while continuar:
#     clave=input("Ingrese nombre artículo: ").title()
#     valor=float(input(f"Ingrese valor del {clave}: "))
#     compras[clave]=valor
#     continuar=input("continuar (Si/No) ").lower() == "si"
# precio_total=0
# print("\n\t---Lista compra---")
# for producto, precio in compras.items():
#     print(f"{producto}\t ${precio}")
#     precio_total += precio
# print(f"Total \t${precio_total}")    
    


# compras={}
# continuar=True
# while continuar:
#     producto=input("Ingresar producto: ").title()
#     precio=float(input(f"Ingrese precio de {producto}: "))
#     compras[producto]=precio
#     continuar=input("Añadir otro artículo (Si/No): ").lower() == "si"
# valor_total=0
# print("---Lista de Compra---")
# for producto, precio in compras.items():
#     print(f"{producto}\t{precio}")
#     valor_total+=precio
# print(f"Valor Total: {valor_total}")    


# ventas_dias={}
# continuar=True
# while continuar:
#     dia_venta=input("Ingrese el día de la venta: ").title()
#     venta_total=float(input(f"Ingrese ventas totales del día {dia_venta}: "))
#     ventas_dias[dia_venta]=venta_total
#     continuar=input("Agregar otro día (Si/No): ").lower() == "si"
# total_ventas=0
# print("--Lista de la Compra---")
# for dia, valor in ventas_dias.items():
#     print(f"{dia} \t${valor}")
#     total_ventas += valor
# print(f"Tota: \t${total_ventas}")         





# ingresos_mes={}
# continuar=True
# while continuar:
#     dia_ingreso=input("Ingrese día del ingreso: ").title()
#     ganancia=float(input(f"Ingrese cantidad de dinero {dia_ingreso}: $"))
#     ingresos_mes[dia_ingreso]=ganancia
#     continuar=input("Ingresar otro estudiante (Si/No): ").lower() == "si"
# total_ingresos=0
# print("Lista de Ingresos")
# for dia, dinero in ingresos_mes.items():
#     print(f"{dia}\t${dinero}")
#     total_ingresos+=dinero
# print(f"Total: \t${total_ingresos}")    


# TRADUCTOR


# traduccion={}
# continuar=True
# while continuar:
#     palabras=input("Ingrese palabras: ").lower().split(", ")
#     # palabras.append(palabras)
#     traduccion=[palabras]
#     print(traduccion)
#     frase=input("Ingrese una frase: ").split(", ")
# if frase in traduccion:
#         print("Hola")

# diccionario={}
# palabras=input("Introduce la lista de palabras y traducciones \nen formato palabra:traducción separadas por comas: ")
# for i in palabras.split(','):
#     clave,valor=i.split(':')
#     diccionario[clave]=valor
# frases = input("Introduceuna frase en español: ")
# for i in frases.split():
#     if i in diccionario:
#         print(diccionario[i], end=" ")
#     else:
#         print(i, end=" ")        

# continuar=True
# while continuar:
#     veces=input("Ingrese materia aprobadas: ")
#     # materias
#     for i in range(0,veces,1):

        
# diccionario={}
# palabras=input("Introduce la lista de palabras y traducciones \nen formato palabra:traducción separadas por comas: ")
# for i in palabras.split(','):
#     clave,valor=i.split(':')
#     diccionario[clave]=valor
# frases = input("Introduceuna frase en español: ")
# for i in frases.split():
#     if i in diccionario:
#         print(diccionario[i], end=" ")
#     else:
#         print(i, end=" ")   




# dicionario={}

# palabras=input("Introduce palabras: (, - :) ")
# for i in palabras.split(","):
#     clave, valor = i.split(":")
#     dicionario[clave]=valor

# frase=input("Ingrese frase: ")    
# for i in frase.split() :
#     if i in dicionario:
#         print(dicionario[i], end=" ")    
#     else:
#         print(i, end=" ")


# diccionario={}

# palabras=input("Introduce palabras: ")
# for i in palabras.split(","):
#     clave, valor = i.split(":")
#     diccionario[clave]=valor

# frase=input("Escribe una frase: ")
# for i in frase.split():
#     if i in diccionario:
#         print(diccionario[i], end=" ")
#     else:
#         print(i, end=" ")    



# cambiar_producto={}

# producto=input("Ingrese productos a cambiar: ")
# for i in producto.split(","):
#     clave, valor = i.split(":")
#     cambiar_producto[clave]=valor

# lista_productos=input("Ingrese texto: ")
# for i in lista_productos.split():
#     if i in cambiar_producto:
#         print(cambiar_producto[i], end=" ")
#     else:
#         print(i, end=" ")    

# diccionario_nero={}

# palabras=input("Ingrese palabras ( , - : ) ")

# for i in palabras.split(","):
#     clave, valor = i.split(":")
#     diccionario_nero[clave]=valor

# frase_a_traducir=input("Ingrese la frase: ")
# for i in frase_a_traducir.split():    
#     if i in diccionario_nero:
#         print(diccionario_nero[i], end=" ")
#     else:
#         print(i, end=" ")    


facturas={}

# continuar=True
# while continuar:
#     ingreso_facturas=input("Ingrese numero de factura y valor separado por (,): ")
#     clave, valor = ingreso_facturas.split(" ")
#     facturas[clave]=valor
#     print("Desea añadir una nueva. \n\t1 - Factura \n\t2 - Pagar Factura. \n\t3 - Termina.")
#     continuar=int(input("Ingrese número: "))
#     if continuar == 1:
#         ingreso_facturas=input("Ingrese numero de factura y valor separado por (,)")
#         clave, valor = ingreso_facturas.split(",")
#         facturas[clave]=valor
#     elif continuar == 2:
#         clave=input("Ingrese numero de factura: ")
#         print(f"La factura {clave} ha sido eliminada")
#     elif continuar == 3:
#         break

# print(f"Cantidad a pagar {valor}")    
# print(f"Tota { valor}")    




# #solicitar al usuario ingresar el 
# # presupuesto actual y el luego el 
# # costo del articulo a comprar
# presupuesto, costo = input("Ingrese presupuesto y costo: ").split()

# #Verificar si el cliente puede comprar el articulo
# if int(presupuesto) >= int(costo):
#     print("Puedes comprar el articulo.")
# else:
#     print("No tienes suficiente dinero para comprar el articulo.")


# factura={}
# cobrado=0
# pendiente=0
# continuar= ""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Introduce numero factura: ")
#         coste=float(input("Introduce el coste factura: "))
#         factura[clave]=coste
#         pendiente += coste
#     if continuar == "P":
#         clave=input("Introduce el número de la factura a pagar: ")    
#         coste=factura.pop(clave, 0)
#         cobrado+= coste
#         pendiente -= coste
#     print(f"Recaudado: {cobrado}")    
#     print(f"Pendiente de cobro: {pendiente}")    
#     continuar=input("¿Quieres añadir una nueva Factura (F), Pagarla (P) o Terminar (T)? ").upper()

# Terminar Facturar Pagar
# facturas={}
# cobrado=0
# pendiente=0
# continuar= ""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Ingrese número factura: ")
#         valor=input("Ingrese valor factura: ")
#         facturas[clave]=valor
#         pendiente += cobrado
#     if continuar == "P":
#         clave=input("Ingrese número factura a pagar: ")
#         valor=facturas.pop(clave,0)
#         cobrado+=valor
#         pendiente+=valor
#     print(f"Recaudado: {cobrado}")    
#     print(f"Pendiente {pendiente}")
#     continuar=input("¿Quieres añadir una nueva Factura (F), Pagarla (P) o Terminar (T)? ").upper()

# Terminar Facturar Pagar
# cobrado+=valor
# pendiente+=valor

# facturas={}
# cobrado=0
# pendiente=0
# continuar= ""

# while continuar != "T":
#     if continuar == "F":
#         clave=input("Ingrese numero factura:")
#         valor=float(input("Ingrese valor factura: "))
#         facturas[clave]=valor
#         pendiente+=cobrado
#     if continuar == "P":
#         clave=input("Ingrese numero factura: ")
#         valor=facturas.pop(clave, 0)
#         cobrado+=valor
#         pendiente+=valor
#     print(f"Cobrado: {cobrado}")        
#     print(f"Pendiente: {pendiente}")
#     continuar=input("¿Quieres añadir una nueva Factura (F), Pagarla (P) o Terminar (T)? ").upper()
      


# facturas={}
# pagado=0
# sin_pagar=0
# continuar=""


# continuar=input("¿Quieres añadir una nueva Factura (F), Pagarla (P) o Terminar (T)? ").upper()
    

# facturas={}
# pagado=0
# sin_pagar=0
# continuar=""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Ingrense numero de factura: ")
#         valor=float(input("Ingrene valor de factura: "))
#         facturas[clave]=valor
#         pagado+=sin_pagar
#     if continuar == "P":
#         clave=input("Ingrese numero factura a pagar: ")
#         valor=facturas.pop(clave,0)
#         pagado+=valor
#         sin_pagar-=valor
#     print(f"Pagado {pagado}")    
#     print(f"Sin pagar: {sin_pagar}")
#     continuar=input("¿Quieres añadir una nueva Factura (F), Pagarla (P) o Terminar (T)? ").upper()
      

# facturas={}
# pagadas=0
# sin_pagar=0
# continuar=""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Numero factura: ")
#         valor=float(input("Valor factura: "))
#         facturas[clave]=valor
#         sin_pagar+=pagadas
#     if continuar == "P":
#         clave=input("Ingrene numeros factura a pagar: ")    
#         valor=facturas.pop(clave,0)
#         pagadas+=valor
#         sin_pagar-=pagadas
#     print(f"Pagadas {pagadas}")    
#     print(f"Sin pagar {sin_pagar}")
#     continuar=input("¿Quieres añadir una nueva Factura (F), Pagarla (P) o Terminar (T)? ").upper()
      

# facturas={}
# pagadas=0
# sin_pagar=0
# continuar=""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Número Factura: ")
#         valor=float(input("Valor Factura: "))
#         facturas[clave]=valor
#         sin_pagar+=valor
#     if continuar == "P":
#         clave=input("Numero factura a pagar: ")
#         valor=facturas.pop(clave)
#         pagadas+=valor
#         sin_pagar-=pagadas
#     print(f"Pagadas {pagadas}")        
#     print(f"Sin Pagar {sin_pagar}")
#     continuar=input("T - F - P: ").upper()        





# facturas={}
# pagadas=0
# sin_pagar=0
# continuar=""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Número Factura: ")
#         valor=float(input("Valor Factura: "))
#         facturas[clave]=valor
#         sin_pagar+=valor
#     if continuar == "P":
#         clave=input("Número factura a pagar: ") 
#         valor=facturas.pop(clave,0) 
#         pagadas+=valor
#         sin_pagar-=valor
#     print(f"Pagadas: {pagadas}")    
#     print(f"Sin pagar {sin_pagar}")
#     continuar=input("T - F - P : ")    


# facturas={}
# pagadas=0
# sin_pagar=0
# continuar=""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Número Factura: ")
#         valor=float(input("Valor Factura: "))
#         facturas[clave]=valor
#         sin_pagar+=valor
#     if continuar == "P":
#         clave=input("Ingrese Número Factura a pagar: ")    
#         valor=facturas.pop(clave, 0)
#         pagadas+=valor
#         sin_pagar-=valor
#     print(f"Pagadas {pagadas}")    
#     print(f"sin Pagar: {sin_pagar}")
#     continuar=input("T - F - P : ").upper()
# print("---Fin---")        

# facturas={}
# pagadas=0
# sin_pagar=0
# continuar=""
# while continuar != "T":
#     if continuar == "F":
#         clave=input("Número Factura: ")
#         valor=float(input("Valor Factura: "))
#         facturas[clave]=valor
#         sin_pagar+=valor
#     if continuar == "P":
#         clave=input("# Factura a pagar: ")
#         valor=facturas.pop(clave,0)
#         pagadas+=valor
#         sin_pagar-=valor
#     print(f"Pagadas: {pagadas}")        
#     print(f"Sin Pagar: {sin_pagar}")      
#     continuar=input("T - F - P : ").upper()  

# CLIENTES EMPRESA
# nif=0
# clientes={}

# continuar=""
# while continuar != "6":

#     print("1- Ingresar Datos cliente: ")
#     print("2- Eliminar cliente, ingerese NIF: ")
#     print("3- Ingrese NIF ver base de datos: ")
#     print("4- Mostrar todos los clientes: ")
#     print("5- Clientes Preferentes: ")
#     print("6- Terminar.")
#     continuar=input("\tIngrese número: ")

#     if continuar == "1":
#         nif=input("Ingrese Nif: ") 
#         nombre=input("Ingrese su Nombre: ")
#         direccion=input("Ingrese su dirección: ")
#         telefono=input("Ingrese su teléfono: ")
#         email=input("Ingrese su email:")
       

#     elif continuar == "2":
#          nif=input("Ingrese su nif: ")
#          clientes.pop(nif)

#     elif continuar == "3":
#         nif=input("Ingrese su nif: ")
#         print(f"{clientes["nif"]}")

#     elif continuar == "4":
#         for clave, valor in clientes.items(): 
#             print(f"{clave} {valor}")   

#     elif continuar == "5":
#         print("Clientes preferentes")
#         clientes["preferentes"] 

# clientes={}
# opcion=""
# while opcion != "6":
#     if opcion == "1":
#         dni=input("Introduce DNI del cliente: ")
#         nombre=input("Nombre Cliente: ")
#         direccion=input("Dirección Cliente: ")
#         telefono=input("Teléfono Cliente: ")
#         email=input("Email Cliente: ")
#         vip=input("¿Cliente Preferente? (S/N)").upper()
#         cliente={
#             "nombre": nombre,
#             "dirección": direccion,
#             "telefono": telefono,
#             "email": email,
#             "preferente": vip=="S",
#         }
#         clientes[dni]=cliente

#     if opcion == "2":
#         dni=input("Introduce DIN del cliente: ")
#         if dni in clientes:
#             del clientes[dni]
#         else:
#             print(f"No exite u cliente con el DNI {dni}")    

#     if opcion == "3":
#         dni=input("Introduce DNI del cliente: ")
#         if dni in clientes:
#             print(f"DNI {dni}")
#             for clave, valor in clientes[dni].items():
#                 print(clave.title() + ":", valor)
#         else:
#             print(f"DNI {dni} no encontrado")
    
#     if opcion == "4":
#         print("Lista de clientes")
#         for clave, valor in clientes.items():
#             print(clave, valor["nombre"])

#     if opcion == "5":
#         print("Lista de clientes preferentes")
#         for clave, valor in clientes.items():
#             if valor["preferente"]:
#                 print(clave, valor["nombre"])

#     print("1- Ingresar Datos cliente: ")
#     print("2- Eliminar cliente, ingerese NIF: ")
#     print("3- Ingrese NIF ver base de datos: ")
#     print("4- Mostrar todos los clientes: ")
#     print("5- Clientes Preferentes: ")
#     print("6- Terminar.")
#     opcion=input("\tIngrese número: ")
    # opcion=input("")   

    # opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
                         
# CLIENTES

# usuarios={}
# menu=""
# while menu!=6:
#         #MENU PROGRAMA
#         print("1- Ingresar Datos cliente: ")
#         print("2- Eliminar cliente, ingerese NIF: ")
#         print("3- Ingrese NIF ver base de datos: ")
#         print("4- Mostrar todos los clientes: ")
#         print("5- Clientes Preferentes: ")
#         print("6- Terminar.")
#         menu=int(input("\tIngrese número: "))

#         if  menu == 1:
#             #INGRESAR DATOS USUARIO
#             cedula=input("Escribe tu cédula: ")
#             nombre=input("Escribe tu nombre: ")
#             direccion=input("Escribe tu dirección: ")
#             telefono=input("Escribe tu teléfono: ")
#             email=input("Escribe tu email: ")
#             vip=input("¿Cliente Preferente? (S/N) ").upper()
#             usuario={
#                 "nombre": nombre,
#                 "direccion": direccion,
#                 "telefono": telefono,
#                 "email": email,
#                 "preferente": vip=="S"
#             }
#             usuarios[cedula]=usuario

#         if menu == 2:
#             #ELIMINAR USUARIO
#             cedula=input("Introduce Cédula cliente: ")
#             if cedula in usuarios:
#                 del usuarios[cedula]
#                 print("Usuario eliminado") 
#             else:
#                 print(f"No hay usuario con esa cédula {cedula}")       


#         if menu == 3:
#             #BASE DATOS USUARIOS
#             cedula=input("Introduce cédula usuario: ")
#             if cedula in usuarios:
#                 print(f"Cédula: {cedula}")
#                 for clave, valor in usuarios[cedula].items():
#                     print(clave.title() + ":", valor)
#             else: 
#                 print(f"Cédula {cedula} no encontrada.")

#         if menu == 4:
#             #MOSTRAR TODOS LOS USUARIO
#             print("--Lista de clientes--")    
#             for clave, valor in usuarios.items():
#                 # if valor["preferente"]:
#                     print(clave, valor["nombre"])

#         if menu == 5:
#             #LISTA CLIENTES PREFERENTES
#             print("Lista de clientes preferentes")
#             for clave, valor in usuarios.items():
#                 if valor["preferente"]:
#                     print(f"\tUsuario: {clave, valor["nombre"]}") 


# productos

# productos={}
# menu=""
# while menu !=6:
#     #MENU PROGRAMA
#         print("1- Ingresar Datos producto: ")
#         print("2- Eliminar producto, ingrese ID: ")
#         print("3- Ingrese ID ver base de datos: ")
#         print("4- Mostrar todos los productos: ")
#         print("5- Productos Preferentes: ")
#         print("6- Terminar.")
#         menu=int(input("\tIngrese número: "))

#         if menu == 1:
#             #INGRESAR DATOS Productos
#             id=input("ID del producto: ")
#             nombre_producto=input("Nombre producto: ")
#             marca_producto=input("Ingrse marca: ")
#             tamanio_producto=input("Ingrese tamaño: ")
#             email_soporte=input("Ingrese email soporte al clente: ")
#             vip=input("Producto de lujo (S/N)").upper()
#             producto={
#                 "nombre_producto": nombre_producto,
#                 "marca_producto": marca_producto,
#                 "tamanio_producto": tamanio_producto,
#                 "email_soporte": email_soporte,
#                 "producto_lujo": vip=="S"
#             } 
#             productos[id]=producto

#             if menu == 2:
#                 #ELIMINAR USUARIO
#                 id=input("Introduce ID producto: ")
#                 if id in productos:
#                     del productos[id]
#                     print(f"Producto con el ID {id} eliminado.")
#                 else:
#                     print(f"Producto con el ID {id} no encontrado.")

#             if menu == 3:
#                 #Mostrar DATOS Productos
#                 id=input("Introduce ID producto: ")
#                 if id in productos:
#                     print(f"ID {id}")
#                     for clave, valor in productos[id].items():
#                         print(f"ID {clave.title()} : {valor}")
#                 else:
#                     print(f"ID {id} no enontrado.")

#             if menu == 4:
#                 #MOSTRAR TODOS LOS Produtos
#                 print("--Lista de productos--")
#                 for clave, valor in productos.items():
#                         print(f"{clave}{valor["nombre_producto"]}") 

#             if menu == 5:
#                  #Productos LUJO
#                  print("Lista de productos de Lujo.")
#                  for clave, valor in productos.items():
#                       if valor["producto_lujo"]:
#                            print(f"\tProducto: {clave}{valor["nombre_producto"]}")
                             

# estudiantes

# estudiantes={}
# menu=""
# while menu !=6:
#     #MENU Estudiantes
#         print("1- Ingresar Datos Estudiantes: ")
#         print("2- Eliminar Estudiantes, ingrese ID: ")
#         print("3- Ingrese ID ver base de datos: ")
#         print("4- Mostrar todos los Estudiantes: ")
#         print("5- Estudiantes Preferentes: ")
#         print("6- Terminar.")
#         menu=int(input("\tIngrese número: "))

#         if menu ==1:
             
#              #Ingresar Datos Estudiante
#              id=input("Ingrese el Id del estudiante: ")
#              nombre=input("Ingrese el nombre del estudiante: ").title()
#              direccion=input("Ingrese el dirección del estudiante: ").title()
#              telefono=input("Ingrese el telefono del estudiante: ")
#              email=input("Ingrese el email del estudiante: ")
#              vip=input("¿Estudiante Preferente? (S/N) ").upper()

#              estudiante={
#                   "nombre": nombre,
#                   "direccion": direccion,
#                   "telefono": telefono,
#                   "email": email,
#                   "preferente": vip=="S"
#              }
#              estudiantes[id]=estudiante

#         if menu == 2:
#              #Eliminar Estudiante
#              id=input("Ingrese ID de estudiante: ")
#              if id in estudiantes:
#                   del estudiantes[id]
#                   print(f"Estudiante con el ID {id} borrado.")
#              else:
#                   print(f"Estudiante con ID {id} no encontrado.") 

#         if menu == 3:
#               #Mostrar datos ESTUDIANTES
#               id=input("Ingrese id del estudiante a consultar: ")
#               if id in estudiantes:
#                     print(f"ID estudiante: {id}")
#                     for clave, valor in estudiantes[id].items():
#                           print(f"{clave.title()} Datos: {valor}")
#               else:
#                     print(f"Estudiante conId {id} no encontrado: ")

#         if menu == 4:
#               #Mostrar todo los estudiantes
#               print("--Lista de estudiantes--")
#               for clave, valor in estudiantes.items():
#                     print(f"ID {clave} Nombre: {valor["nombre"]}")

#         if menu == 5:
#               #Estudaiantes preferemtes
#               print("Estudiantes en Maestria")
#               for clave, valor in estudiantes.items():
#                     if valor["preferente"]:
#                         print(f"\tEstudiante: {valor["nombre"]} preferente {valor["preferente"]}")            

# Preguntar los datos del cliente, 
# crear un diccionario con los datos y añadirlo a la base de datos.

# Preguntar por el NIF del cliente y eliminar sus 
# datos de la base de datos.

# Preguntar por el NIF del cliente y 
# mostrar sus datos.

# Mostrar lista de todos los clientes 
# de la base datos con su NIF y nombre.

# Mostrar la lista de clientes preferentes 
# de la base de datos con su NIF y nombre.

# Terminar el programa.
             
                  
# MASCOTAS

# mascotas={}
# menu=""
# while menu !=6:
#          #MENU Estudiantes
#         print("1- Ingresar Datos mascota: ")
#         print("2- Eliminar mascota, ingrese ID: ")
#         print("3- Ingrese ID ver base de datos: ")
#         print("4- Mostrar todos las mascota: ")
#         print("5- Mascota Preferente: ")
#         print("6- Terminar.")
#         menu=int(input("\tIngrese número: "))

#         if menu == 1:
#            #CREAR MASCOTA
#            id=input("Ingrese ID mascota: ")     
#            nombre_mascota=input("Ingrese nombre mascota: ")     
#            edad_mascota=input("Ingrese edad mascota: ")     
#            raza_mascota=input("Ingrese raza mascota: ")     
#            peso_mascota=input("Ingrese peso mascota: ")     
#            pedrigri=input("Pedrigrí mascota (S/N): ").upper()

#            mascota={
#                  "nombre_mascota": nombre_mascota,
#                  "edad_mascota": edad_mascota,
#                  "raza_mascota": raza_mascota,
#                  "peso_mascota": peso_mascota,
#                  "pedrigri": pedrigri=="S"
#            }     
#            mascotas[id]=mascota

#         if menu == 2:
#               #ELIMINAR MASCOTA
#             id=input("Ingrese ID de mascota para borrar: ")
#             if id in mascotas:
#                 del mascotas[id]
#                 print(f"Mascota con ID {id} borrada.")
#             else:
#                 print(f"Mascota con ID {id} no encontrada. ") 

#         if menu == 3:   
#              #MOSTRAR DATOS CLIENTE: 
#             id=input("Ingre Id de mascota: ")
#             if id in mascotas:
#                 print(f"ID mascota: {id}")
#                 for clave, valor in mascotas[id].items():
#                     print(f"Mascota {clave.title()} Datos: {valor}")
#             else:
#                 print(f"Mascota con ID {id} no encontrada: ")

#         if menu == 4:
#              #MOSTAR BASEDE DATOS MASCOTAS
#              print("--Lista de Mascotas--")
#              for clave, valor in mascotas.items():
#                   print(f"ID {clave} Nombre: {valor["nombre_mascota"]}")         
             
#         if menu == 5:
#              # MASCOTAS PREFERENTES
#              print("Mascotas con Pedigrí")
#              for clave, valor in mascotas.items():
#                   print(f"ID: {id} Nombre: {valor["nombre_mascota"]}. Pedrigí: {valor["pedrigri"]}")
               
                          
#  0  Menú general                

#  1  Ingresar Clientes
     
#  2  ELIMINAR Cliente
   
#  3  Motrar Cliente
  
#  4  MOSTRAR TODOS los CLIENTEs: 
 
#  5  Cliente PREFERENTES
     
#  6  Terminar
           
                          
                


# clientes_banco={}
# menu=""

# while menu != 6:
#     #Menu Clientes
#     print("---Menu Principal---")
#     print("Ingresar datos cliente 1.")
#     print("Borrar Cliente 2.")
#     print("Buscar Cliente 3.")
#     print("Mostrar todos los clientes 4.")
#     print("Clientes Preferentes 5.")
#     print("Terminar 6.")
#     menu=int(input("Ingrese numero: "))

#     if menu == 1:
#         #Crear Cliente
#         cuenta=input("Ingrese número cuenta cliente: ")
#         nombre_cliente=input("Ingrese nombre cliente: ").title()
#         documento_cliente=input("Ingrese documento cliente: ")
#         direccion_cliente=input("Ingrese dirección cliente: ")
#         telefono_cliente=input("Ingrese teléfono cliente: ")
#         email_cliente=input("Ingrese email cliente: ")
#         preferente_cliente=input("Es cliente preferente (S/N): ").upper()

#         cliente={
#             "nombre": nombre_cliente,
#             "documento": documento_cliente,
#             "direccion": direccion_cliente,
#             "telefono": telefono_cliente,
#             "email": email_cliente,
#             "preferente": preferente_cliente=="S"
#         }

#         clientes_banco[cuenta]=cliente

#     if menu == 2:
#         #Borrar Cliente
#         print("---Borrar cliente---")
#         cuenta=input("Ingrese cuenta del cliente: ")
#         if cuenta in clientes_banco:
#             del clientes_banco[cuenta]
#             print(f"Cliente con la cuenta {cuenta} ha sido borrado.")
#         else:
#             print(f"Cliente con cuenta {cuenta} no encontrado.")        

#     if menu == 3:
#         #Mostrar cliente ID
#         print("--Mostrar Clientes--")
#         cuenta=input("Ingrese cuenta de cliente: ")
#         if cuenta in clientes_banco:
#             print(f"")
#             for clave, valor in clientes_banco[cuenta].items():
#                 print(f"{clave.title()}: {valor}")
#         else:
#             print(f"Cliente con cuenta {cuenta} no encontrado.")  

#     if menu == 4:
#         #Mostrar Base de Datos
#         print("---Base de Datos---")
#         for clave, valor in clientes_banco.items():
#             print(f"Cédula {clave} Nombre: {valor["nombre"]}")
#         # else:
#         #     print("Base de datos vacia.")
#     if menu == 5:
#         print("---Clientes Preferentes---")
#         cuenta=input("Ingrese cuenta del cliente: ")
#         if cuenta in clientes_banco:
#             for clave, valor in clientes_banco.items():
#                 print("Sí es Cliente Preferente")
#                 print(f"Cuenta: {cuenta}. Nombre {valor["nombre"]}. Cliente Preferente: {valor["preferente"]}.")   
#         else:
#             print(f"Cliente con cuenta {cuenta} no es preferente.")
# print("---FIN---")     

    





#  0  Menú general                

#  1  Ingresar Clientes
     
#  2  ELIMINAR Cliente
   
#  3  Motrar Cliente
  
#  4  MOSTRAR TODOS los CLIENTEs: 
 
#  5  Cliente PREFERENTES
     
#  6  Terminar



# vehiculos={}
# menu=""
# while menu != 6:
#     # Menu General
#     print("---Menu Parqueadero---")
#     print("1 Ingresar vehículo.")
#     print("2 Eliminar Vehículo.")
#     print("3 Mostrar Vehículo")
#     print("4 Mostrar todos los vehículos.")
#     print("5 Servicio VIP.")
#     print("6 Terminar.")
#     menu=int(input("Ingrese Número: "))

#     if menu == 1:
#         # Ingresar Vehículo
#         placa=input("Ingrese Placa Vehículo: ").upper()
#         hora_ingreso=input("Hora de ingreso Vehículo: ")
#         marca=input("Ingrese Marca Vehículo: ").title()
#         tipo_vehiculo=input("Ingrese Tipo Vehículo: ").title()
#         color=input("Ingrese color Vehículo: ").title()
#         vip=input("Vehículo VIP (S/N) ").upper()

#         vehiculo={
#             "placa": placa,
#             "hora_ingreso": hora_ingreso,
#             "marca": marca,
#             "tipo_vehiculo":tipo_vehiculo,
#             "color": color,
#             "vip": vip=="S"
#         }

#         vehiculos[placa]=vehiculo

#     if menu == 2:
#         # Eliminar Vehículo
#         placa=input("Ingrese placa de vehículo a borrar: ").upper()
#         if placa in vehiculos:
#             del vehiculos[placa]
#             print(f"Vehículo con placa {placa} borrado.")
#         else:
#             print(f"Vehículo con placa {placa} no encontrado.")    
#     if menu == 3:
#         #Motrar vehículo
#         placa=input("Ingrese placa de vehículo: ").upper()
#         if placa in vehiculos:
#             for clave, valor in vehiculos[placa].items():  
#                 print(f"{clave.title()}: {valor}")
#         else: 
#             print(f"Vehículo con placa {placa} no encontrado.")


#     if menu == 4:
#         #Mostrar todos los vehículos
#         print("---Lista de Vehíulos---")
#         for clave,valor in vehiculos.items():
#             print(f"Placa {clave}. Marca Vehículo: {valor["marca"]}.")

#     if menu == 5:
#         #Vehículo VIP
#         print("---Vehículos VIP---")
#         placa=input("Ingrese Placa de Vehículo: ").upper()
#         if placa in vehiculos:
#             for clave, valor in vehiculos.items():
#                 print("---Vehículo VIP---")
#                 print(f"Vehículo con placa {placa} VIP: {valor["vip"]}")
#         else:
#             print(f"Vehículo con placa {placa} no es VIP")



#  0  Menú general                

#  1  Ingresar Clientes
     
#  2  ELIMINAR Cliente
   
#  3  Motrar Cliente
  
#  4  MOSTRAR TODOS los CLIENTEs: 
 
#  5  Cliente PREFERENTES
     
#  6  Terminar

#"nif;nombre;email;teléfono;descuento
# \n01234567L;   
#               Luis González;   
#               luisgonzalez@mail.com;   
#               656343576;12.5

# \n71476342J;   
#               Macarena Ramírez;   
#               macarena@mail.com;   
#               692839321;8
# \n63823376M;   
#               Juan José Martínez;   
#               juanjo@mail.com;   
#               664888233;5.2
# \n98376547F;   
#               Carmen Sánchez;   
#               armen@mail.com;   
#               667677855;15.7"

#{'01234567L': {'nombre': 'Luis González', 
#                'email': 'luisgonzalez@mail.com', 
#             'teléfono': '656343576', 
#            'descuento': 12.5}, 

# '71476342J': {'nombre': 'Macarena Ramírez', 
#                'email': 'macarena@mail.com', 
#             'teléfono': '692839321', 
#            'descuento': 8.0}, 

# '63823376M': {'nombre': 'Juan José Martínez', 
#                'email': 'juanjo@mail.com', 
#             'teléfono': '664888233', 
#            'descuento': 5.2}, 

# '98376547F': {'nombre': 'Carmen Sánchez', 
#                'email': 'carmen@mail.com', 
#             'teléfono': '667677855', 
#            'descuento': 15.7}}

# base_datos={
#             "id": {
#             "nombre": "nombre",
#             "email": "email",
#             "teléfono": "telefono",
#             "descuento": float()
#         }

# }

# clientes={
#         '01234567L': {
#           'nombre': 'Luis González', 
#            'email': 'luisgonzalez@mail.com', 
#         'teléfono': '656343576', 
#        'descuento': 12.5
#        }, 

#        '71476342J': {
#           'nombre': 'Macarena Ramírez', 
#            'email': 'macarena@mail.com', 
#         'teléfono': '692839321', 
#        'descuento': 8.0
#            }, 

#        '63823376M': {
#           'nombre': 'Juan José Martínez', 
#            'email': 'juanjo@mail.com', 
#         'teléfono': '664888233', 
#        'descuento': 5.2
#            }, 

#        '98376547F': {
#           'nombre': 'Carmen Sánchez', 
#            'email': 'carmen@mail.com', 
#         'teléfono': '667677855', 
#        'descuento': 15.7
#            }
#         }



# base_datos[id]=clientes

# print(base_datos["id"])


# DATOS CLIENTES

# datos_clientes= "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

# lista_clientes = datos_clientes.split("\n")
# directorio={}
# lista_campos= lista_clientes[0].split(";")

# for i in lista_clientes[1:]:
#     cliente={}
#     lista_info=i.split(";")

#     for j in range(1,len(lista_campos)):
#         if lista_campos[j] == "descuento":
#             lista_info[j]= float(lista_info[j])
#             cliente[lista_campos[j]] = lista_info[j]
#     directorio[lista_info[0]]=cliente

# print(directorio)    





# # Datos estudiants
# datos_estudiantes= "nif;nombre;email;teléfono;promedio\n01234567L;Luis González;luisgonzalez@mail.com;656343576;4.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;4\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;4.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;3.7"

# lista_estudiantes= datos_estudiantes.split("\n")

# directorio={}

# lista_espacios=lista_estudiantes[0].split(";")

# for i in lista_estudiantes[1:]:
#     estudiante={}
#     lista_data=i.split(";")

#     for j in range(1,len(lista_espacios)):
#         if lista_espacios[j]=="promedio":
#             lista_data[j] = float(lista_data[j])
#             estudiante[lista_espacios[j]]= lista_data[j]
#     directorio[lista_data[0]]=estudiante  

# for clave, valor in directorio.items():
#     print(f"Código: {clave} Promedio: {valor["promedio"]}")      

# print(directorio)


# lista_salon="nif;nombre;email;teléfono;promedio\n01234567L;Luis González;luisgonzalez@mail.com;656343576;4.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;4\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;4.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;3.7"

# lista_estudiantes=lista_salon.split("\n")

# directorio={}

# lista_datos=lista_estudiantes[0].split(";")

# for i in lista_estudiantes[1:]:
#     estudiante={}
#     lista_datos=i.split(";")

#     for j in range(1,len(lista_datos)):
#         if lista_datos[j]=="promedio":

#             lista_datos[j] = float(lista_datos[j])
#             estudiante[lista_datos[j]]=lista_datos[j]

#     directorio[lista_datos[0]]=estudiante

# for clave, valor in directorio.items():
#     print(f"Código: {clave} Promedio; {valor["promedio"]}")            


# lista_clientes="nif;nombre;email;teléfono;promedio\n01234567L;Luis González;luisgonzalez@mail.com;656343576;4.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;4\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;4.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;3.7"

# #convierno el String a un lista con SPLIT 
# # y los separo con , ahora tiene un indice
# clientes_lista=lista_clientes.split("\n")

# #Creo un diccionario general
# directorio={}

# #nif;nombre;email;teléfono;promedio
# lista_espacios=clientes_lista[0].split(";")

# #separa las informaicón por 
# # comas ,  desde el 1 de la lista.
# # y crea un diccionario  
# for i in clientes_lista[1:]:

#     clientes={}
#     lista_datos = i.split(";")

#     #Itera la lista que ha sido separa por comas ,
#     for j in range(1,len(lista_espacios)):

#         #Al iterar acá revisa que en la lista 
#         #haya el valor "promedio"
#         if lista_espacios[j]=="promedio":

#             #convierte el float el String de numeros
#             # a Float número.
#             lista_datos[j]=float(lista_datos[j])
            
#             #Pasa la lista datos a el diccionario Clientes
#             #lista_espacio se convierne en CLAVE
#             #Del diccionario y Lista datos el VALOR
#             clientes[lista_espacios[j]] = lista_datos[j]

#         #Imprime el dicionario con el índice [0] 
#         directorio[lista_datos[0]]=clientes  

# print(directorio)

# REPASO REPASO

# lista_vendedores="nif;nombre;email;teléfono;promedio\n01234567L;Luis González;luisgonzalez@mail.com;656343576;4.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;4\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;4.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;3.7"

# vendedores_lista= lista_vendedores.split("\n")
# base_datos={}
# vendedores_espacios= vendedores_lista[0].split(";")

# for i in vendedores_lista[1:]:
#     vendedores={}
#     vendedores_datos=i.split(";")

#     for j in range(1,len(vendedores_espacios)):
#         if vendedores_espacios[j]=="promedio":

#             vendedores_datos[j]=float(vendedores_datos[j])
#             vendedores[vendedores_espacios[j]] = vendedores_datos[j]

#         base_datos[vendedores_datos[0]] = vendedores

# for clave, valor in base_datos.items():   
#     print(f"ID: {clave}. Promedio: {valor["promedio"]}")     
# print(base_datos)            



# lista_hv="nif;nombre;email;teléfono;promedio\n01234567L;Luis González;luisgonzalez@mail.com;656343576;4.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;4\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;4.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;3.7"

# new_hv = lista_hv.split("\n")

# directorio={}

# espacios_hv=new_hv[0].split(";")

# for i in new_hv[1:]:
#     hvs={}
#     lista_datos_hv=i.split(";")
#     for j in range(1,len(espacios_hv)):
#         if espacios_hv[j]=="promedio":

#             lista_datos_hv[j]=float(lista_datos_hv[j])
#             hvs[espacios_hv[j]]=lista_datos_hv[j]

#         directorio[lista_datos_hv[0]]=hvs

# for clave, valor in directorio.items():
#     print(f"ID: {clave} Promedio: {valor["promedio"]}")


# FUnciones

# def saludar():
#     print("¡Hola amiga!")
#     return

# saludar()    

# def nombre():
#     tu_nombre=input(f"Ingrese su nombre: ")
#     print(f"¡hola {tu_nombre}!")
#     return

# nombre()


# def greet(nombre):
#     """Función que muestra un saludo por pantalla.
#         Parámetros
#         nombre: Nombre del usuario
#         Devuelve el saludo ¡Hola nombre!.
#         """
#     print("¡Hola " + nombre + "!")


# greet("Ana")    
# greet("Python Juliana")    


# def factorial(a):
#     resultado  = a * 1 * a * 3 * a
#     print(f"{resultado}")
#     return resultado


# factorial(2)



# def factorial(n):

#     """Función que calcula el factorial 
#      de un número entero positivo.
#         Parámetros n: Es un entero positivo.
#         Devuelve el factorial de n.
#     """

#     algoritmo = 1
#     for i in range(n):
        
#         algoritmo *= i + 1
#     return algoritmo

# # 4!  Factorial
# # 20!  Factorial
# # 500!  Factorial
# # El ! es el simbolo de factorial
# print(factorial(4))    
# print(factorial(20))    
# print(factorial(600))    



# def factorial(numero):

#     factorizar = 1
#     for i in range(numero):
#         factorizar *= i + 1
#     return factorizar

# print(factorial(4))
# factorial(4)
# factorial(6)


# def factorial(n):

#     factorizar = 1
#     for i in range(n):
#         factorizar *= i + 1
#     return factorizar

# print(factorial(10))        
# print(factorial(9))        
# print(factorial(8))        



# def factorial(numero):

#     factorizar = 1

#     for i in range(numero):

#         factorizar *= i + 1

#     return factorizar

# print(factorial(3))        
# print(factorial(5))        
# print(factorial(6))        



# def factorizar(num):

#     factorial = 1

#     for i in range(num):

#         factorial *= i + 1

#     return factorial

# print(factorizar(7))    
# print(factorizar(5))    

# funcion con IVA

# def facturas(cantidad, iva=21):

#     # if iva >= 1:
#     #     total = cantidad * iva
#     #     return  total    
#     # elif iva == 0:
#     #     total = cantidad * iva     

#     return cantidad + cantidad * iva/100

# cantidad=float(input(f"Cantidad sin IVA: "))
# iva=float(input(f"IVA %: "))

# print(f"Tiene IVA del: {iva}% Total: ${facturas(cantidad, iva)}")
# print(f"IVA del 21% Total: ${facturas(cantidad)}")

        
# def venta(cantidad, iva=21):
#     return cantidad + cantidad * iva / 100

# cantidad=float(input("Cantidad venta: "))
# iva=float(input("Ingrese IVA %: "))

# print(f"Venta con IVA {venta(cantidad,iva)}")
# print(f"Sin IVA {venta(cantidad)}")



# def venta(ventas, iva=21):
#     return ventas + ventas * iva /100


# ventas=float(input("Ingrese Venta: "))
# iva=float(input("IVA: "))

# print(f"IVA del {iva}% Total: ${venta(ventas,iva)}")
# print(f"Venta IVA del 21% Total: ${venta(ventas)}")



































































































































































# def pagos(dinero, iva=21):
#     dinero = dinero + dinero * iva / 100
#     return dinero


# dinero=float(input("Ingerse la cantidad: "))
# iva=float(input("Ingrese % IVA: "))

# print(f"IVA {iva} Total: {pagos(dinero,iva)}")
# print(f"IVA del 21% Total: {pagos(dinero)}")



# def compras(pagos,iva=21):
#     pagos = pagos + pagos * iva / 100
#     return pagos


# pagos=float(input("Ingrese pago: "))
# iva=float(input("Ingrese IVA: "))


# print(f"IVA del {iva}. Total: {compras(pagos,iva)}")
# print(f"IVA del 21% {compras(pagos)}")



# def circulo(circulos):
#     circulos = circulos ** 2
#     circulos =  float(3,14159) * circulos 
#     return float(circulos)


# circulos=float(input("Ingrese radio del circulo: "))

# print(f"Área del curculo es: {circulo}")




# def circulo_area(radio):

#     pi = 3.1415
#     resultado = pi * radio ** 2
#     return resultado

# def volumen_cilindro(radio, altura):

#     resultado = circulo_area(radio)*altura 
#     return resultado


# radio=int(input("Ingrese radio cilíndro: "))
# altura=int(input("Ingrese altura: "))


# print(f"Área: {circulo_area(radio):.2f}")
# print(f"Volumen del cilindro {volumen_cilindro(radio,altura):.2f}")



# def circulo(radio):
#     pi = 3.1415
#     resultado = pi * radio ** 2
#     return resultado

# def volumen_circulo(radio, altura):
#     resultado = circulo(radio)*altura
#     return resultado


# radio=int(input(f"Ingrese radio: "))
# altura=int(input(f"Ingrese altura: "))


# print(f"Área círculo: {circulo(radio):.2f}")
# print(f"Volúmen cilindro: {volumen_circulo(radio,altura):.2f}")


# numero_lista=[2,2,4,5,3,6]


# def media(numero_lista):
#     for i in range(1,len(numero_lista)):
#         numero_lista = i += 1
#         numero_lista / len(numero_lista)
#         return i

# print(f"Media {media(numero_lista)}")        


# numero_lista=[1,2,3,4,5]
# def media(numero_lista):
#     suma=0
#     for i in numero_lista:
#         suma += i
#         media = suma / len(numero_lista)
#     return media

# print(f"Media: {media(numero_lista):.2f}")  

# # DOS

# numero_lista=[2.3, 5.7, 6.8, 9.7, 12.1, 15.6]
# def media(numero_lista):
#     suma=0
#     for i in numero_lista:
#         suma += i
#         media = suma / len(numero_lista)
#     return media

# print(f"Media: {media(numero_lista):.2f}") 


# numero_lista=[2.3, 5.7, 6.8, 9.7, 12.1, 15.6]

# def listas(numero_lista):
    
#     suma=0
#     for i in numero_lista:
#         suma += i
#         media = suma / len(numero_lista)

#     return media

# print(f"Media: {listas(numero_lista):.2f}")




# promedio_estudiante=[3.4,5,4.3,3.8,4.1]


# def promedio(promedio_estudiante):
#     suma=0

#     for i in promedio_estudiante:
#         suma += i
#         media = suma / len(promedio_estudiante)
#     return media

# print(f"Media: {promedio(promedio_estudiante):.2f}")        



# promedio_ventas=[30,40,50,60,80]

# def ventas_semana(promedio_ventas):
#     suma = 0

#     for i in promedio_ventas:
#         suma += i
#         media = suma / len(promedio_ventas)
#     return media

# print(f"Media ventas: {ventas_semana(promedio_ventas)}")        


# promedio=[1,2,3,4,5]

# def media(promedio):
#     suma = 0

#     for i in promedio:
#         suma += i
#         media = suma / len(promedio)
#     return media

# print(media(promedio))        


# def maximo_comun_divisor(numero1, numero2):
#     resto=0

#     while(numero2 > 0):
#         resto = numero2
#         numero2 = numero1 % numero2
#         numero1 = resto
#     return numero1

# def minimo_comun_multiplo(numero1,numero2):

#     if numero1 > numero2:
#         mayor = numero1
#     else:
#         mayor = numero2

#     while (mayor % numero1 != 0) or (mayor  % numero2 != 0 ):
#         mayor += 1
#     return mayor         

# print(f"Máximo común divisor: {maximo_comun_divisor(24,36)}")
# print(f"Mínimo común multiplo: {minimo_comun_multiplo(24,36)}")





# def maximo_comun_divisor(numero1,numero2):
#     resto=0

#     while(numero2 > 0):
#         resto = numero2
#         numero2 = numero1 % numero2
#         numero1 =  resto

#     return numero1


# def minimo_comun_multiplo(numero1,numero2):
#     if numero1 > numero2:
#         mayor_que = numero1
#     else:
#         mayor_que = numero2

#     while(mayor_que % numero1 != 0) or (mayor_que % numero2 != 0):
#         mayor_que += 1
#     return mayor_que

# print(f"Máximo común divisor: {maximo_comun_divisor(24,36)}")                   
# print(f"Mínimo común multiplo: {minimo_comun_multiplo(24,36)}")                   




# cuadrados=[1,2,3,4,5]

# def calcular_cuadrador(cuadrados):

#     for cuadrado in cuadrados:
#         resultado = cuadrado ** cuadrado
       
#     return resultado


# print(calcular_cuadrador(cuadrados))

# cuadrado=[1,2,3,4,5]
# # cuadrado=[2.3, 5.7, 6.8, 9.7, 12.1, 15.6]

# def cuadrados(cuadrado):

#     list=[]

#     for i in cuadrado:

#         list.append(i**2)

#     return list    

# print(f"Cuadrador {cuadrados(cuadrado)}")
# # print(f"Cuadrador {cuadrados(cuadrado)}")


# def square(*sample):
#     """Función que calcula los cuadrados de una lista de números.
#     Parámetros
#     *sample: Es una secuencia de números separados por comas.
#     Devuelve una lista con los cuadrados de los números de sample.
#     """
#     list = []
#     for i in sample:
#         list.append(i**2)
#     return list

# print(square(1, 2, 3, 4, 5))
# print(square(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))


# Escribir una función que reciba una muestra 
# de números en una lista y devuelva
#  otra lista con sus cuadrados.
# cuadrado=[1,2,3,4,5]

# def cuadrados(cuadrado):
#     lista=[]

#     for i in cuadrado:
#         resultado=i**2
#         lista.append(resultado)
#     return lista    

# print(f"Al cuadrado {cuadrados(cuadrado)}")




# cuadrado=[6,7,8,9,10]

# def cuadrados(cuadrado):
#     lista=[]

#     for i in cuadrado:
#         resultado = i ** 2
#         lista.append(resultado)
#     return lista

# print(f"Al cuadrdo: {cuadrados(cuadrado)}")        

# Escribir una función que reciba 
# una muestra de números en una 
# lista y devuelva un diccionario 
# con su media, varianza y desviación típica.


# numeros=[1,2,3,4,5]
# numeros1=[2.3, 5.7, 6.8, 9.7, 12.1, 15.6]

# def cuadrado(numeros):
#     lista=[]

#     for i in numeros:
#         resultado = i ** 2
#         lista.append(resultado)
#     return lista 

# def estidistica(numeros):

#     estadistica_valor={}
#     estadistica_valor["media"]=sum(numeros)/len(numeros)
#     estadistica_valor["varianza"]=sum(cuadrado(numeros))/len(numeros)-estadistica_valor["media"]**2
#     estadistica_valor["desviacion tipica"]=estadistica_valor["varianza"]**0.5
    
#     return estadistica_valor

# print(estidistica(numeros))   
# #  print(estidistica(numeros1))   

# media, varianza y desviación típica.


# numeros1=[1,2,3,4,5]
# numeros=[2.3, 5.7, 6.8, 9.7, 12.1, 15.6]

# def cuadrado(numeros):
#     lista=[]

#     for i in numeros:
#         resultado = i ** 2
#         lista.append(resultado)
#     return lista  

# def estadistica(numeros):

#     valor_estadistica={}
#     valor_estadistica["media"]= sum(numeros)/len(numeros)
#     valor_estadistica["varianza"]= sum(cuadrado(numeros))/len(numeros)-valor_estadistica["media"]**2
#     valor_estadistica["desviacion tipica"]= valor_estadistica["varianza"]/0.5
#     return valor_estadistica

# print(estadistica(numeros))



# media, varianza y desviación típica.
# numeros=[1,2,3,4,5]

# def cuadrado(numeros):
#     lista=[]

#     for i in numeros:
#         resultado = i ** 2
#         lista.append(resultado)
#     return lista


# def estadistica(numeros):

#     valor_estaditica={}
#     valor_estaditica["media"]= sum(numeros)/len(numeros)        
#     valor_estaditica["varianza"]= sum(cuadrado(numeros))/len(numeros)-valor_estaditica["media"]**2
#     valor_estaditica["desviacion tipica"] = valor_estaditica["varianza"]**0.5
#     return valor_estaditica

# print(estadistica(numeros))


# media, varianza y desviación típica.


# numeros=[10,20,30,40,50]

# def cuadrado(numeros):
#     lista=[]

#     for i in numeros:
#         resultado = i **2
#         lista.append(resultado)
#     return lista

# def estadistica(numeros):
#     valor_estadistica={}
#     valor_estadistica["media"]=sum(numeros)/len(numeros)
#     valor_estadistica["varianza"]=sum(cuadrado(numeros))/len(numeros)-valor_estadistica["media"]**2
#     valor_estadistica["desviacion tipica"]= valor_estadistica["varianza"]**0.5
#     return valor_estadistica

# print(estadistica(numeros))    




# media, varianza y desviación típica.

# numeros=[1,3,5,3,5,6]
# numeros=[1,2,4,3,5]

# def cuadrado(numeros):
#     lista=[]

#     for i in numeros:
#         resultado = i ** 2
#         lista.append(resultado)
#     return lista    

# def estaditica(numeros):
#     valor_estadistica={}
#     valor_estadistica["media"]=sum(numeros)/len(numeros)
#     valor_estadistica["varianza"]=sum(cuadrado(numeros))/len(numeros)-valor_estadistica["media"]**2
#     valor_estadistica["desviacion tipica"]= valor_estadistica["varianza"]**0.5
#     return valor_estadistica

# print(estaditica(numeros))    

# numero="10110"

# def numero_decimal(numero):
#     # lista=[]
#     numero = list(numero)
#     numero.reverse()
#     decimal = 0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal    

# def numero_binario(numero):
#     binario=[]
#     while numero > 0:
#         binario.append(str(numero % 2))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)

# print(numero_decimal('10110'))
# print(numero_binario(22))
# print(numero_decimal(numero_binario(22)))
# print(numero_binario(numero_decimal('10110')))                



# def decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0
#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal


# def bynario(numero):
#     binario=[]    
#     while numero > 0:
#         binario.append(str(numero % 2)) # devuelve el resto cero 0 o uno 1
#         numero //= 2 #  devuelve el resultado entero devuelve 11 en lugar de 11.0
#     binario.reverse()
#     return "".join(binario)


# print(decimal("110111"))
# print(bynario(22))
# print(decimal(bynario(22)))
# print(bynario(decimal("10110")))




# def numero_decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0
#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal   

# def numero_binario(numero):
#     binario=[]

#     while numero > 0: 
#         binario.append(str(numero % 2))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)

# print(numero_decimal("10110"))
# print(numero_binario(22))
# print(numero_decimal(numero_binario(22)))
# print(numero_binario(numero_decimal("10110")))     



# def num_decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i

#     return decimal

# def num_binario(numero):
#     binario=[]

#     while numero > 0:
#         binario.append(str(numero % 2))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)


# print(num_decimal("10110"))
# print(num_binario(22))
# print(num_decimal(num_binario(22)))
# print(num_binario(num_decimal("10110")))

# def decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal 

# def binario(numero):
#     binario=[]

#     while numero > 0:
#         binario.append(str(numero % 2))
#         numero //=2
#     binario.reverse()
#     return "".join(binario)   



# def decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal

# def binario(numero):
#     binario=[]

#     while numero > 0:
#         binario.append(str(numero % 2))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)            


# print(decimal("10110"))
# print(binario(22))
# print(decimal(binario(22)))
# print(binario(decimal("10110")))




# def decimal(numero):
#     numero= list(numero)
#     numero.reverse()
#     decimal=0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal

# def binario(numero):
#     binario=[]
#     while numero > 0:
#         binario.append(str(numero % 2 ))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)    


# print(decimal("10110"))
# print(binario(22))
# print(decimal(binario(22)))
# print(binario(decimal("10110")))

# def decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal

# def binario(numero):
#     binario=[]

#     while numero > 0:
#         binario.append(str(numero % 2 ))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)    

# print(decimal("10110"))
# print(binario(22))
# print(decimal(binario(22)))
# print(binario(decimal("10110")))




# def decimal(numero):
#     numero = list(numero)
#     numero.reverse()
#     decimal=0

#     for i in range(len(numero)):
#         decimal += int(numero[i]) * 2 ** i
#     return decimal

# def binario(numero):
#     binario=[]

#     while numero > 0:
#         binario.append(str(numero % 2))
#         numero //= 2
#     binario.reverse()
#     return "".join(binario)

# print(decimal("10110"))
# print(binario(22))
# print(decimal(binario(22)))
# print(binario(decimal("10110")))        














# Crear un programa que pida el nombre, la edad 
# y la altura de personas. Despues de cada ingreso de datos, 
# el programa deberá dar la opción para continuar o finalizar.
# Una vez que el usuario desee finalizar, el programa deberá 
# mostrar el siguiente resumen.

# • Nombre de la persona de mayor edad.
# • Edad promedio.
# • Nombre de la persona de menor estatura.
# • Estatura promedio de todas las personas ingresadas.
# • Cantidad de personas menores a 15 años que midan
# más de 1.70 metros.

# Si me ayudan a resolverlo sería de gran ayuda

# edad=[3,4,5,6]

# datos_personas={}
# menu="S"

# while menu != "N":

#     nombre=input("Ingrese nombre: ")
#     edad=int(input("Ingrese edad: "))
#     estatura=float(input("Ingrese estatura: "))
#     menu=input("Continuar (S/N) ").upper()

#     persona={
#         "nombre": nombre,
#         "edad": edad,
#         "estatura": estatura
#     }

#     datos_personas[nombre]=persona

#     if menu == "N":
#     #   print(datos_personas["nombre"])

#         # for persona in datos_personas.values():
#         #     edades = [persona["edad"]] 
#         edades = [persona["edad"] for persona in datos_personas.values()]

#         if len(edades) > 0:

#             promedio_edad = sum(edades)/len(edades)
#             print(f"Edad promedio: {promedio_edad}")

#             persona_mayor = max(edades)
#             print(f"La persona de mayor edad es: {persona_mayor}")

#             menor_edad = min(edades)
#             print(f"La persona menor es: {menor_edad}")


    # print("Continuar (S/N) ")
    # menu=input().upper()

    
# def main():
#     personas = []
#     continuar = 'S'

#     while continuar.upper() == 'S':
#         nombre = input("Ingresa el nombre: ")
#         edad = int(input("Ingresa la edad: "))
#         estatura = float(input("Ingresa la estatura (en metros): "))
        
#         personas.append({
#             "nombre": nombre,
#             "edad": edad,
#             "estatura": estatura
#         })
        
#         continuar = input("¿Deseas ingresar otra persona? (S/N): ")

#     if personas:
#         # Persona de mayor edad
#         persona_mayor_edad = max(personas, key=lambda p: p["edad"])
        
#         # Edad promedio
#         edad_promedio = sum(p["edad"] for p in personas) / len(personas)
        
#         # Persona de menor estatura
#         persona_menor_estatura = min(personas, key=lambda p: p["estatura"])
        
#         # Estatura promedio
#         estatura_promedio = sum(p["estatura"] for p in personas) / len(personas)
        
#         # Cantidad de personas menores de 15 años y más de 1.70 metros
#         personas_menores_15_y_altas = len([p for p in personas if p["edad"] < 15 and p["estatura"] > 1.70])
        
#         # Mostrar el resumen
#         print("\nResumen:")
#         print(f"• Persona de mayor edad: {persona_mayor_edad['nombre']} con {persona_mayor_edad['edad']} años.")
#         print(f"• Edad promedio: {edad_promedio:.2f} años.")
#         print(f"• Persona de menor estatura: {persona_menor_estatura['nombre']} con {persona_menor_estatura['estatura']} metros.")
#         print(f"• Estatura promedio: {estatura_promedio:.2f} metros.")
#         print(f"• Cantidad de personas menores de 15 años que miden más de 1.70 metros: {personas_menores_15_y_altas}.")
#     else:
#         print("No se ingresaron personas.")

# if __name__ == "__main__":
#     main()



# datos_personas={}
# menu="S"
# personas_menores_15_y_altas=0
# # personas_altas=0

# while menu != "N":

#     nombre=input("Ingrese nombre: ").title()
#     edad=int(input("Ingrese edad: "))
#     estatura=float(input("Ingrese estatura: "))

#     persona={
#         "edad": edad, 
#         "estatura": estatura
#     }

#     datos_personas[nombre] = persona

#     if edad < 18 and estatura > 1.70:
#         personas_menores_15_y_altas +=1
#         # personas_altas +=1

#     menu=input("¿Desea continuar (S/N) ").upper()  

# # Función para calcular el máximo basado en la edad
# def persona_mayor(datos):
#     persona_mayor=None
#     mayor_edad = -1

#     for nombre, datos_persona in datos.items():
#         if datos_persona["edad"] > mayor_edad:
#             mayor_edad = datos_persona["edad"]
#             persona_mayor = nombre
#     return persona_mayor   

# # Función para calcular el mínimo basado en la estatura
# def menor_estatura(datos):
#     persona_menor= None
#     menor_estatura= float("inf")  

#     for nombre, datos_persona  in datos.items():
#         if datos_persona["estatura"] < menor_estatura:
#             menor_estatura = datos_persona["estatura"]
#             persona_menor = nombre
#     return persona_menor              

# #Sumar edades
# def sumar_edades(datos):
#     total=0

#     for datos_persona in datos.values():
#         total += datos_persona["edad"]
#     return total

# #suamr estatura
# def sumar_estaturas(datos):
#     total=0

#     for datos_persona in datos.values():
#         total += datos_persona["estatura"]
#     return total            


# if menu == "N":
#     if datos_personas:
#         persona_mayor = persona_mayor(datos_personas)

#         total_edades = sumar_edades(datos_personas)
#         promedio_edad = total_edades / len(datos_personas)

#         menor_estatura = menor_estatura(datos_personas)

#         total_estatura = sumar_estaturas(datos_personas)
#         promedio_estatura = total_estatura / len(datos_personas)

#         print("\nResumen:")
#         print(f"• Nombre de la persona de mayor edad: {persona_mayor}")
#         print(f"• Edad promedio: {promedio_edad:.1f} años")
#         print(f"• Nombre de la persona de menor estatura: {menor_estatura}")
#         print(f"• Estatura promedio: {promedio_estatura:.2f} metros")
#         print(f"• Cantidad de personas menores a 15 años y con estatura mayor a 1.70 metros: {personas_menores_15_y_altas}")
#     else:
#         print("No se ingresaron datos.")

        
##########################

# Datos Estudiante:

# datos_estudiantes={}
# menu="S"
# estudiantes_menores_30_mejor_promedio=0


# while menu != "N":

#     nombre=input("Ingrese nombre estudiante: ").title()
#     edad=int(input("Ingrese edad: "))
#     promedio=float(input("Ingrese promedio: "))

#     estudiante={
#         "edad": edad,
#         "promedio": promedio
#     }

#     datos_estudiantes[nombre]=estudiante


#     if edad < 30 and promedio > 4.50:
#         estudiantes_menores_30_mejor_promedio += 1


#     menu=input("¿Desea continuar (S/N) ").upper()    


#     def estudiante_mayor(datos):
#         estudiante_mayor=None
#         mayor_edad = -1

#         for nombre, datos_estudiante in datos_estudiantes.items():
#             if datos_estudiante["edad"] > mayor_edad:
#                 mayor_edad = datos_estudiante["edad"]
#                 estudiante_mayor = nombre
#         return estudiante_mayor        


# def menor_promedio(datos):
#     estudiante_menor=None
#     menor_promedio= float("inf")

#     for nombre, datos_estudiante in datos_estudiantes.items():
#         if datos_estudiante["promedio"] < menor_promedio:
#             menor_promedio = datos_estudiante["promedio"]
#             estudiante_menor = nombre
#     return estudiante_menor


# def sumar_edades(datos):
#     total=0

#     for datos_estudiante in datos_estudiantes.values():
#         total += datos_estudiante["edad"]
#     return total


# def sumar_promedios(datos):
#     total=0

#     for datos_estudiante in datos_estudiantes.values():
#         total += datos_estudiante["promedio"]
#     return total


# if menu == "N":
#     if datos_estudiantes:

#         estudiante_mayor = estudiante_mayor(datos_estudiantes)

#         total_edades = sumar_edades(datos_estudiantes)
#         promedio_edad = total_edades / len(datos_estudiantes)

#         menor_promedio = menor_promedio(datos_estudiantes)

#         total_promedios = sumar_promedios(datos_estudiantes)
#         promedio_notas = total_promedios / len(datos_estudiantes)

#         print("\nResumen:")
#         print(f"• Nombre de la persona de mayor edad: {estudiante_mayor}")
#         print(f"• Edad promedio: {promedio_edad:.1f} años")
#         print(f"• Nombre de la persona de menor promedio: {menor_promedio}")
#         print(f"• Promedio notas: {promedio_notas:.2f}")
#         print(f"• Cantidad de personas menores a 30 años y con promedio mayor a 4.5: {estudiantes_menores_30_mejor_promedio}")
#     else:
#         print("No se ingresaron datos.")


# datos_estudiantes={}
# menu="S"
# estudiantes_mayor_30__mejor_promedio=0


# while menu !="N":

#     nombre=input("Ingrese su nombre: ").title()
#     edad=int(input("Ingrese su edad: "))
#     promedio=float(input("Ingrese su promedio: "))

#     estudiante={
#         "edad": edad,
#         "promedio": promedio
#     }

#     datos_estudiantes[nombre]=estudiante


#     if edad > 30 and promedio > 4.6:
#         estudiantes_mayor_30__mejor_promedio += 1


#     menu=input("¿Desea continuar? (S/N) ").upper()   


# def estudiante_mayor(datos):
#     estudiante_mayor=None
#     mayor_estudiante=-1

#     for nombre, datos_estudiante in datos_estudiantes.items():

#         if datos_estudiante["edad"] > mayor_estudiante:
#             mayor_estudiante = datos_estudiante["edad"]
#             estudiante_mayor = nombre
#         return estudiante_mayor    

# def menor_promedio(datos):
#     estudiante_menor_promedio=None
#     menor_promedio=float("inf")

#     for nombre, datos_estudiante in datos_estudiantes.items():
#         if datos_estudiante["promedio"] < menor_promedio:
#             menor_promedio = datos_estudiante["promedio"]
#             estudiante_menor_promedio = nombre
#     return estudiante_menor_promedio


# def sumar_edades_estudiantes(datos):
#     total=0

#     for datos_estudiante in datos_estudiantes.values():
#         total += datos_estudiante["edad"]
#     return total


# def sumar_promedio_estudiantes(datos):      
#     total=0

#     for datos_estudiante in datos_estudiantes.values():
#         total += datos_estudiante["promedio"]
#     return total  


# if menu == "N":
#     if datos_estudiantes:

#         estudiante_mayor = estudiante_mayor(datos_estudiantes)

#         total_edades_estudiantes = sumar_edades_estudiantes(datos_estudiantes)
#         promedio_edad_estudiantes = total_edades_estudiantes / len(datos_estudiantes)

#         menor_promedio = menor_promedio(datos_estudiantes)

#         total_promedio_estudiantes = sumar_promedio_estudiantes(datos_estudiantes)
#         promedio_estudiantes = total_edades_estudiantes / len(datos_estudiantes)

#         print("\nResumen:")
#         print(f"• Nombre del estudiante de mayor edad: {estudiante_mayor}")
#         print(f"• Edad promedio: {promedio_edad_estudiantes:.1f} años")
#         print(f"• Nombre del estudiante de menor promedio: {menor_promedio}")
#         print(f"• Promedio notas: {promedio_estudiantes:.2f}")
#         print(f"• Cantidad de personas mayores de 30 años y con promedio mayor a 4.60: {estudiantes_mayor_30__mejor_promedio}")
#     else:
#         print("No se ingresaron datos.")

###########################




# datos_carros={}
# menu="S"
# carros_2024_Y_mayor_hp=0


# while menu != "N":

#     marca_carro=input("Ingrese marca vehículo: ").title()
#     anio_carro=int(input("Ingrese año vehículo: "))
#     hp_carro=float(input("Ingrese potencia vehículo: "))

#     datos_carro={
#         "anio_carro": anio_carro,
#         "hp_carro": hp_carro
#     }

#     datos_carros[marca_carro]=datos_carro


#     if anio_carro > 2022 and hp_carro > 250:
#         carros_2024_Y_mayor_hp += 1

#     menu=input("¿Desea contionuar (S/N)? ").upper()

# def carro_mas_reciente(carros_dato):
#     carro_mas_nuevo=None
#     mas_nuevo=-1

#     for marca, datos_carro in datos_carros.items():

#         if datos_carro["anio_carro"] > mas_nuevo:
#             mas_nuevo = datos_carro["anio_carro"]
#             carro_mas_nuevo = marca
#         return carro_mas_nuevo    

# def carro_menor_potencia(carros_dato):
#     menor_potencia_carro=None
#     menor_potencia=float("inf")

#     for marca, datos_carro in datos_carros.items():

#         if datos_carro["hp_carro"] < menor_potencia:
#             menor_potencia= datos_carro["hp_carro"]
#             menor_potencia_carro = marca

#     return menor_potencia_carro    

# def carro_anios(carros_dato):
#     total=0

#     for datos_carro in datos_carros.values():
#         total += datos_carro["anio_carro"]
#     return total

# def carro_potencia_promedio(datos_carro):
#     total=0

#     for datos_carro in datos_carros.values():
#         total += datos_carro["hp_carro"]
#     return total

# if menu == "N":
#     if datos_carros:

#         carro_mas_reciente = carro_mas_reciente(datos_carros)

#         total_carro_anios_marca = carro_anios(datos_carros)   
#         promedio_anio_carro = total_carro_anios_marca / len(datos_carros)

#         carro_menor_potencia = carro_menor_potencia(datos_carros)

#         total_carros_promedio_hp = carro_potencia_promedio(datos_carros)
#         carro_hp_promedio = total_carros_promedio_hp / len(datos_carros)

#         print("\nResumen:")
#         print(f"• Nombre de la marca del vehículo más nuevo: {carro_mas_reciente}")
#         print(f"• Promedio año carro: {promedio_anio_carro:.0f}")
#         print(f"• Marca vehículo menor potencia: {carro_menor_potencia}")
#         print(f"• Promedio potencia: {carro_hp_promedio:.1f} hp")
#         print(f"• Cantidad de vehiculos del 2023 al 2024 y con potencia mayor a 250 hp: {carros_2024_Y_mayor_hp}")
#     else:
#         print("No se ingresaron datos.")








##################################


# datos_empleados={}
# menu="S"
# mejor_empleado_mejores_ventas=0

# while menu != "N":

#     nombre=input("Ingrese nombre empleado: ").title()
#     codigo=int(input("Ingrese ranking empleado: "))
#     ventas=float(input("Ingrese total ventas último mes: "))

#     datos_empleado={
#         "codigo": codigo,
#         "ventas": ventas
#     }

#     datos_empleados[nombre]=datos_empleado

#     if codigo < 20 and ventas > 100:
#         mejor_empleado_mejores_ventas += 1

#     menu=input("¿Desea continuar (S/N)? ").upper() 

# def empleado_mejor_ranking(empleados_datos):

#     nombre_mejor_ranking=None
#     numero_ranking=-1

#     for nombre, datos_empleado in datos_empleados.items():

#         if datos_empleado["codigo"] > numero_ranking:
#             numero_ranking = datos_empleado["codigo"]
#             nombre_mejor_ranking = nombre
#         return nombre_mejor_ranking  

# def empleado_menor_venta(empleados_datos):
#     nombre_empledado_menor_venta=None
#     cantidad_venta=float("inf")

#     for nombre, datos_empleado in datos_empleados.items():

#         if datos_empleado["ventas"] < cantidad_venta:
#             cantidad_venta = datos_empleado["ventas"]
#             nombre_empledado_menor_venta = nombre    

#     return nombre_empledado_menor_venta

# def empleado_codigo(empleados_datos):
#     total=0

#     for datos_empleado in datos_empleados.values():
#         total += datos_empleado["codigo"]
#     return total

# def empleados_promedio_ventas(empleados_datos):
#     total=0

#     for datos_empleado in datos_empleados.values():
#         total += datos_empleado["ventas"] 
#     return total

# if menu == "N":
#     if datos_empleados:

#         empleado_mejor_ranking = empleado_mejor_ranking(datos_empleados)

#         total_codigo_empleados = empleado_codigo(datos_empleados)
#         promedio_codigo= total_codigo_empleados / len(datos_empleados)

#         empleado_menor_venta = empleado_menor_venta(datos_empleados)

#         total_promedio_ventas = empleados_promedio_ventas(datos_empleados)
#         empleado_mejor_promedio = total_promedio_ventas / len(datos_empleados)


#         print("\nResumen:")
#         print(f"• Nombre del mejor empleado: {empleado_mejor_ranking}")
#         print(f"• Promedio ranking: {promedio_codigo:.0f}")
#         print(f"• Empleado con menores ventas: {empleado_menor_venta}")
#         print(f"• Promedio ventas: {empleado_mejor_promedio:.1f}")
#         print(f"• Cantidad de empleados con mejor ranking y más ventas: {mejor_empleado_mejores_ventas}")
#     else:
#         print("No se ingresaron datos.")





# #####################

# categoria_productos={}
# menu="S"
# mas_vendido_mas_costoso=0

# while menu != "N":

#     producto=input("Ingrese producto: ").title()
#     cantidad=int(input("Cantidad de productos vendidos: "))
#     venta=float(input("Ventas totales mes: "))

#     categoria_producto={
#         "cantidad": cantidad,
#         "venta": venta
#     }

#     categoria_productos[producto]=categoria_producto

#     if venta > 500 and cantidad > 100:
#         mas_vendido_mas_costoso += 1

#     menu=input("¿Desea continuar (S/N)? ").upper()

# def producto_mas_vendido(productos):     
#     nombre_mas_vendido=None
#     mas_vendido=-1

#     for nombre, categoria_producto in categoria_productos.items():
#         if categoria_producto["cantidad"] > mas_vendido:
#             mas_vendido = categoria_producto["cantidad"]
#             nombre_mas_vendido=nombre
#     return nombre_mas_vendido    

# def producto_menor_venta(productos):
#     nombre_menos_vendido=None
#     menos_vendido=float("inf")

#     for nombre, categoria_producto in categoria_productos.items():
#         if categoria_producto["venta"] < menos_vendido:
#            menos_vendido=categoria_producto["venta"]
#            nombre_menos_vendido=nombre
#     return nombre_menos_vendido        

# def productos_cantidad(productos):
#     total=0

#     for categoria_producto in categoria_productos.values():
#         total+=categoria_producto["cantidad"]
#     return total    


# def productos_promedio(productos):
#     total=0

#     for categoria_producto in categoria_productos.values():
#         total+=categoria_producto["venta"]
#     return total

# if menu == "N":
#     if categoria_productos:

#         producto_mas_vendido= producto_mas_vendido(categoria_productos)

#         total_cantidad_productos = productos_cantidad(categoria_productos)
#         promedio_cantidades=total_cantidad_productos / len(categoria_productos)

#         producto_menor_venta = producto_menor_venta(categoria_productos)

#         total_ventas_promedio = productos_promedio(categoria_productos)
#         producto_mejor_promedio = total_ventas_promedio / len(categoria_productos)

#         print("\nResumen:")
#         print(f"• Producto más vendido: {producto_mas_vendido}")
#         print(f"• Promedio de productos vendidos: {promedio_cantidades:.0f}")
#         print(f"• Producto con menores ventas: {producto_menor_venta}")
#         print(f"• Promedio ventas: {producto_mejor_promedio:.1f}")
#         print(f"• Producto con mejor venta y más cantidad: {mas_vendido_mas_costoso}")
#     else:
#         print("No se ingresaron datos.")


#####################



# estudiantes_listas={}
# menu="S"
# menor_edad_mejor_promedio=0

# while menu != "N":

#     estudiante=str(input("Ingrese nombre estudiante: ")).title()
#     edad=int(input("Ingrese edad estudiante: "))
#     promedio=float(input("Ingrese promedio estudiante: "))


#     estudiante_lista={
#         "edad": edad,
#         "promedio": promedio
#     }

#     estudiantes_listas[estudiante]=estudiante_lista

#     if edad < 25 and promedio > 4.5:
#         menor_edad_mejor_promedio += 1

#     menu=str(input("¿Desea constinuar (S/N)? ")).upper()

# def  estudiante_mejor(datos_estudiantes):
#      nombre_estudiante_edad=None
#      estudiante_mayor=-1

#      for nombre, datos_estudiante in estudiantes_listas.items():
#         if datos_estudiante["promedio"] > estudiante_mayor:
#             estudiante_mayor = datos_estudiante["promedio"]
#             nombre_estudiante_edad = nombre
#      return nombre_estudiante_edad

# def  estudiante_edad(datos_estudiantes):
#     nombre_promedio_estudiante=None
#     estudiante_menor_promedio=float("inf")  

#     for nombre, datos_estudiante in estudiantes_listas.items():
#         if datos_estudiante["promedio"] < estudiante_menor_promedio:
#             estudiante_menor_promedio= datos_estudiante["promedio"]
#             nombre_promedio_estudiante=nombre
#     return nombre_promedio_estudiante

# def promedio_edad(datos_estudiante):
#     total=0

#     for datos_estudiantes in estudiantes_listas.values():
#         total+= datos_estudiantes["edad"]
#     return total    

# def promedio_notas(datos_estudiante):
#     total=0

#     for datos_estudiantes in estudiantes_listas.values():
#         total += datos_estudiantes["promedio"]
#     return total

# if menu == "N":

#     if estudiantes_listas:

#         estudiante_mejor=estudiante_mejor(estudiantes_listas)

#         total_promedio_edad=promedio_edad(estudiantes_listas)
#         promedio_edades=total_promedio_edad/len(estudiantes_listas)

#         estudiante_edad=estudiante_edad(estudiantes_listas)

#         total_promedio=promedio_notas(estudiantes_listas)
#         mejor_estudiante=total_promedio/len(estudiantes_listas)

#         print("\nResumen:")
#         print(f"• Estudiante con mejor promedio: {estudiante_mejor}")
#         print(f"• Edad promedio de estudiantes: {promedio_edades:.0f}")
#         print(f"• Estudiante menor promedio: {estudiante_edad}")
#         print(f"• Promedio notas: {mejor_estudiante:.1f}")
#         print(f"• Cantidad de estudiantes menores y con mejor promedio: {menor_edad_mejor_promedio}")
#     else:
#         print("No se ingresaron datos.")

# def contador_palabras(texto):
#     texto=texto.split()
#     palabras={}

#     for i in texto:
#         if i in palabras:
#             palabras[i]+=1
#         else:
#             palabras[i] = 1

#     return palabras            


# def palabra_mas_repetida(palabras):
    
#     max_palabra=""
#     max_palabra_frecuente=0

#     for palabra, frecuencia in palabras.items():

#         if frecuencia > max_palabra_frecuente:
#             max_palabra = palabra
#             max_palabra_frecuente = frecuencia

#     return max_palabra, max_palabra_frecuente        

# # texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
# texto = "tres tristes tigres comian trigo en tres tristes platos, sentados en un trigal sentados en un trigal en tres tristes platos, comian trigo tres tristes tigres"
# print(f"Contador palabras: {contador_palabras(texto)}")
# print(f"Palabras más repetida: {palabra_mas_repetida(contador_palabras(texto))}")




##COntador palabras

# def contador_word(text):
#     text=text.split()
#     diccionario={}

#     for i in text:
#         if i in diccionario:
#             diccionario[i] += 1
#         else:
#             diccionario[i] = 1

#     return diccionario

# def contador_total_words(text):

#     max_palabras=""
#     max_frecuencia=0

#     for palabra, frecuencia in text.items():
#         if frecuencia > max_frecuencia:
#             max_palabras = palabra
#             max_frecuencia = frecuencia
#     return max_palabras, max_frecuencia


# text = "tres tristes tigres comian trigo en tres tristes platos, sentados en un trigal sentados en un trigal en tres tristes platos, comian trigo tres tristes tigres".title()
# print(f"Contador palabras: {contador_word(text)}")
# print(f"Palabras más repetida: {contador_total_words(contador_word(text))}")




#CONTADOR WORDS AND LETTERS

# def contador_palabras(texto):
#     texto=texto.split()
#     palabras={}

#     for i in texto:
#         if i in palabras:
#             palabras[i] +=  1
#         else:
#             palabras[i] = 1

#     return palabras

# def  contador_frecuencia_palabras(texto):

#         max_palabra=""
#         max_frecuencia=0

#         for palabra, frecuencia in texto.items():
#             if frecuencia > max_frecuencia:
#                 max_palabra = palabra
#                 max_frecuencia = frecuencia
#         return max_palabra, max_frecuencia        


# texto = "tres tristes tigres comian trigo en tres tristes platos, sentados en un trigal sentados en un trigal en tres tristes platos, comian trigo tres tristes tigres".title()
# print(f"Contador palabras: {contador_palabras(texto)}")
# print(f"Palabras más repetida: {contador_frecuencia_palabras(contador_palabras(texto))}")



#CONTADOR PALABRAS Y MAX PALABRA



# def contador_palabras(texto):
#     texto=texto.split()
#     palabras={}

#     for i in texto:
#         if i in palabras:
#             palabras[i] += 1
#         else:
#             palabras[i] = 1
#     return palabras

# def contador_frecuencia_palabras(texto):
#     max_palabra=""
#     max_frecuencia=0

#     for palabra, frecuencia in texto.items():
#         if frecuencia > max_frecuencia:
#             max_palabra = palabra
#             max_frecuencia = frecuencia

#     return max_palabra, max_frecuencia

  
# texto = "tres tristes tigres comian trigo en tres tristes platos, sentados en un trigal sentados en un trigal en tres tristes platos, comian trigo tres tristes tigres".title()
# print(f"Contador palabras: {contador_palabras(texto)}")
# print(f"Palabras más repetida: {contador_frecuencia_palabras(contador_palabras(texto))}")





#CONTADOR PALABRAS AND FRECUENCIA PALABRAS


# def contador_palabras(texto):
#     texto=texto.split()
#     palabras={}

#     for i in texto:
#         if i in palabras:
#             palabras[i] += 1
#         else:
#             palabras[i] = 1
#     return palabras

# def contador_frecuencia_palabras(texto):
#     max_palabra=""
#     max_frecuencia=0

#     for palabra, frecuencia in texto.items():
#         if frecuencia > max_frecuencia:
#             max_palabra = palabra
#             max_frecuencia = frecuencia      
#         return max_frecuencia,max_palabra

 
# texto = "tres tristes tigres comian trigo en tres tristes platos, sentados en un trigal sentados en un trigal en tres tristes platos, comian trigo tres tristes tigres".title()
# print(f"Contador palabras: {contador_palabras(texto)}")
# print(f"Palabras más repetida: {contador_frecuencia_palabras(contador_palabras(texto))}")





#PROGRAMAICÓN FUNCIONAL

# precio=0
# porcentaje=0

# lista={
#     "precio": precio,   
#     "procentaje": porcentaje   
#         }


# def descuento(precio):

#         descuento=10
#         precio =  precio - descuento 

#         return precio

# def iva(precio):

#         iva=0.005
#         precio =  precio + (precio * iva)

#         return precio   

# def compras(lista):
        
#         for precio, iva in lista.items():
#                 print(precio)
#                 print(iva)
        
       

# print(descuento(100))
# print(iva(100))
# print(compras(lista))

# def aplicar_descuento(precio, descuento):
#      precio = precio - precio * descuento / 100
#      return precio

# def aplicar_iva(precio, procentaje_iva):
#      precio = precio + precio * procentaje_iva / 100
#      return precio

# def precio_cesta(cesta, funcion):
#     total=0

#     for precio, iva_o_descuento in cesta.items():
#           total += funcion(precio, iva_o_descuento)
#     return total


# print('El precio de la compra tras aplicar los descuentos es: ', precio_cesta({1000:20, 500:10, 100:1}, aplicar_descuento))
# print('El precio de la compra tras aplicar el IVA es: ', precio_cesta({1000:20, 500:10, 100:1}, aplicar_iva))




# #DEscuento

# def descuento(precio,descuento):
#      precio = precio - precio * descuento / 100
#      return precio

# def iva(precio, iva):
#      precio = precio + precio * iva / 100
#      return precio

# def cesta(pedido, descuento):
#      total=0

#      for precio, apliacar_iva in pedido.items():
#           total*= descuento(precio, apliacar_iva)
#      return total

# print('El precio de la compra tras aplicar los descuentos es: ', precio_cesta({1000:20, 500:10, 100:1}, aplicar_descuento))
# print('El precio de la compra tras aplicar el IVA es: ', precio_cesta({1000:20, 500:10, 100:1}, aplicar_iva))
    



# def aplicar_descuento(precio, descuento):
#      precio = precio - precio * descuento / 100
#      return precio

# def aplicar_iva(precio, iva):
#      precio = precio + precio * iva / 100
#      return precio

# def precio_pedido(productos, funcion):
#      total=0

#      for precio, iva_o_descuento in productos.items():
#           total+= funcion(precio, iva_o_descuento)
#      return total

# print('El precio de la compra tras aplicar los descuentos es: ', precio_pedido({1000:20, 500:10, 100:1}, aplicar_descuento))
# print('El precio de la compra tras aplicar el IVA es: ', precio_pedido({1000:20, 500:10, 100:1}, aplicar_iva))



# #PEdidio tienda

# def precio_descuento(precio, descuento):
#      precio = precio - precio * descuento / 100
#      return precio

# def precio_iva(precio, iva):
#      precio = precio + precio * iva / 100
#      return precio

# def productos_pedido(productos, impuestos):
#      total =0

#      for precio, iva_o_descuento in productos.items():
#             total+= impuestos(precio, iva_o_descuento)
#      return total

# print(f"Precio descuento: {productos_pedido({100:20,500:40,40:15}),precio_descuento}")
# print(f"Precio descuento: {productos_pedido({100:20,500:40,40:15}),precio_iva}")

# print(f"Precio con descuento: {productos_pedido({100: 20, 500: 40, 40: 15}, precio_descuento)}") 
# print(f"Precio con IVA: {productos_pedido({100: 20, 500: 40, 40: 15}, precio_iva)}")



# ##IVA DESCUENTO EN COMPRA

# def precio_descuento(precio, descuento):
#       precio = precio - precio * descuento / 100
#       return precio

# def precio_iva(precio, iva):
#       precio = precio + precio * iva / 100
#       return precio

# def productos_compra(productos, impuestos):
#       total =0

#       for precio, iva_o_descuento in productos.items():
#           total += impuestos(precio, iva_o_descuento)
#           return total

# print(f"Precio con descuento: {productos_compra({2340:30, 300:40, 3426:25}, precio_descuento)}")        
# print(f"Precio con IVA: {productos_compra({2340:19, 300:5, 3426:1}, precio_iva)}")        



#DEscuendo y IVA
# 
# def precio_descuento(precio, descuento):
#       precio = precio - precio * descuento / 100
#       return precio

# def precio_iva(precio, iva):
#       precio = precio + precio * iva / 100
#       return precio

# def producto_compra(producto, impuestos):
#       total=0
#       for precio, iva_o_descuento in producto.items():
#             total+= impuestos(precio, iva_o_descuento)
#       return total

# print(f"PRecio con descuento: {producto_compra({400:10},precio_descuento)}")      
# print(f"Precio con IVA: {producto_compra({400:10},precio_iva)}")      


#CALCULADORA CIENTÍFICA

# calcular el seno, 
# coseno, tangente, 
# exponencial y logaritmo neperiano.


# menu=True

# def seno(valor):
#     resultado = math.sin(valor)
#     return resultado

# def coseno(valor):
#     resultado= math.cos(valor)   
#     return resultado 

# def tangente(valor):
#     resultado= math.tan(valor)
#     return resultado

# def exponencial(valor):
#     resultado= math.exp(valor)
#     return resultado

# def neperiano(valor):
#     resultado = math.log(valor)
#     return resultado

# while menu != 6:
# # calcular el seno, 
# # coseno, tangente, 
# # exponencial y logaritmo neperiano.
#     valor=float(input("Ingrese un valor: "))
#     print("1 - SENO.")
#     print("2 - COSENO")
#     print("3 - TANGENTE")
#     print("4 - EXPONENCIAL")
#     print("5 - NEPERIANO")
#     print("6 - SALIR")
#     menu=int(input("¿Cuál función desea aplicar? "))
   
    
#     if menu == 1:
#         resultado = seno(valor)
#         print(f"Resultado: {resultado}")

#     if menu == 2:
#         resultado = coseno(valor)
#         print(resultado)

#     if menu == 3:
#         resultado = tangente(valor)
#         print(f"Resultado: {resultado}")

#     if menu == 4:
#         resultado = exponencial(valor)
#         print(resultado) 

#     if menu == 5:
#         resultado = neperiano(valor)
#         print(f"Resultado: {resultado}")

#     if menu == 6:
#         break     
            

# def aplicar_funcion(calcula, numero_entero):

#     funcion = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
#     resultado = {}
#     for i in range(1, numero_entero + 1):
#         resultado[i] = funcion[calcula][i]
#     return resultado    

# def culcular():
#     calculo=input("¿cual función desea aplicar (sin, cos, tan, exp, log)? ").lower()
#     numero=int(input("Número entero positivo: ")) 

#     for valor, funcion_hacer in aplicar_funcion(calculo, numero).items():
#         print(f" {valor} \t {funcion_hacer}")
#     return

# culcular()       


# from math import sin, cos, tan, exp, log

# def apply_function(f, n):
#     '''
#     Función que aplica una función a los enteros desde 1 hasta n.
#     Parámetros:
#         f: Es una función que recibe un número real y devuelve otro.
#         n: Es un número entero positivo.
#     Devuelve:
#         Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
#     '''
#     functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
#     result = {}
#     for i in range(1, n+1):
#         result[i] = functions[f](i)
#     return result

# def calculator():
#     '''
#     Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. 
#     Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
#     Parámetros:
#         f: Es una cadena con la función a aplicar (sin, cos, tan, exp o log).
#         n: Es un entero positivo.
#     '''
#     f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
#     n = int(input('Introduce un entero positivo: '))
#     for i, j in apply_function(f, n).items():
#         print (i, '\t', j)
#     return

# calculator()





#CALCULADORA CIENTIFICA

# def aplicar_algortimo(calculador, numero_entero):
#     funcion={'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
#     resultado={}

#     for i in range(1, numero_entero):
#         resultado[i]=funcion[calculador](i)
#     return resultado

# def calcular():
#     calculo=input("función que desea realizar (sin, cos, tan, exp, log) ").lower()
#     numero=int(input("Número entero positivo: "))

#     for valor, funcion_hacer in aplicar_algortimo(calculo, numero).items():
#         print(f"{valor} {funcion_hacer}")
#     return

# calcular()            






# def aplicar_algoritmos(calcular, numero_entero):
#     funcion={'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
#     resultado={}

#     for i in range(1, numero_entero):
#         resultado[i]=funcion[calcular](i)
#     return resultado

# def calcular():
#     calculo=input("Función a realizar: (sin, cos, tan, exp, log) ").lower()
#     numero=int(input("Número entero: "))

#     for valor, funcion_hacer in aplicar_algoritmos(calculo, numero).items():
#         print(f"{valor} {funcion_hacer}")
#     return    

# calcular()



#list

# 

# numeros_lista=[1,2,3,4]

# def aplicar_funcion_lista(funcion, listas):

#     lista=[]

#     for i in listas:
#         lista.append(funcion(i))

#     return lista    

# def cuadrado(numero):
#     numero =  numero * numero  
#     return  numero

# print(f"Resultado:  { aplicar_funcion_lista(cuadrado, numeros_lista)}")




#

# numero_lista=[10,20,30,45,]


# def aplicar_funcion(funcion, numero):
#     lista=[]

#     for i in numero:
#         lista.append(funcion(i))

#     return lista

# def multiplicar(numero):

#     numero = numero * numero
#     return numero

# print(f"Resultado: {aplicar_funcion(multiplicar, numero_lista)}")    





#r

# numeros=[1,2,3,4,5]

# def aplicar_funcion(funcion, numeros):

#     lista=[]

#     for i in numeros:
#         lista.append(funcion(i))

#     return lista 

# def multiplicar(numero):
#     numero = numero  * numero
#     return numero

# print(f"Resultado: {aplicar_funcion(multiplicar, numeros)}")   




# numeros_lista=[1,2,3,4]

# def aplicar_funcion(funcion, listas):

#     lista=[]

#     for i in listas:
#         lista.append(funcion(i))
#     return lista

# def multiplicar(numero):
#     numero = numero * numero
#     return numero


# print(f"{aplicar_funcion(multiplicar, numeros_lista)}")



# lista_numero=[726,464,8,9]

# def aplicar_funcion(funcion, lista):

#     nueva_lista=[]

#     for i in lista:
#         nueva_lista.append(funcion(i))
#     return nueva_lista

# def multilicar(numero):
#     numero = numero * numero
#     return numero

# resultado = aplicar_funcion(multilicar, lista_numero)    

# for resulta in resultado:
#     print(f"Resultado: {resulta }")


# print(f"Resultado: {aplicar_funcion(multilicar, lista_numero)}")


# lista_division=[4,5,6,7]

# def aplicar_funcion(funcion, numeros_lista):

#     lista=[]

#     for i in numeros_lista:
#         lista.append(funcion(i))
#     return lista

# def division(numero):
#     numero = numero / numero   
#     return numero


# print(f"Resultado {aplicar_funcion(division, lista_division) }")







# lista_resta=[6,5,7,88,9]

# def aplicar_funcion(funcion,  numeros_lista):

#     lista=[]

#     for i in numeros_lista:
#         lista.append(funcion(i))
#     return lista

# def restar(numero):
#     numero  = numero - numero
#     return numero

# print(f"Resultado: {aplicar_funcion(restar, lista_resta)}")            



# lista_suma=[1,2,3,4]

# def aplicar_funcion(funcion, numero_lista):

#     lista=[]

#     for i in numero_lista:
#         lista.append(funcion(i))
#     return lista    

# def suma(numero):
#     numero = numero + numero 
#     return numero

# print(f"Resultado: { aplicar_funcion(suma, lista_suma)}")


# lista_suma=[1,2,2,4]

# def aplicar_función(funcions, numero_listas):
#     mista=[]

#     for i in numero_listas:
#         mista.append(funcions(i))

#     return mista

# def suma(numero):

#     numero=numero + numero
#     return numero

# print(aplicar_función(suma, lista_suma ))    

# saludo="Hola mundo"

# print(saludo)


# nombre=input("Ingrese su nombre: ").title()

# print(f"Hola {nombre}")

# operacion= (3+2) / (2*5) ** 2

# print(f"{operacion}")

# horas_trabajadas=int(input("Ingrese horas trabajadas: "))
# horas_precio=float(input("Ingrese el valor por hora: "))

# resultado= horas_trabajadas * horas_precio

# print(f"El pago por las {horas_trabajadas} horas es: ${resultado}")


# suma=int(input("ingrese un entero positivo: "))

# resultado= suma * (suma + 1) / 2

# print(f"la suma de 1 hasta {suma} es: {resultado:.0f}")

# num1=int(input("Ingrese el primer número entero: "))
# num2=int(input("Ingrese el segundo número entero: "))

# cociente= float(num1 / num2)
# resto= float(num1 % num2)

# print(f"{num1} entre {num2} da un cociente {cociente} y un resto {resto}")


# cantidad_invertir=float(input("Ingrese cantidad a invertir: "))
# interes_anual=float(input("Ingrese interés anual: "))
# anios_inversion=float(input("Años de inversion: "))

# # interes= cantidad_invertir +  (cantidad_invertir / interes_anual)
# # resultado= interes * anios_inversion

# resultado = cantidad_invertir * ( interes_anual / 100 + 1) ** anios_inversion

# print(f"Capital final {resultado:.2f}")


# cantidad=float(input("¿Cantidad a invertir? "))
# interes=float(input("Interés anual "))
# anios=float(input("Años de inversión "))

# resultado = cantidad*(interes / 100 + 1 ) ** anios

# print(f"Capital final: ${resultado:.2f}")

# peso=float(input("Ingrese su peso "))
# estatura=float(input("Ingrese su estatura "))

# imc = peso  / (estatura) ** 2

# print(f"Tu índice de masa corporal es {imc:.3f}")


# payaso=112
# muneca=75

# numero_payasos=int(input("Ingrese numero de payaso vendidos: "))
# numero_munecas=int(input("Ingrese numero de muñecas vendidos: "))

# peso_payasos = float(numero_payasos * payaso)
# peso_munecas = float(numero_munecas * muneca)

# peso_total = float(peso_payasos + peso_munecas)

# print(f"El peso de payasos es: {peso_payasos} g")
# print(f"El peso de muñecas es: {peso_munecas} g")
# print(f"El peso total del pedido es: {peso_total}")



# deposito=float(input("Ingrese el deposito "))
# interes=0.04

# anio1 =  deposito * ( interes  + 1)
# anio2 = anio1 * (interes + 1)
# anio3 = anio2 * (interes + 1)


# print(f"\n\tBalance segundo año ${anio2:.2f}")
# print(f"\tBalance primer año ${anio1:.2f}")
# print(f"\tBalance tercer año ${anio3:.2f}")


# pan_vendido=int(input("Cantidad de Pan vendido del día anterior "))
# pan=float(3.49)
# descuento=0.6

# precio_normal = float(pan * pan_vendido)
# precio_con_descuento = pan_vendido  * pan * (1 - descuento)

# print(f"\nPrecio unidad de pan ${pan}")
# print(f"Precio normal de los {pan_vendido} panes es de ${precio_normal:.2f} ")
# print(f"Precio con el 60% de descuento ${precio_con_descuento:.2f}")
# print(f"\n\t TOTAL ${precio_con_descuento:.2f}")



# nombre=str(input("Ingrese su nombre: ")).title()
# numero=int(input("Ingrese un número entero: "))

# print(f"\n{nombre} "*numero)


# nombre=str(input("Ingrese su nombre completo: "))

# nombre1 = nombre.lower()
# nombre2 = nombre.upper()
# nombre3 = nombre.title()


# print(f"\n{nombre}")
# print(f"{nombre1}")
# print(f"{nombre2}")
# print(f"{nombre3}")


# nombre=str(input("Ingrese  su nombre: ").title())

# nombre_numero = len(nombre)

# print(f"Su nombre {nombre} tiene {nombre_numero} letras.")



# frase=str(input("Escriba una frase: "))

# resultado = frase
# hola = frase

# print(resultado[::-1])
# print("".join(reversed(hola)))


# numero=input("Ingrese un numero +34-913724710-56 ")

# print(numero[4:13:])
# print(numero[4:-3])


# frase=input("Escriba una frase ")
# # vocal=input("Escriba una vocal ").upper()
# vocal=input("Escriba una vocal ")

# print(f"{frase}{vocal}")
# print(frase.replace(vocal, vocal.upper()))
# print(frase.replace("pues", frase))


email=str(input("Escriba su email: "))

print(email[:email.find("@")]+"@ceu.es")






















