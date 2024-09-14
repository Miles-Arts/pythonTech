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

numeros_loteria=[]

for i in range(6):
    numeros_loteria.append(int(input("Introduce un número ganador: "))) 
numeros_loteria.sort()
print(f"Los números ganadores son {numeros_loteria}")



















