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

nombre_producto=input("Ingrese el nombre producto: ")
precio_producto=float(input("Ingrese el precio producto: "))
unidades_producto=int(input("Ingrese el número unidades producto: "))

total_valor=precio_producto*unidades_producto

# print(nombre_producto, precio_producto, unidades_producto, total_valor)
print(f'{nombre_producto}: {unidades_producto:3d} unidades x {precio_producto:11.2f}€ = {total_valor:9.2f}€'.format(nombre_producto = nombre_producto, unidades_producto = unidades_producto, precio_producto = precio_producto, total_valor = total_valor))








