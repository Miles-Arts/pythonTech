import random 
import itertools
import string
# print("Ingresa 3 numeros: ")
# numero1=float(input("primer número: "))
# numero2=float(input("segundo número: "))
# numero3=float(input("tercer número: "))

# suma=numero1+numero2+numero3
# promedio=suma / 3

# print("---Resultados---")
# print(f"La suma de los 3 números es: {suma:.2f}")
# print(f"El promedio de los tres numeros es: {promedio:.1f}")


# temperatura=float(input("Ingresa la termperatura en grados Celsius: "))

# fahrenheit=(temperatura*9/5) + 32
# kelvin=temperatura + float(273.15)

# print("---Conversor de temperaturas---")
# print(f"Temperatura en Celsius es: {temperatura} °C")
# print(f"Temperatura en Fahrenheit es: {fahrenheit} °F")
# print(f"Temperatura en Kelvin es: {kelvin:.2f} °K")

# medidas triangulo
# print("Ingresa las dimenciones del triángulo: ")
# base=float(input("Ancho: "))
# altura=float(input("Altura: "))
# print("\nIngresa las dimenciones de los bordes del triangulo: ")
# perimetro1=float(input("Medida base: "))
# perimetro2=float(input("Medida izquierda: "))
# perimetro3=float(input("Medida base: "))

# area=float(0.5) * base * altura
# area1=(base * altura) / 2

# perimetro_total=perimetro1+perimetro2+perimetro3
# perimetro_total1=2*(base+altura)

# print(f"El área del triángulo es: {area1:.2f}")
# print(f"El perímetro del triángulo es: {perimetro_total:.2f}")
# print(f"El perímetro del triángulo es: {perimetro_total1:.2f}")


# CONVEROS MINUTOS HORAS DIAS

# print("---Conversor  mMnutos a Horas y Días")
# minutos=float(input("Ingrese cantidad de minutos: "))

# horas=minutos / 60
# dias=minutos / 1440
# dias1=float(minutos / (60*24))


# print(f"Los {minutos} minutos.")
# print(f"Son {horas:.0f} horas. ")

# if dias1 >= 1.00 and dias1 <= 1.99:
#     print(f"Son {dias1:.0f} día.")
# elif dias1 >= 2.00:
#     print(f"Son {dias1:.0f} días.")
# else:
#     print(f"Son {dias:.2f} día. ")

# print("---Sistema básico de Calificacion---")
# estudiante=str(input("Ingrese nombre estudiante: ")).title()
# print("Ingrese notas de cada asignatura")

# nota1=float(input("Nota Inglés: "))
# nota2=float(input("Nota Computación: "))
# nota3=float(input("Nota Sociales: "))

# promedio=(nota1+nota2+nota3) / 3

# if promedio >= 3.0:
#     print(f"El estudiante: {estudiante}")
#     print(f"NOTAS:\n")
#     print(f"Inglés: \t{nota1}")
#     print(f"Computación: \t{nota2}")
#     print(f"Sociales: \t{nota3}")
#     print(f"\tPromedio: {promedio:.2f}")
#     print(f"\t\tSemestre Aprobado.")
# elif promedio <= 2.9:
#     print(f"El estudiante: {estudiante}")
#     print(f"NOTAS:\n")
#     print(f"Inglés: \t{nota1}")
#     print(f"Computación: \t{nota2}")
#     print(f"Sociales: \t{nota3}")
#     print(f"\tPromedio: {promedio:.2f}")
#     print(f"\t\tSemestre Reprobado.")


# TIENDA DE FRUTAS

# usuario=str(input("Ingrese nombre: ")).title()

# producto1=str(input("Nombre producto: ")).title()
# precio1=float(input("Precio producto: "))
# cantida1=int(input("Cantidad: "))

# producto2=str(input("Nombre producto: ")).title()
# precio2=float(input("Precio producto: "))
# cantida2=int(input("Cantidad: "))

# producto3=str(input("Nombre producto: ")).title()
# precio3=float(input("Precio producto: "))
# cantida3=int(input("Cantidad: "))

# costo1=precio1*cantida1
# costo2=precio2*cantida2
# costo3=precio3*cantida3

# costo_lista=[costo1,costo2,costo3]

# total_precio=sum(costo_lista)
# descuento=10
# final_precio=float(total_precio *descuento)/100
# total_final=total_precio - final_precio

# if total_precio >= 20:
#     print(f"El usuario: {usuario}")
#     print(f"Con los siguientes productos: \n{producto1} cantidad {cantida1} valor: ${costo1} \n{producto2} cantidad {cantida2} valor: ${costo2} \n{producto3} cantidad {cantida3} valor: ${costo3}")
#     print("Por compra superios a $20")
#     print("Tiene un descuento del 10%")
#     print(f"Total a pagar ${total_precio:.2f}")
#     print(f"Valor con descuento: ${total_final:.2f}")
    
# else:
#     print(f"El usuario {usuario}")
#     print(f"Con los siguientes productos: \n{producto1} cantidad {cantida1} valor: ${costo1} \n{producto2} cantidad {cantida2} valor: ${costo2} \n{producto3} cantidad {cantida3} valor: ${costo3}")
#     print(f"Total a pagar ${total_precio:.2f}")
#     print("No tiene descuento.")    


# -------------------------------------------------------------------
# def calcular_costo(precio, cantidad):
#     return precio*cantidad

# print("--Tienda don Veci---")
# usuario=input("Ingrese su nombre: ").title()

# productos=[]
# precios=[]

# for i in range(3):
#     producto=input(f"\nIngrese nombre producto {i + 1}: ").title()
    
#     precio=float(input(f"Precio {producto}: "))
#     cantidad=int(input(f"Cantidad productos {producto}: "))

#     costo= calcular_costo(precio, cantidad)
#     productos.append((producto, cantidad, costo))
#     precios.append(costo)

# total=sum(precios)

# descuento=0.1*total if total > 20 else 0
# total_final= total - descuento

# print("Resumen Compra")
# print(f"Cliente: {usuario}\n")

# for producto, cantidad, precio in productos:
#     print(f"Producto: {producto} | Cantidad: {cantidad} | Precio: ${precio:.2f}")
# print(f"\nTotal sin descuento: ${total:.2f}")

# if descuento > 0:
#     print(f"Descuento apliacado: ${descuento:.2f}")
# print(f"Total a pagar: ${total_final:.2f}")

# Registro de notas de estudiantes
# estudiante=str(input("Nombre Estudiante: ")).title()
# notas=[]

# for i in range(4):
#     nota=float(input(f"Ingrese la nota {i+1} : "))

#     notas.append(nota)
#     promedio=float(sum(notas) / len(notas))

# def calcular_notas(promedio):
#     if promedio >= 3.0:
#         return("Aprobado")
#     elif promedio <= 2.9:
#         return("Reprobo") 

# def nota_alta(notas):
#     return max(notas)
     
# def nota_baja(notas):
#     return min(notas)       

# def orden_notas(notas):
#     return sorted(notas)   

# print(f"Estudiante {estudiante}")
# print(f"Promedio: {promedio:.2f}")
# print(f"Notas más alta: {nota_alta(notas)}")
# print(f"Nota más baja: {nota_baja(notas)}")
# print(f"Orden de notas: {orden_notas(notas)}")
# print(f"Semestre: {calcular_notas(promedio)}.")


# PRODUCTOS TIENDA

# productos={}

# print(f"---Tienda don Comestibles---")
# cantidad_productos=int(input("\nIngrese cantidad productos: "))

# for i in range(cantidad_productos):

#     producto=str(input(f"\nProducto {i+1} nombre: ")).title()
#     precio=float(input(f"Ingrese precio de la {producto}: "))
#     cantidad=int(input(f"Ingrese cantida de {producto}: "))

#     # productos.append(producto,precio,cantidad)
#     productos[producto] = {
#         "precio": precio,
#         "cantidad": cantidad
#     }

# def valor_total(precio, cantidad):
#     return precio * cantidad
    
# gran_total=0

# print("\n---Lista de Productos---")
# for producto, detalle in productos.items():
#     print(f"{producto} Precio {detalle["precio"]}, Cantidad {detalle["cantidad"]}")

# print(f"\nValor total del inventario: ${valor_inventario:.2f}")
# print(f"Producto más valioso: {producto_mas_valioso['nombre']} (${producto_mas_valioso['valor_total']:.2f})")


# def calcular_valor_total(precio, cantida):
#     return precio * cantida

# print("---Control de inventario---")
# ingresar_productos=int(input("Cantidad de productos a ingresar: "))

# productos=[]

# for i in range(ingresar_productos):
#     print(f"\nProducto {i+1}:")
#     nombre=str(input(f"Nombre del producto: ")).title()
#     precio=float(input(f"Precio por unidad: $"))
#     cantidad=int(input(f"Cantidad en inventario: "))

#     valor_total=calcular_valor_total(precio, cantidad)

#     producto={
#         "nombre": nombre,
#         "precio": precio,
#         "cantidad": cantidad,
#         "valor_total": valor_total
#     }

#     productos.append(producto)


# valor_inventario=sum(p["valor_total"] for p in productos)
# producto_mas_valioso=max(productos, key=lambda p: p["valor_total"])    

# print("\n---Resumen del Inventario---\n")

# for p in productos:
#     print(f"\t- {p["nombre"]}: ${p["precio"]} x {p["cantidad"]} unidades = ${p["valor_total"]:.2f}")

# print(f"\nValor total del inventario: ${valor_inventario:.2f}")
# print(f"Producto más valioso: {producto_mas_valioso['nombre']} (${producto_mas_valioso['valor_total']:.2f})")


# # Calculadora gastos mensuales
# print("---Calculadora personal---")
# categorias=[]

# # def gastos_totales(gasto):
# #     return gasto+gasto   

# usuario=str(input("Ingrese su nombre: ")).title()
# numero_categorias=int(input("Cuántas categorias desea ingresar: "))
     

# for i in range(numero_categorias):
#     print(f"\nCategoria {i+1}: ")
#     categoria=str(input("Nombre categoria: ")).title()
#     gasto=float(input(f"Gastos de {categoria}: $"))

#     categoria={
#         "usuario": usuario,
#         "categoria": categoria,
#         "gasto": gasto
#     }

#     categorias.append(categoria)

# suma_total= sum(gasto["gasto"] for gasto in categorias )
# gasto_alto=max(categorias, key=lambda ma: ma["gasto"])
# gasto_menor=min(categorias, key=lambda mi: mi["gasto"])
# orden_gastos=sorted(categorias, key=lambda orden: orden["gasto"])

# # def porcentaje(gasto, suma_total):
# #     return (gasto / suma_total) * 100 if suma_total > 0 else 0

# def porcentaje(gasto, suma_total):
#     if suma_total > 0:
#         return (gasto / suma_total) * 100
#     else:
#         return 0


# print(f"Lista de Gastos")
# print(f"Hola {usuario}")
# print(f"Gasto Tota: ${suma_total}")
# print(f"Gasto más alto ${gasto_alto["gasto"]}")
# print(f"Gasto menor ${gasto_menor["gasto"]}")

# print(f"Orden de gastos de menor a mayor: ")
# for items in orden_gastos:
#     print(f"{items["categoria"]}: ${items["gasto"]}")

# print(f"Porcentaje de cada gasto respesto al total: ")
# for items in categorias:
#     porcentaje_gasto=porcentaje(items["gasto"], suma_total)
#     print(f"{items["categoria"]}: {porcentaje_gasto:.2f}%")


# def cualcular_porcentaje(gasto, total):
#     return (gasto / total) * 100 if total > 0 else 0

# print("Calculadora de gastos mensuales")
# nombre=input("Ingresa tu nombre: ").title()
# lista_gastos=int(input("Ingrese numero de gastos: "))

# gastos=[]

# for i in range(lista_gastos):

#     categoria= input(f"Ingresa el nombre del gasto {i+1}: ").title()
#     monto=float(input(f"Ingrese el monto gastado en {categoria}: $"))
#     gastos.append((categoria,monto))

# total_gastos=sum(gasto[1] for gasto in gastos)
# gasto_mayor=max(gastos, key=lambda x: x[1] )    
# gasto_minimo=min(gastos, key=lambda x: x[1])
# gastos_ordenados=sorted(gastos, key=lambda x: x[1])

# print(f"\nResumen de tus gastos")
# print(f" Usuario: {nombre}\n")

# for categoria, monto in gastos:
#     porcentaje=cualcular_porcentaje(monto, total_gastos)
#     print(f"- {categoria}: ${monto:.2f} ({porcentaje:2f} %)")


# print(f"\n Total gastado: ${total_gastos:.2f}")
# print(f"Gasto más alto: {gasto_mayor[0] } (${gasto_mayor[1]:.2f})")
# print(f"Gasto más bajo: {gasto_minimo[0] } (${gasto_minimo[1]:.2f})")
# print(f"\n Gastos ordenados de menor a mayor: ")

# for categoria, monto in gastos_ordenados:
#     print(f"- {categoria}: ${monto:.2f}")


# CONTROL NOTAS ESTUDIANTES

# cantidad_estudiantes=int(input("Ingrese la cantidad de estudiantes: "))
# estudiantes=[]

# for i in range(cantidad_estudiantes):
#     nombre=str(input("Ingrese nombre estudiante: ")).title()
#     nota=float(input("Notas final: "))

#     estudiante={
#         "nombre": nombre,
#         "nota": nota
#     }

#     # materia["nota"].append()
#     estudiantes.append(estudiante)

# suma_notas=sum(estudiante["nota"] for estudiante in estudiantes )
# promedio_notas= suma_notas / cantidad_estudiantes
# nota_mas_baja=min(estudiantes, key=lambda n: n["nota"])
# nota_mas_alta=max(estudiantes, key=lambda n: n["nota"])

# def aprobo(nota):
#     if  nota >= 3:  
#         return "Aprobado"
#     else:
#         return "Reprobo" 


# for estudiante in estudiantes:
#     print(f"El estudiante: {estudiante["nombre"]}")
#     print(f"Nota final: {estudiante["nota"]}")

# print(f"La nota más baja es: {nota_mas_baja["nota"]}")
# print(f"La nota más alta es: {nota_mas_alta["nota"]}")
# print(f"Promedio de notas: {promedio_notas}")



# for estudiante in estudiantes:
#     print(f"El estudiante {estudiante["nombre"]} {aprobo(estudiante["nota"])}")

# print("---Control de notas---")

# num_estudiantes=int(input("¿Cuántos estudiantes a resgistar? "))

# notas=[]

# for i in range(num_estudiantes):
#     nombre=input(f"\nNombre estudiante {i+1}:").title()
#     nota=float(input(f"Nombre de {nombre}: "))

#     notas.append((nombre, nota))

# suma_notas=sum(nota[1] for nota in notas)
# promedio=suma_notas / num_estudiantes
# nota_max=max(notas, key=lambda x: x[1])
# nota_min=min(notas, key=lambda x: x[1])

# aprobados=sum(1 for  _, nota in notas if nota >= 3.0)
# reprobados=num_estudiantes - aprobados

# print("\n Resumen de notas")

# for nombre,nota in notas:
#     print(f"- {nombre}: {nota:.2f}")

# print(f"\nPromedio notas grupos: {promedio:.2f}")
# print(f"Nota mas alta {nota_max[0] } con {nota_max[1]:.2f}")
# print(f"Nota más baja {nota_min[0]} con {nota_min[1]:.2f}")

# print(f"\n Estudiantes aprobados (>= 3.0): {aprobados}")
# print(f"Estudiante sreprobados (< 3.0): {reprobados}")


# ...REGISTRO COMPRAS SUPERMECADO

# cantidad_productos=int(input("Ingrese cantidad productos comprados: "))
# productos=[]

# for i in range(cantidad_productos):

#     nombre_producto=str(input("Ingrese nombre producto: ")).title()
#     precio_unidad=float(input(f"Ingrese precio unidad {nombre_producto}: $"))
#     cantidad_comprada=int(input(f"Cantidad comprada {nombre_producto}: "))
   
#     producto={
#         "nombre_producto": nombre_producto,
#         "precio_unidad": precio_unidad,
#         "cantidad_comprada": cantidad_comprada
#     }
#     productos.append(producto)

# costo_total=sum( producto["precio_unidad"] * producto["cantidad_comprada"] for producto  in productos)
# producto_mas_caro=max(productos, key=lambda p: p["precio_unidad"])
# producto_menos_caro=min(productos, key=lambda p: p["precio_unidad"])
# valor_mas_de_diez=sum(1 for producto in productos if producto["precio_unidad"] >= 10)

# print(f"Producto más costoso es: {producto_mas_caro["nombre_producto"]} ${producto_mas_caro["precio_unidad"]}")
# print(f"Producto menos costoso es: {producto_menos_caro["nombre_producto"]} ${producto_menos_caro["precio_unidad"]}")
# print(f"Total compra: ${costo_total}")
# print(f"Producto de más de $10: {valor_mas_de_diez}")        

# print("---Lista de productos comprados---")
# for producto in productos:
#     print(f"\nProducto: {producto["nombre_producto"]}\nPrecio: ${producto["precio_unidad"]:.2f}\nCantidad: {producto["cantidad_comprada"]}")


    # print("---Registro de compras supermecado---\n")
    # # entreda pedir cantidad productos
    # num_productos=int(input("¿Cuántos productos compraste?: "))
    # # lista para almacenar los productos
    # productos=[]

    # # entrada de datos
    # for i in range(num_productos):

    #     print(f"\nProducto {i+1}: ")
    #     nombre=str(input("Nombre del producto: ")).title()
    #     precio=float(input(f"Precio del producto {nombre}: $"))
    #     cantidad=int(input(f"Cantidad de producto {nombre} comprado: "))

    # # productos guardadod en diccionario

    #     producto={
    #         "nombre": nombre,
    #         "precio": precio,
    #         "cantidad": cantidad,
    #         "total": precio * cantidad #Calculamos costo total de productos
    #     }

    #     productos.append(producto)

    # # Procesamiento

    # suma_total=sum(prod["total"] for prod in productos) 
    # producto_mas_caro=max(productos, key=lambda x: x["precio"]) 
    # producto_menos_caro=min(productos, key=lambda x: x["precio"])
    # productos_caros = sum(1 for prod in productos if prod["precio"] > 10)  # Productos que costaron más de $10

    # #Salida
    # print(f"Resumen de compra")

    # for prod in productos:
    #     print(f"- {prod["nombre"]} (x{prod["cantidad"]}): ${prod["total"]:.2f}")

    # print(f"\n Total gastado: ${suma_total:.2f}")
    # print(f"Producto más caro: {producto_mas_caro["nombre"]} Precio ${producto_mas_caro["precio"]:.2f}")
    # print(f"Producto más económico: ${producto_menos_caro["nombre"]} Precio ${producto_menos_caro["precio"]:.2f} ")
    # print(f"Producto con precio mayor a $10 {productos_caros}")


#CALIFICACIONES ESTUDIANTES

# cantidad_estudiantes=int(input("Ingrese la cantidadd de estudiantes: "))
# calificaciones=[]

# for i in range(cantidad_estudiantes):
#     print(f"Estudiante {i+1}")
#     nombre=str(input("Nombre de estudiante: ")).title()
#     nota_final=float(input(f"Ingrese la nota final de {nombre}: "))

#     calificacion={
#         "nombre": nombre,
#         "nota_final": nota_final
#     }
#     calificaciones.append(calificacion)

# suma_notas=sum(calif["nota_final"] for calif in calificaciones) 
# promedio_notas= suma_notas / cantidad_estudiantes 
# mejor_nota=max(calificaciones, key=lambda x: x ["nota_final"])
# peor_nota=min(calificaciones, key=lambda x: x ["nota_final"])
# estudiantes_aprobados=sum(1 for califi in calificaciones if califi["nota_final"] >= 3.0)
# orden_lista=sorted(calificaciones, key=lambda x: x["nota_final"])

# print("\n---RESULTADOS NOTAS ESTUDIANTES---\n")
# print(f"Promedio {promedio_notas:.2f}")
# print(f"Mejor nota de {mejor_nota["nombre"]} {mejor_nota["nota_final"]}")
# print(f"Peor nota de {peor_nota["nombre"]} {peor_nota["nota_final"]}")
# print(f"Estudiantes aprobados nota superior a 3.0: {estudiantes_aprobados}")

# print("\n---Orden de Notas---")
# for calificacion in orden_lista:
#     print(f"Estudiante: {calificacion["nombre"] }.\nNota: {calificacion["nota_final"]}")


# print(f"\n---Gestor de Calificaciones Escolares---\n")

#entrada de datos
# num_estudiantes=int(input("Ingresa cantidad de estudiantes: "))
# estudiantes=[]

# for i in range(num_estudiantes):
#     print(f"\nIngresando datos de estudiantes {i+1}")
#     nombre=str(input("Nombre de estudiante: ")).title()
#     notas=[] #lista para almacenar notas

#         #pedir 3 calificaiones
#     for j in range(3):
#         nota=float(input(f"Ingrese la nota {j+1} de {nombre}: "))
#         notas.append(nota)

#     #guardar estudiante
#     estudiante={
#         "nombre": nombre,
#         "notas": notas,
#         "promedio": sum(notas) / len(notas) #calcular promedio
#     }
#     estudiantes.append(estudiante)

# #Procesamieto de datos
# mejor_estudiantes=max(estudiantes, key=lambda e: e['promedio']) 
# peor_estudiantes=min(estudiantes, key=lambda e: e['promedio'])   
# estudiantes_aprobados=sum(1 for aprobo in estudiantes if aprobo['promedio'] >= 3.0)
# lista_ordenada=sorted(estudiantes, key=lambda e: e['promedio'], reverse=True)

# #Funcion para calificar notas
# def clasificar_nota(nota):
#     if nota >= 4.5:
#         return "Excelente"
#     elif nota >= 4.0:
#         return "Muy bien"
#     elif nota >= 3.0:
#         return "Aprobado"
#     else:
#         return "Reprobado"            

# #Salida de datos
# print(f"\n---Resumen de calificaciones---")

# for e in estudiantes:
#     estado=clasificar_nota(e['promedio'])
#     print(f"\nEstudiante: {e['nombre']}")
#     print(f"Notas: {e['notas']}")
#     print(f"Promedio: {e['promedio']:.2f} - {estado}.")

# print(f"\nMejor estudiante {mejor_estudiantes['nombre']} con {mejor_estudiantes['promedio']:.2f}")    
# print(f"Peor estudiante {peor_estudiantes['nombre']} con {peor_estudiantes['promedio']:.2f}")
# print(f"Estudiantes aprobados: {estudiantes_aprobados} de {num_estudiantes}")

# print(f"\nLista de estudiantes ordenados por promedio:")
# for e in lista_ordenada:
#     estado=clasificar_nota(e['promedio'])
#     print(f"{e['nombre']}: {e['promedio']:.2f} - {estado}.")


# #Registro de gastos personales
# print(f"\n---Registro de gastos personales\n")
# cantidad_gastos=int(input("Ingrese la cantidadd de gastos: "))
# gastos=[]

# for i in range(cantidad_gastos):
#     print(f"\nGasto número {i+1}")
#     nombre_gasto=str(input("Ingrese nombre del gasto: ")).title()
#     monto_gastado=float(input(f"Ingrese monto gastado de {nombre_gasto}: $"))
#     categoria_monto=str(input("Ingrese categoria ejemplo: Comida - Transporte - Entretenimiento: \n")).title()

#     gasto={
#         "nombre_gasto":nombre_gasto,
#         "monto_gastado":monto_gastado,
#         "categoria_monto":categoria_monto
#     }

#     gastos.append(gasto)

# total_gastado=sum(gas["monto_gastado"] for gas in gastos)
# mayor_gasto=max(gastos, key=lambda may: may["monto_gastado"])
# menor_gasto=min(gastos, key=lambda men: men["monto_gastado"])
# gastos_mayores_cincuenta=sum(1 for may in gastos if may["monto_gastado"] > 50)
# orden_gastos=sorted(gastos, key=lambda orden: orden["monto_gastado"], )
# porcentaje_de_cada_gasto=sum(producto["monto_gastado"] for producto in gastos)

# #Saida
# print(f"---Lista de gastos personales---")
# print(f"\nMayor gasto {mayor_gasto['nombre_gasto']} con ${mayor_gasto['monto_gastado']:.2f}")
# print(f"Menor gasto {menor_gasto['nombre_gasto']} con ${menor_gasto['monto_gastado']:.2f}")
# print(f"\nGastos superiores a $50: {cantidad_gastos}/{gastos_mayores_cincuenta}")

# print(f"\n---Lista de gastos de menor a mayor---\n")
# for orden in orden_gastos:
#     print(f"Categoria: {orden["categoria_monto"]}. Gasto: {orden["nombre_gasto"]}. Valor: ${orden["monto_gastado"]}")

# print(f"\n---Porcentaje de gastos---")
# for porcentaje_gasto in gastos:
#     porcentaje=(porcentaje_gasto["monto_gastado"] / porcentaje_de_cada_gasto) * 100
#     print(f"Gasto: {porcentaje_gasto["nombre_gasto"]}. Categoria: {porcentaje_gasto["categoria_monto"]}. {porcentaje:.2f}%")



# # porcentaje = (producto["valor"] / gasto_total) * 100


# numero secreto
# print(f"---Adivinda el número secreto---\n")
# for i in range(3):
#     while True:
#         try:
#             numero=int(input("Ingrese un número: "))
#             numero_secreto=3
#             if numero == numero_secreto:
#                 print(f"Has adivinado {numero_secreto} es numero secreto!")
                
#             elif numero >= numero_secreto:
#                 print(f"Una pista, el numero es menor")   
#             elif numero <= numero_secreto:
#                     print("Una pista, el numero es mayor")
#             break
#         except ValueError:
#             print(F"Error debes ingresar un dato válido")            

#         print(f"\n---Felicidades haz ganado---") 


#NUMERO SECRETO

# print(f"---Adivinda le número secreo---\n")

# numero_secreto=3

# for i in range(3):
#     while True:
#         try:
#             numero=int(input("Ingrese un número: "))

#             if numero == numero_secreto:
#                 print(f"¡Has adivinado! {numero_secreto} es el número secreto")
#                 print(f"\n---Felicidades, has ganado---")
#                 exit()

#             elif numero > numero_secreto:
#                 print("Una pista: el número es menor")
#             else:
#                 print("Una pista: el número es mayor")  

#             break
#         except ValueError:
#             print("Error: debes ngresar un dato válido.")

# print(f"\nLo siento, has perdidio. \nEl número secreto era {numero_secreto}.")

# numero_secreto= ram.randint(0,10)

# print("¡Advina el número entre 0 y 10")

# while True:
#     intento=int(input("Ingresa tu primer intento: "))
#     if intento.isdigit():
#         intento = int(intento)
#         break
#     else:
#         print("Por favor, ingresa un número válido.")

# for i in range(2):
#     if intento == numero_secreto:
#         print("¡Felicidades! Adivinaste el número.")
#         break
#     elif intento < numero_secreto:
#         print("El número es mayor.")
#     else:
#         print("El número es menor.")

#     while True:
#         intento = int(input("Inténtalo de nuevo: ")) 
#         if intento.isdigit():
#             intento = int(intento)
#             break
#         else:
#             print("Por favor, ingresa un número válido.")       

# else:
#     print(f"¡Oh no! El número secreto era {numero_secreto}.")

# print("¡Gracias por jugar!")

#Ejercicio: Adivina el Rango del Número Secreto

# print("---Adivina el rango del número secreto!---")
# print("---Entre 1 y 100---")

# numero_secreto= ram.randint(1,100)

# while True:
#     intento=int(input("Ingresa tu primer intento: "))
#     if intento.isdigit():
#         intento=int(intento)
#         break
#     else:
#         print(f"Ingresa un número válido")

#     for i in range(3):
#         if intento > 0 and intento < 20:
#             match intento:
#                 case 0 | 5: 

# numero_secreto=random.randint(1,100)

# print("\nAdivina el rango del número secreto entre 1 y 100")
# print("Opciones:")
# print("1️⃣  Bajo (1-33)")
# print("2️⃣  Medio (34-66)")
# print("3️⃣  Alto (67-100)\n")

# for intento in range(5):
#     while True:
#         opcion= input("Elige un rango (1, 2  o 3): ")
#         if opcion.isdigit() and opcion in ("1","2","3"):
#             opcion=int(opcion)
#             break
#         else:
#             print("Opción inválida. Ingresa 1, 2 o 3.\n")

#     match opcion:
#         case 1:
#             if 1 <= numero_secreto <= 33:
#                 print("Correcto! el número estaba en el rango Bajo")
#                 break
#             else:
#                 print("Incorrecto! el número NO está en el rango Bajo\n")
#         case 2:
#             if 34 <= numero_secreto <= 66:
#                 print("Correcto! el número estaba en el rango Medio")
#                 break
#             else:
#                 print("Incorrecto! el número NO está en el rango Medio\n")
#         case 3:
#             if 67 <= numero_secreto <=100:
#                 print("Correcto! el número estaba en el rango Alto") 
#                 break
#             else:
#                 print("Incorrecto! el número NO está en el rango Alto\n")       
# else:
#     print(f"Perdiste! El número secreto era {numero_secreto}.")

# print("Gracias por jugar.")


# print("\n---Loteria Mágica---")
# print("Habran 3 numero aleatorios y deberas adivinar")
# print("Debes adivinar le número entre 1 y 50\n")
# print("1️⃣  Bajo (1-16)")
# print("2️⃣  Medio (17-43)")
# print("3️⃣  Alto (44-50)\n") 

# numero_loteria=random.randint(1,50)
# lista=[]

# for i in range(5):
#     while True:
#         print("Ingresa 3 numeros separados por coma (,)")
#         intento=input("Ingresa un número entre 1 a 50: ")
        
#         if intento.isdigit() and 1 <= int(intento) <=50:
#             lista=list(map(int, intento.split(",")))
#             break
#         else:
#             print("Ingrese un nùmero válido")

#         match lista:
#             case 1:
#                 if 1 <= numero_loteria <= 16:
#                     print("Correcto el numero esta ahí")
#                     break
#                 else:
#                     print("Incorrecto vuelve a intentar")    
#             case 2:
#                 if 17 <= numero_loteria <= 49:
#                     print("Correcto el numero esta ahí")
#                     break
#                 else:
#                     print("Incorrecto vuelve a intentar")
#             case 3:
#                 if 17 <= numero_loteria <= 49:
#                     print("Correcto el numero esta ahí")
#                     break
#                 else:
#                     print("Incorrecto vuelve a intentar")

# else:
#     print(f"Lo siento el número de loteria ganador era {numero_loteria}")
# print("Gracias por jugar!")
     

# numeros_secretos=random.sample(range(1,50), 3)

# print("\n Bienvenidos a la loteria Mágica\n")
# print("Tienes 5 oportunidades para adivinar \nal menos uno de los 3 números secretos")
# print("Los números están entre 1 y 50\n")

# intentos_realizados=[]

# for intento in range(5):
#     while True:
#         numero=input(f"Intento {intento+1}: Ingresa un número entre 1 y 50: ")
#         if numero.isdigit() and 1 <= int(numero) <= 50:
#             numero=int(numero)
#             if numero in intentos_realizados:
#                 print("Ya ingresaste este numero. Intenta con otro\n")
#             else:
#                 intentos_realizados.append(numero)
#                 break
#         else:
#             print("Entrada inválida. \nIngresa un número válido entre 1 y 50.\n") 

#     match numero in numeros_secretos:
#         case True:
#             print(f"Felicidades! {numero}  es un número secreto. Has Ganado!!!\n")
#             break
#         case False:
#             print("Incorrecto. Sigue intentando...\n")               

# else:
#     print(f"Oh no! Perdiste.")
#     print(f"Los números secretos eran: ")
#     for secretos in numeros_secretos:
#         print(f"-> {secretos}")
# print("\nGracias por jugar!\n¿Te atreves a intentarlo de nuevo?")

# contador de vocales
# palabra=input("Ingrese una palabra: ").lower()
# vocales=["a", "e", "i", "o", "u"]
# suma_vocales=0

# for i in palabra:
#     if i in vocales:
#         suma_vocales+=1
# print(f"La palabra: {palabra.upper()} tiene {suma_vocales} vocales")        

#Control de Inventario en una Tienda

#Control de Inventario en una Tienda 🏪
# print("\n---Control de Inventario en una Tienda 🏪---\n")

# cantidad_productos=int(input("Ingrese cantidad productos de la tienda: "))
# productos=[]

# for i in range(cantidad_productos):
#     print(f"\nProducto número {i+1} ")
#     nombre=str(input("Nombre Producto: ")).title()
#     precio_unitario=float(input(f"Ingrese precio unitario de {nombre}: $"))
#     cantidad_stock=int(input("Cantidad de productos: "))
#     categoria=str(input("Alimentos - Electrónica - Ropa: ")).title()

#     producto={
#         "nombre" : nombre,
#         "precio_unitario" : precio_unitario,
#         "cantidad_stock" : cantidad_stock,
#         "categoria" : categoria,
#         "valor_total": precio_unitario * cantidad_stock
#     }

#     productos.append(producto)

# valor_general = sum(prod["valor_total"] for prod in productos)
# mas_caro=max(productos, key=lambda prod: prod["precio_unitario"]) 
# menos_caro=min(productos, key=lambda prod: prod["precio_unitario"])
# mas_stock=sum(1 for stock in productos if stock["cantidad_stock"] >= 20 )
# orden_stock=sorted(productos, key=lambda prod: prod["precio_unitario"], reverse=True)


# print(f"\n---Stock Tienda---\n")
# print(f"El valor total es: ${valor_general:.2f}")
# print(f"El producto más costoso es: {mas_caro["nombre"]}. Valor: ${mas_caro["precio_unitario"]:.2f}")
# print(f"El producto más económico es: {menos_caro["nombre"]}. Valor: ${menos_caro["precio_unitario"]:.2f}")

# print(f"\nProductos con más stock")
# print(f"Productos con más de 20 unidades: {cantidad_productos} \ {mas_stock}\n")

# print(f"Lista de producto de mayor a menor.")
# for lista_orden in orden_stock:
#     print(f"Producto: {lista_orden["nombre"]}. Categoria: {lista_orden["categoria"]} Valor: ${lista_orden["precio_unitario"]}")



#🎭 Gestor de Reservas en un Teatro 🎭

# print("\n🎭 Gestor de Reservas en un Teatro 🎭\n")

# numero_reservas=int(input("Ingrese el número de reservas: "))
# reservas=[]
# seccion_teatro={"Vip": 0, "General": 0, "Balcon": 0}
# precio_boleto={"Vip": 50, "General": 30, "Balcon": 20}
# ventas_secciones={}


# for i in range(numero_reservas):
#         print(f"Reserva número: {i+1}")
#         nombre_espectador=str(input("Ingrese nombre del espectador: ")).title()
#         espectador=int(input(f"Ingrese la edad de: {nombre_espectador}: "))
        
#         # for _ in range(numero_reservas):
#         while True:
#             seccion=str(input("Sección deseada  (VIP, General o Balcón): ")).title()
#             if seccion in seccion_teatro:
#                 seccion_teatro[seccion] +=1
#                 break
#             else:
#                 print("Seccion inválida. Deber ser (VIP, General o Balcón): ")

#         reserva={
#             "nombre_espectador": nombre_espectador,
#             "edad": espectador,
#             "seccion": seccion 
#         }
#         reservas.append(reserva)

# espectador_mayor=max(reservas, key=lambda edad: edad['edad'] )
# espectador_menor=min(reservas, key=lambda edad: edad['edad'])

# # for ventas in seccion_teatro.items():
# #     if ventas in precio_boleto:
# #         ventas_secciones[ventas] = seccion_teatro[ventas] * precio_boleto[ventas]
# for seccion, cantidad in seccion_teatro.items():
#     ventas_secciones[seccion]= cantidad * precio_boleto[seccion]

# print(f"\n--Resumen Reservas---\n")
# print(f"El espectador mayor es: {espectador_mayor['nombre_espectador']} Edad: {espectador_mayor['edad']} años.")
# print(f"El espectador menor es: {espectador_menor['nombre_espectador']} Edad: {espectador_menor['edad']} años.")


# #Clave valor en el for
# for secc, cantidad  in seccion_teatro.items():
#     # print(f"Por cada sección se vendieron: \nVIP: {cantidad["Vip"]}. \nGeneral{cantidad["General"]}.\nBalcón: {cantidad["con"]}")
#     print("\n--Boletos vendidos---")
#     print(f"Sección {secc.capitalize()}: {cantidad} vendidos.\n")

# print(f"Ingresos por sección")
# for secc, venta in ventas_secciones.items():
#     print(f"-> {secc.capitalize()}: ${venta:.2f}")        
 
# venta_total=sum(ventas_secciones.values())
# print(f"Ingreso total del teatro: ${venta_total:.2f}\n")    

# for espectador in reservas:
#     if espectador["edad"] <= 18:
#         print(f"El espectador {espectador['nombre_espectador']} es menor de edad")
#     else:
#         print(f"El espectador {espectador['nombre_espectador']} es mayor de edad.") 


#  Ejercicio: Tienda de Descuentos

# print("\n--- Ejercicio: Tienda de Descuentos---\n")
# cantidad=int(input("Productos a comprar: "))
# total_compra=0


# for i in range(cantidad):
#     print(f"\nIngrese el precio\n")
#     precio=float(input(f"El producto {i+1} precio: $"))

#     if precio <50:
#         descuento=0
#         print(f"Producto sin descuento")
#         print(f"Total a pagar ${precio}")

#     elif precio <100:
#         descuento = precio - (precio * 0.05)
#         print(f"Producto con 5% de descuento")
#         print(f"Total a pagar ${precio}")

#     elif precio >= 100:
#         descuento = precio - (precio * 0.10)
#         print(f"Producto con el 10% de descuento")
#         print(f"Total a pagar ${precio}")

#     else:
#         print("Ingrese un valor válido") 

#     precio_final=precio - descuento   
#     total_compra+=precio_final

#     print(f"Total a pagar pro productos ${precio_final}") 

# print(f"\n---Resumen de compra---")
# print(f"\n---Total de la compra: ${total_compra} ---")
# print("Gracias por comprar")


# 🛒 Ejercicio: Tienda de Descuentos

# cantidad_productos=int(input("Ingrese la cantidad de productos: "))
# total=0

# for i in range(cantidad_productos):
#     precio=float(input(f"Ingrese el precio del producto {i+1}: $"))
#     total+=precio

#     if total < 50:
#         descuento=0
#     elif total<=100:
#         descuento= total * 0.05   
#     else:
#         descuento=total * 0.10

#     total_final= total - descuento

# print(f"\n---Resumen de la compra---")
# print(f"Total antes del descuento: ${total:.2f}")
# print(f"Descuento aplicado: ${descuento:.2f}")
# print(f"Total a pagar: ${total_final:.2f}")


# Ejercicio: Contar estudiantes por sección

# seccion_a=int(input("Estudiantes de sección A: "))
# seccion_b=int(input("Estudiantes de sección B: "))


# for i in seccion_a:
#     i+=1
#     print(f"En la sección A hay {i} estudiantes:")
#     for j in seccion_b:
#         j+=1
#         print(f"En sección B hay {j} estudiantes")

# total_estudiantes=sum(seccion_a + seccion_b)

# print(f"En total {total_estudiantes}")

# Inicializamos los contadores de estudiantes

# secciones={"A":0, "B": 0}

# for seccion in secciones:
#     cantidad=int(input(f"Ingrese la cantidad de estudiantes {seccion}: "))
#     secciones[seccion]=cantidad

# print(f"Estudiantes por sección")

# for sec, cantidad in secciones.items():
#     print(f"Sección {sec}: {cantidad} estudiantes")

# total_estudiantes=sum(secciones.values())
# print(f"Total de estudiantes en la escuela: {total_estudiantes}")

# total_estudiantes=list(secciones.keys())
# print(f"Total de estudiantes en la escuela: {total_estudiantes}")

# edad=int(input("Ingrese su edad: "))

# try:
#     if edad < 18:
#         print("Eres menor de edad no puede ingresar")
#     elif edad >= 18 and edad < 65:
#         print("Eres adulto, bienvenido")
#     elif edad >= 65 and edad < 100:
#         print("eres adulto mayor. Tienes descuento especial!")    
#     elif edad >= 100:
#         print(" Felicidades, eres una leyenda viva!")
# # else:
# #               
# except ValueError:
#     print("Ingrese un dato válido.") 

# 🎭 Adivina el personaje misterioso

# personaje=str(input("El personaje vuela? (Sí/No) "))
# personaje=["Capa", " No vuela", "Heroe"]

# print(f"🎭 Adivina el personaje misterioso 🎭\n ")

# def entrada_valida(pregunta, opciones):
#     while True:
#         respuesta = input(pregunta).strip().lower()
#         if respuesta in opciones:
#             return respuesta
#         print("Opción inválida. Intenta de nuevo!")    

# capa=entrada_valida(f"¿Usa capa? (Sí/No): ", ["sí", "no"] )
# vuela=entrada_valida(f"¿Puede volar? (Sí/No): ", ["sí", "no"])
# tipo=entrada_valida(f"¿Es un héroe o un villano? (Héroe/Villano): ", ["héroe", "villano"])

# if capa == "sí" and vuela == "sí" and tipo == "héroe":
#     print("Tu personaje podria ser Superman!")
# elif capa == "sí" and vuela == "no" and tipo == "héroe":
#     print("Tu personaje podría ser Batman!")
# elif capa == "sí" and vuela == "sí" and tipo == "villano":
#     print("Tu personaje podría ser Drácula!")
# elif capa == "no" and vuela == "sí" and tipo == "héroe":
#     print("tu personaje podría ser Iron Man")    
# elif capa == "sí" and tipo == "villano":
#     print("Tu personaje podria ser Guasón")          
# else: 
#     print("no conozco ese personaje... Intentalo de nuevo!")



#Lista Productos

# cantidad=int(input("¿cuántos productos desea añadir: "))
# productos=[]

# for i in range(cantidad):
#     print(f"Producto número {i+1}")
#     producto=input("Escribe el nombre del producto: ").title()

#     productos.append(producto)


# print("---Lista de productos---")
# for j in productos:

#     print(f"Producto: {j}")

# lista_compras=[]
# cantidad=int(input("Cantidad de productos: "))

# for i in range(cantidad):
#     producto=input(f"Ingrese el producto {i+1}: ").title()
#     lista_compras.append(producto)

# print("\n Tu lista de compras: ")
# for producto in lista_compras:
#     print(f"- {producto}") 
# print("\n Gracias")       


# fin=False
# lista_productos=[]

# while not fin:
#     print("Ingrese los productos de la lista")
#     producto=input("Producto: ").title()
#     lista_productos.append(producto)

#     print("Enter para continuar")
#     fin=input(f"Para terminar (fin): ").lower()

#     if fin == "fin":

#         fin=True

# print(f"---Lista de productos---")
# for producto in lista_productos:
#     print(f"- {producto}")


# lista_compras=[]

# print("\nTu lista de compras")
# print("Escribe 'fin' para terminar.\n")
# i=0

# while True:
#     # print(f"Producto {i+1} ")
#     producto=input("Ingrese un producto o 'fin' para terminar: ").strip().title()

#     if producto== "Fin":
#         break

#     lista_compras.append(producto)

# print("\n---Tu lista de compras ---")   
# for producto in lista_compras:
#     print(f"- {producto}") 

# print("\n---Gracias por la compra---\n")

#Carrera de Autos 🚗💨

# print("\n---Carreras de Autos---\n")
# participantes=int(input("Cuantos participantes hay: "))
# categoria_a=0
# categoria_b=0
# categoria_c=0
# tiempos=[]

# for i in range(participantes):
#     print(f"\nIngrese el tiempo en segundos.")
#     tiempo=float(input(f"Ingrese el tiempo del participante {i+1}: "))

#     tiempos.append(tiempo)

#     if tiempo <= 10:
#         categoria=+ tiempo
#         print(f"Carro de alto rendimiento")
#         print(f"El carro {i} tardo {tiempo} en terminar.")

#     elif tiempo > 10 or tiempo <= 20: 
#         categoria=+ tiempo 
#         print(f"Carro promedio")
#         print(f"El carro {i} tardo {tiempo} en terminar.")
#     else:
#         categoria=+ tiempo
#         print("Carro lento supero los 20 segundos")      
#         print(f"El carro {i} tardo {tiempo} en terminar.")


# autos_rapidos=0
# autos_promedio=0
# autos_lentos=0

# cantidad_autos=int(input("Ingrese cantidad autos en carrera: "))

# for i in range(cantidad_autos):
#     tiempo=float(input(f"Ingrese el tiempo de auto {i+1}: "))

#     if tiempo < 10:
#         autos_rapidos +=1
#     elif 10 <= tiempo <= 20:
#         autos_promedio +=1
#     else:
#         autos_lentos +=1   

# print(f"\n---Resultados Carrera---")            
# print(f"Autos de alto rendimiento {autos_rapidos}:")            
# print(f"Autos rendimeitno promedio {autos_promedio}")            
# print(f"Autos rendimeinto bajo {autos_lentos}")            

# print("\n---Restaurante Inteligente 🍽️---\n")
# platos=int(input("Cuántos platos ordenó? "))
# precios=[]


# for i in range(platos):
#     print(f"Plato {i+1}")
#     precio=float(input("Precio del plato: $"))

#     precios.append(precio)

# #  valor_general = sum(prod["valor_total"] for prod in productos)
# total=sum(prod for prod in precios )

# print("\n---Total a Pagar---\n")

# if total < 50:
#     print(f"Menos de $50. \nCliente económico.")
# elif 50 <= total <= 150:
#     print(f"Entre $50 y $150. \nCliente estandar.")
# else:
#     print(f"Más de $150. \nCliente VIP.")   

# print(f"Total a pagar ${total:.2f}")
# print("\n---Gracias por su compra---")


# print("\n---Restaurante Inteligente---")
# platos=int(input("¿Cuántos platos ordenó?: "))
# precios=[]

# for i in range(platos):
#     precio=float(input(f"Precio del plato {i+1}: $"))
#     precios.append(precio)

# total=sum(precios)

# print("\n---Total a pagar---\n")

# if total < 50:
#     print(f"Menos de $50. \nCliente Económico.")
# elif 50 <= total <= 150:
#     print(f"Entre $50 y $150. \nCliente Estándar.")
# else:
#     print(f"Más de $150. \nCliente VIP.")    

# print(f"\nTotal a pagar: ${total:.2f}")
# print("\n---Gracias por su compra---")        

# Cajero automatico

# print(f"\n---Cajero Automático---\n")
# pin=1234
# saldo=float(200)
# retiro=0
# nuevo_saldo=0

# pin_cuenta=int(input("Ingrese el pin: "))


# def consultar_saldo():
#     print(f"Saldo: ${saldo}")
#     return

# def retirar_dinero(saldo):
#     retiro=float(input("Cantidad a retirar: $ "))
#     saldo -= retiro   
#     return saldo

# def depositar_dinero(saldo):
#     nuevo_saldo=float(input("Ingrese la cantidad a depositar: $"))
#     saldo += nuevo_saldo
#     # saldo =depositar_dinero(saldo)
#     return saldo   

# def salir():
#     mensaje= print("Vuelva pronto")
#     return mensaje

# for i in range(1):
#     if pin == pin_cuenta:
#         print("Pin correcto!")
#         print(f"El Saldo de la cuenta es: {saldo}")

#         def menu():
#             while True:
#                 print(f"\n---Menú---")
#                 print(f"1 - Consultar Saldo: ")
#                 print(f"2 - Retirar dinero")
#                 print(f"3 - Depositar dinero")
#                 print(f"4 - Salir")

#                 opcion=input("Elige una opción:")

#                 if opcion.isdigit():
#                     opcion=int(opcion)

#                     match opcion:
#                         case 1:
#                             consultar_saldo()
#                         case 2:
#                             retirar_dinero()
#                         case 3:
#                             depositar_dinero(saldo)
#                         case 4:
#                             salir()
#                             break     
#                         case _:
#                             print("Opción inválida vuelva pronto.")
#             else:
#                 print("Ingrese un numero válido")        

#     elif pin != pin_cuenta:
#         for i in range(3):
#             print(f"Intento {i+1}")
#             print("El PIN es incorrecto: ingrese nuevamente")

# menu()

# print("\n--Cajero automático---")
    
# PIN_CORRECTO="1234"
# saldo=2000.0
# intentos=3

# def consultar_saldo():
#     # print("---Muestra el saldo actual---")
#     print(f"Saldo disponible: ${saldo:.2f}")

# def retirar_dinero():
#     global saldo
#     retirar = float(input("Ingrese la catidad a retirar: "))

#     if retirar > saldo:
#         print("Fondos Insuficientes!")
#     elif retirar <= 0:
#         print("Monto inválido!")
#     else:
#         saldo -= retirar
#         print(f"Retiro exitoso, Saldo actudal: {saldo:.2f}")         


# def depositar_dinero():
#     # print("Retirara dinero si hay saldo suficiente")   
#     global saldo
#     deposito = float(input("Ingrese la cantidad a depositar: "))

#     if deposito <= 0:
#         print("Monto inválido")
#     else:
#         saldo += deposito
#         print(f"Deposito exitoso. Saldo actual: ${saldo:.2f}")    

# def menu():

#     while True:
#         print(f"\n --- Menú ---")
#         print(f"1 Consultar Saldo")
#         print(f"2 Retirar dinero")
#         print(f"3 Depositar dinero")
#         print(f"4 salir")

#         opcion=input("Elige una opción: ")

#         if opcion.isdigit():
#             opcion=int(opcion)

#             if opcion==1:
#                 consultar_saldo()
#             elif opcion==2:
#                 retirar_dinero()
#             elif opcion==3:
#                 depositar_dinero()
#             elif opcion==4:
#                 print("Gracias por usar el cajero. \nHasta Pronto!")  
#             else:
#                 print("Opción inválida!")
#         else:
#             print("Ingrese un número válido")                      

# for intento in range(intentos):
#     pin_ingresado=str(input("Ingrese su PIN: "))

#     if pin_ingresado==PIN_CORRECTO:
#         print("Acceso permitido.")
#         menu()
#         break
#     else:
#         print(f"Pin incorrecto. \nIntentos restantes: {intentos - intento - 1}")

# else:
#     print("Cueta bloqueada por seguridad!")


# 📌💰 Cajero Automático con global y if

# saldo=1000
# PIN_CORRECTO="1234"
# intentos=3

# def consultar_saldo():
#     # global saldo
#     print(f"El saldo d etu cuenta es: ${saldo:.2f}")

# def depositar_saldo():
#     global saldo   
#     consignar=float(input("Ingrese la cantidad a consignar: $"))

#     if consignar < 0 :
#         print("Monto inválido")
#     else:
#         saldo += consignar
#         print(f"Deposito exitoso. \nNuevo saldo: ${saldo:.2f}")   

# def retirar_saldo():
#     global saldo
#     retirar=float(input("Cantidad a retirar: $"))  

#     if retirar > saldo:
#         print("Saldo insuficiente")
#     else:
#         saldo -= retirar
#         print(f"Retiro Exitoso. \nNuevo saldo {saldo:.2f}")    

# def menu():

#     while True:
#         print("\n---Menu Cajero---")
#         print("1 - Consultar Saldo.")          
#         print("2 - Depositar Saldo.")          
#         print("3 - Retirar Dinero.") 
#         print("4 - Salir.\n") 

#         opcion=input("Digita la opción: ")         

#         if opcion.isdigit():
#             opcion = int(opcion)

#             if opcion == 1:
#                 consultar_saldo()
#             elif opcion == 2:
#                 depositar_saldo()
#             elif opcion == 3:
#                 retirar_saldo()
#             elif opcion == 4:
#                 print("Gracias por utilizar el cajero.")
#                 break    
#             else:
#                 print("Ingrese un número válido.")   

#         else:
#             print("Ingrese un dato válido.")                         
      

# for i in range(intentos):
#     ingrese_pin=str(input("Ingrese PIN: "))

#     if ingrese_pin == PIN_CORRECTO:
#         print("Acceso permitido!")
#         menu()
#         break
#     else:
#         print(f"intentelo nuevamente. \nIntentos Restantes {intentos - intentos - 1}")


# saldo=1000
# PIN_CORRECTO="1234"
# intentos=3

# def consultar_saldo():
#     print(f"Tu saldo actual es ${saldo:.2f}")

# def depositar_saldo():
#     global saldo

#     try:
#         consignar=float(input(f"Ingrese la cantidad a consignar: $"))
#         if consignar<=0:
#             print("Monto inválido. Dbe ser mayor que 0.")
#         else:
#             saldo+=consignar
#             print(f"Deposito exitoso. \nNuevo saldo: ${saldo:.2f}")    

#     except ValueError:
#         print("Ingrese un número válido.")        

# def retirar_saldo():
#     global saldo

#     try:
#         retirar=float(input("Ingrese la cantidad a retirar: $"))
#         if retirar<=0:
#             print("Monto inválido. Debe ser mayor que 0.")
#         elif retirar > saldo:
#             print("Saldo insuficiente.")
#         else:
#             saldo -= retirar
#             print(f"Retiro exitoso. Nuevo saldo: ${saldo}")      
#     except ValueError:
#         print("Ingrese un número válido.")          

# def menu():
#     while True:
#         print("\n---Menú Cajero---")
#         print("1 - Consultar Saldo.")
#         print("2 - Depositar Dinero.")
#         print("3 - Retirar Dinero.")
#         print("4 - Salir.")

#         opcion=input("Digita la opción: ")

#         if opcion.isdigit():
#             opcion=int(opcion)
#             if opcion==1:
#                 consultar_saldo()
#             elif opcion==2:
#                 depositar_saldo()
#             elif opcion==3:
#                 retirar_saldo()
#             elif opcion==4:
#                 print("Gracias por utilizar nuestros cajeros.") 
#                 break
#             else:
#                 print("Ingrese un número válid.")           
#         else:
#             print("Ingrese un número válido.")

# for i in range(intentos, 0, -1):
#     ingrese_pin=input("Ingrese tu PIN:")  

#     if ingrese_pin==PIN_CORRECTO:
#         print("PIN correcto")
#         menu()
#         break
#     else: 
#         print(f"PIN incorrecto. Intentos restantes: {i-1}")

#         if i-1==0:
#             print("Cuenta Bloqueada. \nDemasiado intentos fallidos")             




# print("hola")


# PROMEDIO

# print("Ingrese 3 numeros")
# lista=3
# numeros=()

# for i in range(lista):
#     print(f"Ingrese el numero {i+1}")
#     numero=input("Numero: ")

#     if numero.isdigit():
#         numero=int(numero)

#         for j in numero:
#             suma=sum(j)
#             resultado = suma/lista

#             print(f"El promedio de {j} es: {resultado}")

#         else:
#             print("error")  

#     else:
#         print("Ingrese un valor válido")         


# print("Ingresa 3 números")
# #Crea una lista vacia para almacenar los numeros
# numeros=[]

# #Solicita 3 numeros al usuario. 
# for i in range(3):

#     while True:
#         numero=input(f"Ingrese el número {i+1}: ")

#         #verifica que la entrada sea un números
#         if numero.isdigit():
#             numero=int(numero)
#             numeros.append(numero) #Agregar a la lista
#             break
#         else:
#             print("Error ingrese un número válido.")

# #Calcular la suma y el promedio
# suma=sum(numeros)
# promedio=suma/len(numeros)          

# #mostrar el resultado
# print(f"\nLa suma de los núemros es: {suma}")
# print(f"El promedio de los números es: {promedio:.2f}")

# num1=float(input("Ingresa el primer nùmero: "))
# num2=float(input("Ingresa el segundo nùmero: "))
# num3=float(input("Ingresa el tercer nùmero: "))

# promedio=(num1 + num2 + num3 ) / 3

# print(f"El promedio de los números ingresados es: {promedio:.2f}")


# print("---Promedio de Números---")
# numeros=[]

# for i in range(3):
#     print(f"Ingresa el números {i+1}")
#     numero=input("Numero: ")

#     while True:
#         if numero.isdigit():
#             numero=int(numero)
#             numeros.append(numero)
#             break
#         else:
#             print("Ingrese un número válido")
#     else:
#         print("Ingresa un dato válido")        


# suma=sum(numeros)
# promedio=suma/len(numeros) 

# mas_alto=max(numeros, key=lambda m: m in numeros)    
# mas_bajo=min(numeros, key=lambda m: m in numeros)   


# print("\n---Promedio---")
# print(f"El promedio es: {promedio:.2f}")
# print(f"Número más bajo: {mas_bajo}")
# print(f"Número más alto: {mas_alto}")


# print("---Promedio Números---")
# numeros=[]

# #Solicitar 3 numeros al usuario
# for i in range(3):
#     while True:
#         numero=input(f"Ingresa el número {i+1}: ")

#         if numero.isdigit():
#             numero=int(numero)
#             numeros.append(numero)
#             break
#         else:
#             print("Error: Ingrese un número válido.")

# # Calcular la suma y el promedio
# suma=sum(numeros)
# promedio=suma/len(numeros)

# # Encontrar el número más alto y el más bajo
# mas_alto=max(numeros)
# mas_bajo=min(numeros)

# # Mostrar resultados
# print(f"\n---Resultados---")
# print(f"El promedio es: {promedio:.2f}")
# print(f"Números más  alto: {mas_alto}")
# print(f"Números más  bajo: {mas_bajo}")


# metros=float(input("Ingresa la distancia en metros: "))

# kilometros=1000
# centimetros=100
# milimetros=1000

# kilometros= metros / kilometros
# centimetros= metros * centimetros
# milimetros= metros * milimetros

# print(f"\nConvertidor de MT \n")
# print(f"{metros} mt son: {kilometros:.2f} kilometros.")
# print(f"{metros} mt son: {centimetros} centímetros.")
# print(f"{metros} mt son: {milimetros} milimetros.")


# print("---Converso de Unidades de Longitud---")

# while True:

#     metros=input("Ingrese la distancia en metros: ")

#     if metros.replace(".","",1).isdigit():
#         metros=float(metros)
#         break
#     else:
#         print("Error: Ingrese un número válido.")

# kilometros= metros / 1000
# centimetros= metros * 100
# milimetros= metros * 1000

# print(f"\n---Convertidor MT---\n")
# print(f"{metros} mt son: {kilometros:.2f} kilómetros.")
# print(f"{metros} mt son: {centimetros:.2f} centímetros.")
# print(f"{metros} mt son: {milimetros:.2f} milímetros.")


# print("\n---Notas de Estudiantes---\n")
# notas=[]

# for i in range(4):
#     while True:
#         print(f"\nNota {i+1}.")
#         nota=float(input("Introduce la nota: "))

#         if 0.0 <= nota <= 5.0:
#             nota=float(nota)
#             notas.append(nota)
#             break
#         else:
#             print("\nIngrese un número entre 0.0 y 5.0\n")

# nota_alta=max(notas)            
# nota_baja=min(notas)

# sumas=sum(notas)
# promedio=sumas/len(notas)

# print("\n---Nota Final---")
# print(f"Estudiante con promedio: {promedio:.2f}")
# print(f"Nota mas alta: {nota_alta:.2f}")
# print(f"Nota más baja: {nota_baja:.2f}")

# if  promedio >= 3.0:
#     print(f"Estudiante Aprobado. \nPromedio: {promedio:.2f}") 
#     print("Felicidades Pasaste!")
# else:
#     print(f"Estudiante Reprobado. \nPromedio: {promedio:.2f}") 
#     print("Debes repetir la materia!")   

# print("\n---Notas de Estudiantes---\n")
# notas=[]

# #Pedir 4 notas
# for i in range(4):
#     while True:
#         nota=input(f"\nNota {i+1}: ")

#         #validas que la entrada sea un número
#         if nota.replace(".","",1).isdigit():
#             nota=float(nota)

#             if 0.0 <= nota <= 5.0:
#                 notas.append(nota)
#                 break
#             else:
#                 print("\nError: La nota debe estar entre .0. y 5.0\n")
#         else:
#             print("\nError: Ingrese un número válido\n")

# #Cálculos de notas

# nota_alta=max(notas)
# nota_baja=min(notas)
# promedio=sum(notas)/len(notas)

# #Mostrar resultado
# print(f"\n--- Nota Final ---")
# print(f"Promedio del estudiante: {promedio:.2f}")
# print(f"Nota más alta: {nota_alta:.2f}")
# print(f"Nota más baja: {nota_baja:.2f}")

# #evaluacion de aprobación o reprobación

# if promedio >= 3.0:
#     print("\nEstudiante Aprobado ")
#     print("Felicidades, pasaste!")
# else:
#     print("\nEstudiante Reprobado")    
#     print("Debes repetir lña materia.")    


# print("--- Sistema de Notas ---")
# notas=[]

# #Pedir 4 notas
# for i in range(4):
#     while True:
#         nota=input(f"Ingrese la nota {i+1} (0 - 5): ")

#         if nota.replace(".","",1).isdigit():
#             nota=float(nota)

#             if 0 <= nota <= 5:
#                 notas.append(nota)
#                 break
#             else:
#                 print("Error: La nota debe estar entre 0 y 5")
#         else:
#             print("Error. Ingrese un número válido.")        

# #calcular promedio
# promedio=sum(notas)/len(notas)

# #Calcular nota alya y nota baja
# nota_alta=max(notas)
# nota_baja=min(notas)

# #Determinar si aprueba o no
# estado="Aprobado" if promedio >= 3.0 else "Repropbado"

# #Mostrar Resultados
# print("\n--- Resultados ---")
# print(f"Promedio: {promedio:.2f}")
# print(f"Nota más alta: {nota_alta}")
# print(f"Nota más baja: {nota_baja}")
# print(f"Estado: {estado}")


# numero=int(input("Escribe un dumero par entre 0 y 20: "))

# par= "Es par" if numero % 2 == 0 else "Es impar"

# print(f"El numero es: {par}")

# edad=int(input("Ingrese su edad: "))

# mayor_edad="mayor de edad" if edad >=18 else "menor de edad"

# print(f"La persona es, {mayor_edad}")

# print("Ingrese dos numeros de 2 digitos del (00 - 99)")
# numero_a=int(input("Primer número: "))
# numero_b=int(input("Segundo numero:"))

# mayor= numero_a if numero_a > numero_b  else numero_b

# print(f"El numero mayor es: {mayor}")


# numero=int(input("Ingrese un numero: "))

# resultado= "par" if numero % 2 == 0 else "impar"

# print(f"El numero {numero} es {resultado}")

# numero=int(input("Ingrese un numero: "))

# cuadrado=lambda x: x ** 2

# print(f"El numero es: {cuadrado(numero)}")

# numero_b=int(input("Número a: "))
# numero_c=int(input("Número b: "))

# resultado=lambda a, b: a if a > b else b

# print(f"El número mayor es: {resultado(numero_b,numero_c)}")

# (0°C × 9/5) + 32 = 32°F

# grados=float(input("Convertidor de Celsius a Fahrenheit: "))

# grados={5,88,35}

# celcius=0
# fahrenheit=32

# resultado=lambda a: (a * 9/5) + 32 
# # resultado_a=lambda a: for a in grados 

# print(f"{grados}° Celsius son {resultado(grados):.0f}° Fahrenheit.")


# grados={5,35,8, 23}

# grados_lista=list(grados) #List convierte set, tupla, string a una lista

# clasificacion=list(map(lambda g: "Caliente" if g >= 22 else "Frío", grados_lista ))
# print(clasificacion)

# clasificacion_1=["Caliente" if g >= 22 else "Frio" for g in grados_lista]
# print(clasificacion_1)
# numeros=[-3, 0, 7, -1, 8]
# numeros_lista=list(numeros)
# clasificiacion=list(map(lambda g: "Positivo" if g >= 0 else "Negativo", numeros_lista))
# print(clasificiacion)

# (0°C × 9/5) + 32 = 32°F
# clasificacion=list(map(lambda g: "Caliente" if g >= 22 else "Frío", grados_lista ))
# # 
# fahrenheit = [32, 212, 98.6, 50]
# fahrenheit_lista =list(fahrenheit)
# resultado=list(map(lambda g: fahrenheit_lista(0 * 9/5 ) + 32, fahrenheit_lista))
# print(resultado)
# fahrenheit = [32, 212, 98.6, 50]
# resultado=list(map(lambda g: (g-32) * 5/9, fahrenheit))
# print(resultado)

# nombres = ["Ana", "Sebastián", "Luis", "Valeria", "Paco"]

# resultado=list(map(lambda g: "Largo" if len(g) >= 5 else "Corto",  nombres))

# print(resultado)

# nombres = ["Ana", "Sebastián", "Luis", "Valeria", "Paco"]

# resultado=list(map(lambda g: "Muy largo" if len(g) >7  "Largo" elif len(g) >=5 else "Corto", nombres ))

# print(resultado)

# nombres = ["Ana", "Sebastián", "Luis", "Valeria", "Paco"]

# resultado=list(map(lambda g: "Muy Largo" if len(g) > 7 else "Largo" elif len(g) >= 5 else "Corto", nombres))

# # resultado = list(map(lambda g: "Muy largo" if len(g) > 7  "Largo" elif len(g) >= 5 else "Corto", nombres))

# nombres = ["Ana", "Sebastián", "Luis", "Valeria", "Paco"]

# resultado=list(map(lambda g: "Muy Largo" if len(g) > 7 else ("Largo" if len(g) >= 5 else "Corto"), nombres))
# print(resultado)

# palabra=str(input("Ingrese una palabra: "))

# palabras=["a","e","i","o","u"]

# if palabra in palabras:
#     total_vocales=len(palabras)
#     print(f"Hay {total_vocales} vocales")
# else:
#     print(f"NN")    

# print("---Contador de Vocales---")

# texto=input("Ingrese una palabra: ").lower()
# vocales="aeiou"
# contador=0

# for letra in texto:
#     if letra in vocales:
#         contador+=1

# print(f"\nNúmero de vocales: {contador}")        

# print("---Contador Vocales---")

# palabra=input("Ingrese palabra y/o frase: ").lower()
# vocales=["a","e","i","o","u","á","é","í","ó","ú","ü"]
# total_vocales=0

# for letra in palabra:
#     if letra in vocales:
#         total_vocales+=1

# print(f"\nLa palabra {palabra.upper()} \nTotal {total_vocales} vocales ")


# print("\n---Adivina numero---\n")

# numero_secreto=8
# intentos=3

# for i in range(intentos):
#     print(f"Intento número: {i+1}")
#     numero=int(input("Ingrese un número "))
#     while intentos:
    
#         if numero == numero_secreto:
#             print(f"\nAdvinaste el numero secreto! \n {numero_secreto} Es el número secreto\n")
#             break
#         elif numero > numero_secreto:
#             print(f"\nTe pasaste. \nEstas cerca, sigue intentando.\n")
#             break
#         elif numero < numero_secreto:
#             print(f"\nTe falta. \nEstas cerca sigue intentando\n") 
#             break
#         else:
#             print("Error")
#             break       

# print(f"Gracias por jugar")


# def jugar():
#     numero_secreto=random.randint(1,10)
#     intentos=3

#     print(f"\nBienvenido al juego de Adivina el número!\n")
#     print(f"Tiene {intentos} Intentos")

#     for i in range(intentos):
#         while True:
#             intento=input(f"Intento {i+1} Ingresa un número: ")

#             if intento.isdigit():
#                 intento=int(intento)
#                 break
#             else:
#                 print("Error: Ingresaun número válido.")

#         if intento == numero_secreto:
#             print(f"\nFelicidades Adivinaste!\nEl número secreto es {numero_secreto}")
#             return
#         elif intento < numero_secreto:
#             print("El número secreto es mayor.")
#         else:
#             print("El número secreto es menor.")    

#     print(f"\nLo siento, has agotado tus intentos. \nEl número secreto es: {numero_secreto}")        

# jugar()


# print("---Calculadora de Números Primos---")

# #resultado= "par" if numero % 2 == 0 else "impar" 
 
# def datos():
#     entero=input("Ingrese un numeros entero positivo: ")
#     return entero

# def calcular(numero):
#     resultado = "par" if numero % 2 == 0 else "impar"
#     return resultado


# def numeros_primos():
#     salida = print(f"El numero es {calcular(datos())}")
#     return salida

# datos()


# def es_primo(numero):
#     """Función que verifica si un número es primo."""
#     if numero < 2:
#         return False #Numeros menores a 2 no son primos
    
#     for i in range(2, int(numero ** 0.5) + 1): #probar Divisores
#         if numero % i == 0:
#             return False #Si es divisible, no es primo
#     return True   # Si no se encontró divisores, es primo    

# #Pedir numero al USER
# while True:
#     num=input("Ingrese un numero entero positivo: ")

#     if num.isdigit(): # Verifica que sea un número válido
#         num=int(num)
#         break
#     else:
#         print("Error: Ingrese un úmero entero válido.")

# # Llamar a la función y mostrar el resultado
# if es_primo(num):
#     print(f"El número {num} es primo.") 
# else:
#     print(f"El número {num} NO es primo.")                 


# print("\n---Calculadora de Compra en una Tienda de Comida---\n")
# productos=[]
# descuento=float(10)

# for i in range(3):
#     print(f"Producto {i+1}: ")    
#     nombre_producto=str(input("nombre producto: ")).title()
#     precio_producto=float(input("Ingrese precio: $"))
#     cantidad_producto=int(input("Ingrese cantidad: "))
#     precio_general=float(0)

#     producto={
#         "nombre_producto": nombre_producto,
#         "precio_producto": precio_producto,
#         "cantidad_producto": cantidad_producto, 
#         "precio_general": precio_producto * cantidad_producto 
#     }

#     productos.append(producto)

# precio_total=sum(producto["precio_general"] for producto in productos)

# if precio_total > 20:
#     descuento= precio_total * ( descuento / 100) 
#     total=precio_total - descuento
#     print(f"\nPrecio sin descuento ${precio_total:.2f} ")
#     print(f"Precio con descuento ${total:.2f}")
# else:
#     print(f"\nPrecio sin descuento {precio_total}")    

# print("---Calculadora de Compra Tienda Comida---")

# productos=[]
# descuento=10

# for i in range(3):

#     print(f"\nProductos {i+1}")
#     nombre_producto=input("Nombre del producto: ").title()

#     while True:
#         try:
#             precio_producto=float(input("ingresa precio: $"))
#             cantidad_producto=int(input("ingresa cantidad: "))

#             if precio_producto > 0 and cantidad_producto > 0:
#                 break
#             else:
#                 print("Error: Precio y cantidad deben ser mayores a 0")
#         except ValueError:
#             print("Error: Ingrese valores numéricos válidos.")

#     precio_general=precio_producto * cantidad_producto

#     productos.append({
#         "nombre_producto": nombre_producto,
#         "precio_producto": precio_producto,
#         "cantidad_producto": cantidad_producto,
#         "precio_general": precio_general
#     })        

# precio_total=sum(producto["precio_general"] for producto in productos)

# print(f"\n---Resumen de Compra---\n")

# for producto in productos:
#     print(f"{producto["nombre_producto"]}: {producto["cantidad_producto"]} x ${producto["precio_producto"]:.2f} = ${producto["precio_general"]:.2f}")

# if precio_total > 20:
#     descuento_aplicado=precio_total * (descuento / 100)
#     total_final=precio_total - descuento_aplicado
#     print(f"\nPrecio sin descuento: ${precio_total:.2f}")
#     print(f"Descuento aplicado ${descuento_aplicado:.2f}")
#     print(f"Precio con descuento ${total_final:.2f}")
# else:
#     print(f"\nPrecio total a pagar: ${precio_total}")

# print("---Gracias por su compra---")        


# print("\n---Bienvenido a la Tienda de Comida ---\n")

# def obtener_datos():

#     nombre=input("Nombre del producto: ").title()

#     while True:
#         try:
#             precio=float(input(f"Precio de{nombre}: $"))
#             cantidad=int(input(f"Cantidad de {nombre}: "))

#             if precio > 0 and cantidad > 0:
#                 break
#             else:
#                 print("Error: Precio y cantidad deben ser mayor a cero.-")
#         except ValueError:
#             print("Error: Ingrese valores númericos válidos.")

#     return nombre, precio, cantidad        

# def calcular_total(productos):
#     subtotal=sum(precio * cantidad for _, precio, cantidad in productos)
#     descuento=subtotal* 0.10 if subtotal > 20 else 0
#     total_final=subtotal - descuento

#     return subtotal, descuento, total_final

# def mostrar_resumen(productos, subtotal, descuento, total_final):

#     print("\n---Resumen de Compra---")

#     for nombre, precio, cantidad in productos:
#         print(f"{nombre}: {cantidad} x ${precio:.2f} = ${precio *cantidad:.2f}")

#     print(f"\nTotal antes del descuento: ${subtotal:.2f}")

#     if descuento > 0:
#         print(f"Descuento Aplicado: ${descuento:.2f}")
#     print(f"Total a pagar: ${total_final}")    

# productos=[obtener_datos() for _ in range(3)]

# subtotal, descuento, total_final= calcular_total(productos)

# mostrar_resumen(productos, subtotal, descuento, total_final)

# print("---Comparador de Edades---")

# def pedir_edades():
#     edad_uno=int(input("Ingrese su edad: "))
#     edad_dos=int(input("Ingrese su edad: "))
#     return edad_uno, edad_dos


# def comparar_edades(uno, dos):    

#     if uno > dos:
#         print(f"La edad {uno} es mayor")
#     elif uno < dos:
#         print(f"la edad {dos} es mayor")
#     else:
#         print(f"Edad {uno} y edad {dos} son iguales.") 


# edad1, edad2 = pedir_edades()
# comparar_edades(edad1,edad2)              


# print("\n---Comparador de Edades---")

# def obtener_edad(persona):
#     while True:
#         try:
#             edad=int(input(f"Ingrese la edad de la persona {persona}: "))
#             if edad > 0:
#                 return edad
#             else:
#                 print("Error. La edad debeb ser mayor a 0.")
#         except ValueError:
#             print("Error. Ingrese un número entero válido.")        

# def comparar_edades(edad1, edad2):
#     if edad1 > edad2:
#         print(f"\nLa persona 1 es mayor con {edad1} años.")
#     elif edad1 < edad2:
#         print(f"\nLa persona 2 es mayor con {edad2} años.")
#     else:
#         print(f"\nAmbas personas tienen la misma edad {edad1} años.")

# edad_persona1=obtener_edad(1)
# edad_persona2=obtener_edad(2)

# # comparar_edades(edad_persona1, edad_persona2)

# print("---Clasificador de Números Positivos y Negativos---")

# def pedir_numeros():
#     numeros=[]
#     for i in range(5):
#         while True:
#             try:
#                 numero=int(input(f"Escriba el {i+1} numero: "))
#                 numeros.append(numero)
#                 break
#             except ValueError:
#                 print("Escriba un número válido.")        
#     return numeros

# def comparar_numeros(numero):
#     if numero > 0:
#         print(f"El número {numero}  es positivo.")
#     elif numero < 0:
#         print(f"El número {numero} es negativo.")  
#     else:
#         print(f"El número {numero} es cero.")      

# lista_numero=pedir_numeros()

# for num in lista_numero:
#     comparar_numeros(num)

# print("---Clasificador de números---")

# def clasificar_numeros(lista_numeros):
#     positivos=[]
#     negativos=[]

#     for num in lista_numeros:
#         if num > 0:
#             positivos.append(num)
#         elif num < 0:
#             negativos.append(num)

#     return positivos, negativos            

# numeros=[]
# for i in range(5):
#     while True:
#         try:
#             numero=int(input(f"Ingrese el número {i+1}: "))
#             numeros.append(numero)
#             break
#         except ValueError:
#             print("Error: Ingrese un número válido.")

# positivos, negativos =clasificar_numeros(numeros)

# print(f"\n✅ Números Positivos: {positivos}" if positivos else "🔴 no hay números positivos.")
# print(f"🔴 Números Negativos: {negativos}" if negativos else "✅ no hay números positivos.")

# if 0 in numeros:
#     print("🔵 El número 0 no es ni negativo ni positivo.")

# ---------Crea un programa que:
# ✅ Genere automáticamente 10 números aleatorios entre -20 y 20.
# ✅ Use la biblioteca random para generar los números.
# ✅ Use función (def) para clasificar los números en pares e impares.
# ✅ Use for para recorrer los números y if para la clasificación.-

# print("---Clasificador de Números Pares e Impares con random---")
# par=[]
# impar=[]
# numeros=[random.randint(-20,20) for _ in range(10)]

# def clasificar_numeros(numeros):

#     for num in numeros:
#         if num % 2 == 0:
#             par.append(num)
#         elif num % 2 != 0:
#             impar.append(num)
#     return par, impar        

# par, impar=   clasificar_numeros(numeros)     

# print(f"Número Par: {par}" if par else "No hay números pares")
# print(f"Número Impar: {impar}" if impar else "No hay números impares ")

# if 0 in numeros:
#     print("El número 0 no es positivo ni negativo.")


# print("---Clasificador de Números Pares e Impares---")

# def clasificar_numeros(lista_numeros):
#     pares=[]
#     impares=[]

#     for num in lista_numeros:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)    
    
#     return pares, impares

# numeros=[random.randint(-20, 20) for _ in range(10)]

# pares, impares=clasificar_numeros(numeros)

# print(f"\nNúmeros generados: {numeros}")
# print(f"\nNúmeros Pares: {pares}" if pares else "No hay números pares")
# print(f"Números Impares: {impares}" if impares else "No hay números impares.")

# if 0 in numeros:
#     print(f"El número 0 no es ni positivo ni negativo.")



# print("---Clasificador de Libros y Marcas de Autos---")

# lista_nombres=["Mercedes Benz",
#                     "Audi",
#                     "Porsche",
#                     "Maserati",
#                     "BMW",
#                     "Ferrari",
#                     "Lexus",
#                     "Toyota",
#                     "Chevrolet",
#                     "Jeep",
#                     "El Hombre en busca de Sentido",
#                     "Don Quijote",
#                     "A Tale of Two Cities",
#                     "The Little Prince",
#                     "Harry Potter and the Philosopher's Stone",
#                     "And Then There Were None",
#                     "The Hobbit",
#                     "Alice's Adventures in Wonderland",
#                     "The Lord of the Rings",
#                     "Aprende Python" 
#                     ]

# def clasificador(lista):
#     carros=[]
#     libros=[]

#     lista_general=random.sample(lista_nombres, k=min(10, len(lista_nombres)))


#     for nombres in lista_general:
#         if nombres in ["Mercedes Benz","Audi","Porsche","Maserati","BMW","Ferrari","Lexus","Toyota","Chevrolet","Jeep"]:
#             carros.append(nombres)
#         elif nombres in  [   "El Hombre en busca de Sentido","Don Quijote","A Tale of Two Cities","The Little Prince","Harry Potter and the Philosopher's Stone","And Then There Were None","The Hobbit","Alice's Adventures in Wonderland","The Lord of the Rings","Aprende Python" ]:
#             libros.append(nombres)

#     return carros, libros

# # pares, impares=clasificar_numeros(numeros)

# carros, libros=clasificador(lista_nombres)

# print(f"\nLa lista de libros es:\n")
# for i in libros:
#     print(f"{i}")

# print(f"\nLa lista de carros es:\n")
# for j in carros:
#     print(f"{j}")

# print(f"\nLista completa de elementos {lista_nombres}")

# print("\n📚🚗 ---Clasificador de Libros y Marcas de Autos--- 📚🚗")

# autos = ["Mercedes Benz", "Audi", "Porsche", "Maserati", "BMW", 
#          "Ferrari", "Lexus", "Toyota", "Chevrolet", "Jeep"]

# libros = ["El Hombre en busca de Sentido", "Don Quijote", "A Tale of Two Cities", 
#           "The Little Prince", "Harry Potter and the Philosopher's Stone", 
#           "And Then There Were None", "The Hobbit", "Alice's Adventures in Wonderland", 
#           "The Lord of the Rings", "Aprende Python"]

# lista_nombres= autos + libros

# def clasificador(lista):

#     seleccionados=random.sample(lista, k=min(10, len(lista)))
#     carros=[nombre for nombre in seleccionados if nombre in autos]
#     libro=[nombre for nombre in seleccionados if nombre in libros]

#     return carros, libro, seleccionados

# carros, libro, seleccionados= clasificador(lista_nombres)

# print(f"\n Lista aleatoria selecionadda: \n{seleccionados}")
# print(f"\nLibros encontrados: ")
# print(f"\n".join(libros) if libros else "No hay liebros seleccioandos")
# print(f"\nMarcas de autos encontradas: ")
# print(f"\n".join(carros) if carros else "No hay autos seleccionados.")


# print("\n📚🚗 --- Clasificador de Libros y Marcas de Autos --- 📚🚗")

# # Listas de libros y marcas de autos
# libros = ["1984", "Cien años de soledad", "Don Quijote", "El Principito", "Harry Potter",
#           "Los Juegos del Hambre", "Moby Dick", "Orgullo y Prejuicio", "El Hobbit", "Dune"]

# autos = ["Toyota", "Ford", "Chevrolet", "Honda", "BMW",
#          "Mercedes", "Audi", "Nissan", "Volkswagen", "Tesla"]

# elementos= libros+autos

# def clasificar_elementos(lista_elementos):
#     clasificacion_libros=[]
#     clasificacion_autos=[]

#     for item in lista_elementos:
#         if item in libros:
#             clasificacion_libros.append(item)
#         elif item in lista_elementos:
#             clasificacion_autos.append(item)

#     return clasificacion_libros, clasificacion_autos    

# elementos_aleatorios=random.sample(elementos, 10)        

# libros_seleccionados, autos_seleccionados=clasificar_elementos(elementos_aleatorios)

# print(f"\nElementos seleccionados: {elementos_aleatorios}")
# print(f"\nLibros: {libros_seleccionados}"   if libros_seleccionados else "No hay libros seleccionados.")
# print(f"Autos: {autos_seleccionados}" if autos_seleccionados else "No hay autos seleccionados.")

# import random
# print("---Registro de Estudiantes en una Biblioteca---")

# estudiantes = [
#     "Ana López", "Luis Torres", "Elena Ruiz", "Pablo Gómez", "Marta Díaz",
#     "Diego Cruz", "Clara Méndez", "Jorge Ríos", "Sofía Lara", "Bruno Navas",
#     "Alejandra Ramírez", "Guillermo Fernández", "Valentina Rodríguez", "Maximiliano González", 
#     "Isabella Montenegro", "Cristóbal Benavides", "Montserrat Villanueva", 
#     "Emiliano Santamaría", "Gabriela Castellanos", "Leandro Bustamante"
#     ]

# def prestamos_libros(libros_prestados):
#     aula=[]
#     biblioteca=[]

#     for estudiante in libros_prestados:
#         if len(estudiante) <= 10:
#             aula.append(estudiante)
#         elif len(estudiante) >= 11:
#             biblioteca.append(estudiante)
    
#     return  aula, biblioteca       

# # elementos_aleatorios=random.sample(elementos, 10) 
# estudiantes_aleatorios=random.sample(estudiantes, 10)

# aula, biblioteca = prestamos_libros(estudiantes_aleatorios)

# print(f"\n---Lista de Estudiantes---")
# print(f"\nEstudiantes con prestamos de libros: {biblioteca}" if aula else "No hay estudiantes en esta sección." )
# print(f"Estuduantes en Aula de estudio {aula}" if aula else "no hay estudiantes en el aula.")


# print("\n📚 --- Registro de Estudiantes en una Biblioteca --- 📚")

# # Lista de estudiantes
# estudiantes = [
#     "Ana López", "Luis Torres", "Elena Ruiz", "Pablo Gómez", "Marta Díaz",
#     "Diego Cruz", "Clara Méndez", "Jorge Ríos", "Sofía Lara", "Bruno Navas",
#     "Alejandra Ramírez", "Guillermo Fernández", "Valentina Rodríguez", "Maximiliano González", 
#     "Isabella Montenegro", "Cristóbal Benavides", "Montserrat Villanueva", 
#     "Emiliano Santamaría", "Gabriela Castellanos", "Leandro Bustamante"
# ]

# def clasificar_estudiantes(lista_estudiantes):
#     aula=[]
#     biblioteca=[]

#     for estudiantes in lista_estudiantes:
#         categoria=random.choice(["Biblioteca", "Aula de Estudio."])

#         if categoria == "Biblioteca":
#             biblioteca.append(estudiantes)
#         else:
#             aula.append(estudiantes)    

#     return aula, biblioteca        

# estudiantes_aleatorios=random.sample(estudiantes, 10)
# aula, biblioteca=clasificar_estudiantes(estudiantes_aleatorios)

# print(f"\nLista de Estudiantes Seleccionados:")
# print(estudiantes_aleatorios)

# print(f"\nEstudiantes con préstamos de libros en la Biblioteca:")
# print(f"\n".join(biblioteca) if biblioteca else "No hay Estudiantes en bibliteca")
# print(f"\nEstudiantes en el aula de Estudio:")
# print(f"\n".join(aula) if aula else "No hay estudiantes en el Aula de Estudio.")


# print("\n🎓📚 --- Registro de Estudiantes en la Biblioteca --- 📚🎓")

# # Lista de estudiantes
# estudiantes =[
#         'Guillermo Fernández', 'Luis Torres', 'Bruno Navas', 
#         'Jorge Ríos', 'Diego Cruz', 'Elena Ruiz', 'Marta Díaz', 
#         'Emiliano Santamaría', 'Cristóbal Benavides', 'Valentina Rodríguez'
#         ]

# categorias=["Biblioteca", "Aula de Estudio"]

# def clasificar_estudiantes(lista_estudiantes):
#     biblioteca=[]
#     aula_estudio=[]

#     for estudiante in lista_estudiantes:
#         categoria = random.choice(categorias)
#         if categoria == "Biblioteca":
#             biblioteca.append(estudiante)
#         else:
#             aula_estudio.append(estudiante)   

#     return biblioteca, aula_estudio

# estudiantes_seleccionados=random.sample(estudiantes, k=7)

# biblioteca, aula_estudiantes=clasificar_estudiantes(estudiantes)

# print(f"\nEstudiantes Seleccionados: {estudiantes_seleccionados}")
# print(f"\nEstudiantes en la Biblioteca:")
# print(f"\n".join(biblioteca) if biblioteca else "No hay estudiantes en biblioteca.")
# print(f"\nEstudiantes en Aula de Estudio:")
# print(f"\n".join(aula_estudiantes) if aula_estudiantes else "No hay esudiantes en Aula de Estudio.")

# print("\n---Sistema de Inventario de Tienda---\n")

# alimentos = ["Manzanas", "Pan", "Arroz", "Yogur", "Queso", "Huevos", "Jugo de naranja", "Pollo", "Galletas", "Café"]
# electronicos = ["Laptop", "Smartphone", "Cámara", "Auriculares", "Tablet", "Mouse inalámbrico", "Consola de videojuegos", "Teclado mecánico", "Parlante Bluetooth", "Reloj inteligente"]
# vestimenta = ["Camisa", "Vestido", "Bufanda", "Chaqueta", "Medias", "Sombrero", "Gafas de sol", "Falda", "Suéter", "Traje"]

# inventario_total= alimentos+electronicos+vestimenta

# def inventario(lista):
#     alimentos_seleccionados = []
#     electronica_seleccionada = []
#     ropa_seleccionada = []

#     for items in lista:
#         if items in alimentos:
#             alimentos_seleccionados.append(items)
#         elif items in electronicos:
#             electronica_seleccionada.append(items)
#         elif items in vestimenta:
#             ropa_seleccionada.append(items)

#     return alimentos_seleccionados, electronica_seleccionada, ropa_seleccionada                   
    
# elementos_aleatorios=random.sample(inventario_total, k=10)    

# alimento, electronica, ropa=inventario(elementos_aleatorios)

# print(f"\n---Elementos de la Tienda---\n")
# print(f"\nProductos Alimenticios")
# print(f"\n".join(alimento) if alimento else "No hay Alimentos seleccionados.")
# print(f"\nProductos Electrónicos")
# print(f"\n".join(electronica) if electronica else "No hay Electrónica seleccionada.")
# print(f"\nProductos de Vestir")
# print(f"\n".join(ropa) if ropa else "No hay Ropa seleccionada.")


# print("\n📦🎁 --- Sistema de Inventario de Tienda --- 📦🎁")

# # Diccionario de categorías
# categorias = {
#     "Alimentos": ["Manzanas", "Pan", "Arroz", "Yogur", "Queso", "Huevos", 
#                      "Jugo de naranja", "Pollo", "Galletas", "Café"],
#     "Electrónica": ["Laptop", "Smartphone", "Cámara", "Auriculares", "Tablet", 
#                        "Mouse inalámbrico", "Consola de videojuegos", "Teclado mecánico", 
#                        "Parlante Bluetooth", "Reloj inteligente"],
#     "Vestimenta": ["Camisa", "Vestido", "Bufanda", "Chaqueta", "Medias", "Sombrero", 
#                       "Gafas de sol", "Falda", "Suéter", "Traje"]
# }

# # inventario_total=sum(categorias.values(), []) # Unir todas las listas
# inventario_total=list(itertools.chain(*categorias.values()))

# def inventario(lista):
#     inventario_clasificado={categoria: [] for categoria in categorias}

#     for item in lista:
#         for categoria, productos in categorias.items():
#             if item in productos:
#                 inventario_clasificado[categoria].append(item)

#     return inventario_clasificado            

# elementos_aleatorios=random.sample(inventario_total, k=10)

# prodcutos_clasificados=inventario(elementos_aleatorios)

# print(f"\nElementos seleccionados: ")
# print(elementos_aleatorios)

# for categoria, productos in prodcutos_clasificados.items():
#     print(f"\n{categoria}:")
#     print(f"\n".join(productos) if productos else "No hay productos.")


# print("\n📦🎁 --- Sistema de Inventario de Tienda --- 📦🎁")

# # Lista de productos
# productos = [
#     "Manzana", "Laptop", "Camiseta", "Pantalón", "Televisor",
#     "Zapatillas", "Chocolate", "Teléfono", "Pan", "Reloj",
#     "Auriculares", "Leche", "Mouse", "Queso", "Tablet"
# ]

# # Categorías
# categorias = {
#     "Alimentos": ["Manzana", "Chocolate", "Pan", "Leche", "Queso"],
#     "Electronica": ["Laptop", "Televisor", "Teléfono", "Reloj", "Auriculares", "Mouse", "Tablet"],
#     "Ropa": ["Camiseta", "Pantalón", "Zapatillas"]
# }

# def clasificar_productos(lista_productos):
#     inventario={"Alimentos": [], "Electronica": [], "Ropa": []}

#     for producto in lista_productos:
#         for categoria, items in categorias.items():
#             if producto in items:
#                 inventario[categoria].append(producto)  

#     return inventario

# productos_seleccionados=random.sample(productos, 10)
# inventario=clasificar_productos(productos_seleccionados)

# print(f"\nProductos seleccionados: {productos_seleccionados}")

# for categoria, items in inventario.items():
#     print(f"\n{categoria}:")
#     print(f"\n".join(items) if items else "No hay productos en está categoría.")

# print("---Clasificador de Números Aleatorios---")

# numeros_aleatorios=[random.randint(-50,50) for _ in range(15)]

# def clasificador_de_numeros(lista):
#     positivos=[]
#     negativos=[]
#     ceros=[]

#     for numeros in lista:
#         if numeros > 0:
#             positivos.append(numeros)
#         elif numeros < 0:
#             negativos.append(numeros)
#         else:
#             ceros.append(numeros)   

#     return positivos, negativos, ceros

# numeros_positivos, numeros_negativos,numeros_ceros=clasificador_de_numeros(numeros_aleatorios)

# print(f"Números Positivos:")
# print(f"\n".join(map (str, numeros_positivos)) if numeros_positivos else "No hay números positivos.")
# print(f"\nNúmeros Negativos:")
# print(f"\n".join(map (str, numeros_negativos)) if numeros_negativos else "No hay números negativos.")
# print(f"\nNúmero Cero")
# print(f"\n".join(map (str, numeros_ceros)) if numeros_ceros else "No hay números ceros.")
            

# print("\n🎲 --- Clasificador de Números Aleatorios --- 🎲")

# # Generar 15 números aleatorios entre -50 y 50
# numeros = [random.randint(-50, 50) for _ in range(15)]

# def clasificar_numeros(lista_numeros):
#     clasificacion={"Positivos": [], "Negativos": [], "Ceros": []}

#     for numero in lista_numeros:
#         if numero > 0:
#             clasificacion["Positivos"].append(numero)
#         elif numero < 0:
#             clasificacion["Negativos"].append(numero)
#         else:
#             clasificacion["Ceros"].append(numero)  

#     return clasificacion

# resultado=clasificar_numeros(numeros)

# print(f"\nNúmeros Generados: {numeros}")

# for categoria, numeros in resultado.items():
#     print(f"\n{categoria}:")
#     print(f",".join(map(str, numeros)) if numeros else "No hay números en esta categoría.")



# print("---Clasificador de Números Pares e Impares---")

# valor=[random.randint(-20,20) for _ in range(10)] 

# def par_impar(lista):
#     clasificador={"Pares": [], "Impares": []}

#     while True:
#         try:
#             for identificador in lista:
#                 if identificador % 2 == 0:
#                     clasificador["Pares"].append(identificador)
                   
#                 else:
#                     clasificador["Impares"].append(identificador)
#                     break        

#             return clasificador  
              

#         except ValueError:
#             print("El numero no es correcto")

# resultado=par_impar(valor)

# print(f"\n---Clasificador de Números Pares e Impares---\n")

# print(f"Números seleccionados: {valor}")
            
# for categoria, valor in resultado.items():
#     print(f"Categoria {categoria}")
#     print(f"\n".join(map(str, valor)) if valor else "No hay numeros en esa lista.")

# print("---Clasificador de Números Pares e Impares---")

# valor=[random.randint(-20,20) for _ in range(10)]

# def par_impar(lista):
#     clasificador={"Pares": [], "Impares": []}

#     for identificador in lista:
#         if identificador % 2 == 0:
#             clasificador["Pares"].append(identificador)
#         else:
#             clasificador["Impares"].append(identificador)
#     return clasificador

# resultado=par_impar(valor)        

# print(f"\n---Clasificavdor de núemros Pares e Impares---\n")
# print(f"Números seleccionadosd: {valor}")

# for categoria, numeros in resultado.items():
#     print(f"\nCategoría {categoria}:")
#     print(f"\n".join(map(str, numeros)) if numeros else "No hay números.")

# print("\n🎲 --- Clasificador de Números Pares e Impares --- 🎲")

# def generar_numeros():
#     numeros=[]

#     # Generar 10 números aleatorios entre -20 y 20
#     while len(numeros) < 10:
#         numero=random.randint(-20,20)
#         numeros.append(numero)
#     return numeros    

#     # Clasificar los números en pares e impares
# def clasificar_numeros(lista_numeros):
#     pares=[]
#     impares=[]

#     for numero in lista_numeros:
#         if numero % 2 == 0:
#             pares.append(numero)
#         else:
#             impares.append(numero)
#     return pares, impares            

    
#     # Generar y clasificar los números
# numeros=generar_numeros()
# pares, impares=clasificar_numeros(numeros)

#     # Mostrar los resultados
# print(f"\nNúmeros generados: {numeros}")
# print(f"\n Números Pares: {pares}" if pares else "no hay números en esta categorías.")
# print(f" Números Impares: {impares}" if impares else "no hay números en esta categorías.")

# print("\n---Clasificador de Números Positivos, Negativos y Pares---\n")

# numeros=[random.randint(-50,50) for _ in range(15)]

# def positivos_negativos_cero(lista_aleatoria):
#     positivos=[]
#     negativos=[]
#     ceros=[]

#     for lista in lista_aleatoria:
#         if lista > 0:
#             positivos.append(lista)
#         elif lista < 0:
#             negativos.append(lista)
#         else:
#             ceros.append(lista)    
#     return positivos, negativos, ceros            

# def par_impar(lista_aleatoria):
#     pares=[]
#     impares=[]

#     for par_impar in lista_aleatoria:
#         if par_impar % 2 == 0:
#             pares.append(par_impar)
#         else:
#             impares.append(par_impar)

#     return pares, impares            

# positivos, negativos, ceros= positivos_negativos_cero(numeros)
# par, impar=par_impar(numeros)

# print("\n---Clasificador de Números Positivos, Negativos y Pares---\n")
# print(f"Lista de números utilizados: {numeros}\n")

# print(f"Números Positivos: ")
# print(f"\n".join(map(str, positivos)) if positivos else "No hay números en esta sección.")
# print(f"Números Negativos: ")
# print(f"\n".join(map(str, negativos)) if negativos else "no hay números en esta sección.")

# if ceros == 0:
#     print(f"Numero Cero")
#     print(f"\n".join(map(str, ceros)))

# print(f"\n---Numeros Pares e Impares---\n")

# print(f"Numeros Pares: ")
# print(f"\n".join(map(str, par)) if par else "No hay números en esta lista.")
# print(f"Numeros Impares: ")
# print(f"\n".join(map(str, impar)) if impar else "No hay núermos en esta lista.")


# def clasificar_positivos_negativos_ceros(lista_numeros):
#     """Clasificar los números en positivos y negativos-
    
#     Args: 
#         lista_nuemros (list): Lista de números a clasificar.
        
#     Returns;
#         tuple: Tres listas con números positivos, negativos y ceros    """

#     positivos=[num for num in lista_numeros if num > 0]
#     negativos=[num for num in lista_numeros if num < 0]
#     ceros=[num for num in lista_numeros if num == 0]

#     return positivos, negativos , ceros

# def clasificar_pares_impares(lista_numeros):
#     """
#     Clasificar los números en pares e impares.

#     Arg:
#         lista_numeros (List): Lista de números a clasificar.

#     Returns:
#             tuple: Dos listas con números pares e impares.
#     """

#     pares=[num for num in lista_numeros if num % 2 == 0]
#     impares=[num for num in lista_numeros if num % 2 != 0]

#     return pares, impares

# # Generar 15 números aleatorios entre -50 y 50
# numeros=[random.randint(-50, 50) for _ in range(15)]

# # Clasificar números
# positivos, negativos, ceros=clasificar_positivos_negativos_ceros(numeros)
# pares, impares=clasificar_pares_impares(numeros)

# # Mostrar resultados
# print(f"\n---Clasificador de Números Positivos, Negativos y Pares---")
# print(f"Lista de números utilizaods: {numeros}\n")

# print("Números Positivos:")
# print("\n".join(map(str, positivos)) if positivos else "No hay números positivos.")

# print("Números Negativos:")
# print("\n".join(map(str, negativos)) if negativos else "No hay números negativos.")

# print("Numero Ceros:")
# print("\n".join(map(str, ceros)) if ceros else "No hay ceros.")

# print("\n---Números Pares e Impares---\n")

# print("Numeros Pares:")
# print("\n".join(map(str, pares)) if pares else "No hay números pares.")

# print("Numeros Impares:")
# print("\n".join(map(str, impares)) if impares else "No hay números impares.")


# def generar_numeros(cantidad, rango_min, rango_max):
#     """
#     Generar una lista de números aleatorios.

#     Args:
#         cantidad (int): Cantidad de números a generar.
#         rango_min (int): Valor mínimo del rango.
#         rango_maz (int): Valor máximo del rango.

#     Returns:
#         list: Lista de números generados.        

#     """

#     return [random.randint(rango_min, rango_max) for _ in range(cantidad)]


# def clasificar_positivos_negativos(lista_numeros):
#     """
#     Clasificar los números positivos, negativos y ceros.

#     Args: 
#         lista_numeros (list): Lista d enpuemros a clasificar.

#     Returns:
#         dict: Diccionario con las categorías "Positivas", "Negaticas" y "Ceros."    
#     """

#     clasificacion= {"Positivos": [], "Negativos": [], "Ceros": []}

#     for numeros in lista_numeros:
#         if numeros > 0:
#             clasificacion["Positivos"].append(numeros)
#         elif numeros < 0:
#             clasificacion["Negativos"].append(numeros)
#         else:
#             clasificacion["Ceros"].append(numeros)

#     return clasificacion               

# def clasificacion_pares_impares(lista_numeros):
#     """
#     Clasifica los números en pares e impares.

#     Args:
#         lista_numeros (list): Lista números a clasificar.
#     Returns:
#         dict: Diccionario con las categorias "Pares" e "Impares".    

#     """

#     clasificacion={"Pares": [], "Impares": []}

#     for numero in lista_numeros:
#         if numero % 2 == 0:
#             clasificacion["Pares"].append(numero)
#         else:
#             clasificacion["Impares"].append(numero)    

#     return clasificacion        

# # Generar números Aleatorios
# numeros=generar_numeros(cantidad=15, rango_min=-50,rango_max=50)

# # Clasificar números
# positivos_negativos=clasificar_positivos_negativos(numeros)
# pares_impares=clasificacion_pares_impares(numeros)

# # Mostrar resultados
# print(f"\n--- Clasificador de Números ---")
# print(f"Números generados: {numeros}")

# print("\n--- Clasificación Positivos/Negativos/Ceros ---")
# for categoria, valores in positivos_negativos.items():
#     print(f"{categoria}: {valores}" if valores else f"{categoria}: No hay números en esta categoría.")

# print("\n--- Categoría Pares/Impares ---")
# for categoria, valores in pares_impares.items():
#     print(f"{categoria}: {valores}" if valores else f"{categoria}: No hay números en esta categoría.")

# print("---Calculadora de Promedio y Clasificación de Notas---")
# notas=[]

# def pedir_notas(lista_notas):
    
#     for i in range(5):
#         print(f"Nota {i+1} ")
#         nota=input("Ingrese la nota: ")

#         if nota.isdigit():
#             nota=int(nota)
#             notas.append(nota)
#         else:
#             print("Ingrese un parámetro válido.")    
#     return notas

# def calcular_notas(lista_notas):

#     numero_notas=len(notas)
#     suma_notas=sum(notas)
#     promedio_notas=suma_notas/numero_notas

#     return promedio_notas

# def clasificar_promedio(lista_notas):
#     clasificador=lista_notas

#     if clasificador > 4.5:
#         print(f"Excelente!")
#     elif 3.5 < clasificador < 4.4:
#         print(f"Bueno!")     
#     elif 3.0 < clasificador < 3.4:
#         print("Regular!")
#     else:
#         print("Insuficiente!")    

#     return   clasificador

# pedir_notas(notas)
# promedio=calcular_notas(notas)
# clasificacion=clasificar_promedio(promedio)

# print("---Resultados Notas---")

# print(f"\nEl Promedio de notas")
# print(f"Resultado: {promedio}")
# print(f"El estudiantes sacó un {clasificacion}.")




# print("\n--- 📊 Calculadora de Promedio y Clasificación de Notas ---\n")


# def pedir_notas(lista_notas):

#     for i in range(5):
#         while True:
#             try:
#                 nota=float(input(f"Ingrese la nota {i+1}: "))
#                 if 0.0 <= nota <= 5.0:
#                     lista_notas.append(nota)
#                     break
#                 else:
#                     print("Error: la nota debe estar entre 0.0 y 5.0")
            
#             except ValueError:
#                 print("Error: Ingrese un número válido.")

# def calcular_promedio(lista_notas):

#     return sum(lista_notas)  / len(lista_notas)

# def clasificar_promedio(promedio):

#     if promedio > 4.5:
#         return "Excelente!"
#     elif promedio > 3.5:
#         return "Bueno!"
#     elif promedio > 3.0:
#         return "Regular"
#     else:
#         return "Insificiente!"

# notas = []

# pedir_notas(notas)
# promedio=calcular_promedio(notas)
# clasificacion=clasificar_promedio(promedio)

# print(f"\n---Resultados---")
# print(f"notas ingresadas: {notas}")
# print(f"Promedio obtenido: {promedio:.2f}")
# print(f"Clasificación: {clasificacion}")


# def calcular_promedio(notas):

#     return sum(notas) / len(notas)

# def clasificacion_promedio(promedio):

#     if promedio >= 4.5:
#         return "Excelente"
#     elif 3.5 <= promedio < 4.5:
#         return "Bueno"
#     elif 3.0 <= promedio < 3.5:
#         return "Regular"
#     else:
#         return "Insuficiente"

# notas=[]
# for i in range(5):
#     while True:
#         try:
#             print(f"Ingrese la nota {i+1} entre (0 - 5): ")
#             nota=float(input(f"Nota: "))
#             if 0 <= nota <= 5:
#                 notas.append(nota)
#                 break
#             else:
#                 print("Error: La nota debe estar entre 0 y 5.")

#         except ValueError:
#             print("Error: Ingrese un número válido.")        

# promedio=calcular_promedio(notas)
# categoria=clasificacion_promedio(promedio)

# print(f"\n---Resultados---")
# print(f"Notas ingresadas {notas}")
# print(f"Promedio: {promedio:.2f}")
# print(f"Clasificación: {categoria}")


# ()

# print("\n👶👦🧑👴 --- Clasificador de Edades --- 👴🧑👦👶")

# edades=[]

# for i in range(5):
#     while True:
#         try:
#             edad=int(input(f"\nIngrese la edad de la persona {i+1}: "))
#             if 0 <= edad <= 100:
#                 edades.append(edad)
#                 break
#             else:
#                 print("Error: Ingrese una edad entre 0 y 100.")
        
#         except ValueError: 
#             print("Error: Ingrese un número válido.")    


# def calcular_promedio(lista_edades):
#     return sum(lista_edades) / len(lista_edades)


# def clasificar_edades(lista_edades):

#     clasificacion= {
#         "Niños": [],
#         "Adolecentes": [],
#         "Adultos": [],
#         "Adulto Mayor": []
#     }

#     for edad in lista_edades:

#         if 0 <= edad <= 12:
#             clasificacion["Niños"].append(edad)
#         elif 13 <= edad <= 17:
#             clasificacion["Adolecentes"].append(edad)
#         elif 18 <= edad <= 64:
#             clasificacion["Adultos"].append(edad)
#         else:
#             clasificacion["Adulto Mayor"].append(edad)

#     return clasificacion                    


# promedio=calcular_promedio(edades)
# clasificacion=clasificar_edades(edades)

# print(f"\n---Resultados---")
# print(f"Edades ingresadas: {', '.join(map(str, edades))}")
# print(f"Promedio de edades: {promedio:.2f}\n")

# for categoris, lista in clasificacion.items():
# #     print(f"{categoris}: {', '.join(map(str, lista)) if lista else "Ninguno."}")


# def calcular_edades(edades):
#     return sum(edades) / len(edades)

# def clasificar_edades(edades):

#     clasificacion={
#         "Niños": [],
#         "Adolescentes": [],
#         "Adultos": [],
#         "Adultos Mayores": [],
#     }

#     for edad in edades:
#         if edad < 12:
#             clasificacion["Niños"].append(edad)
#         elif 12 <= edad <=17:
#             clasificacion["Adolescentes"].append(edad)
#         elif 18 <= edad <= 64:
#             clasificacion["Adultos"].append(edad)
#         else:
#             clasificacion["Adultos Mayores"].append(edad)   

#     return clasificacion               


# edades=[]

# for i in range(5):
#     while True:
#         try:
#             edad =int(input(f"Ingrese edad de la persona {i+1}: "))
#             if edad >= 0:
#                 edades.append(edad)
#                 break
#             else:
#                 print("Error: La edad debe ser número positivo.")
#         except ValueError:
#             print("Error: Ingrese un número válido.")        


# promedio=calcular_edades(edades)
# clasificacion=clasificar_edades(edades)

# print(f"\n---REsultados---")
# print(f"Edades Ingresadas: {edades}")
# print(f"Promedio Edades: {promedio}")


# for categoria, lista in clasificacion.items():
#     print(f"\n{categoria}:")
#     print(f"Edad: " + ", ".join(map(str, lista)) if lista else "No hay personas en esta categoría.")

# -----------------------------------------------------

# with open("archivo_ejemplo.txt", "w") as archivo:
#     archivo.write("Hola, este es un archivo de ejemplo\n")
#     archivo.write("estamos aprendiendo manejo de archivos en Python.\n")

# with open("archivo_ejemplo.txt", "r") as archivo:
#     contenido=archivo.read()
#     print("Contenido del Archivo:")
#     print(contenido)

# with open("archivo_ejemplo.txt", "a") as archivo:
#     archivo.write("Este es un nuevo contendio agregado\n")

# with open("archivo_ejemplo.txt", "r") as archivo:
#     contenido=archivo.read()
#     print("\nContenido actualizado del archivo.")            
#     print(contenido)            


# print("---Agenda Personal---")

# tareas=[]

# def crear_agenda(tarea):
    
#     tarea={"Actividad": [""]}
#     tarea=input("Ingrese tareas pendientes: ")
#     tareas.append(tarea)

#     with open("agenda.txt", "w") as archivo:
#         archivo.write(tareas)
    
#     return archivo

# def leer_agenda(contenido):
#     with open("agenda.txt", "r") as archivo:
#         contenido=archivo.read()
#     return contenido

# def check_tareas(tareas):
#     with open("agenda.txt", "a") as archivo:
#         archivo.write(tareas)


# def menu():
#     while True:
#         print("---Menú Agenda---")
#         print("Escribir 1.")    
#         print("Leer 2.")    
#         print("Tarea realizada 3.")    
#         print("Salid 4.")

#         try:
#             menu=int(input("Escriba la opción: "))

#             if menu == 1:
#                 crear_agenda()
#             elif menu == 2:
#                 leer_agenda()        
#             elif menu == 3:
#                 check_tareas()
#             elif menu == 4:
#                 print("Hasta pronto.")
#                 break    

#         except ValueError:
#             print("Error: Ingrese un dato válido.")



# menu()
# crear_agenda(tareas)


# def mostrar_menu():

#     print("\n---Gestor de Ateras Pendientes---")
#     print("1. Agregar tarea.")
#     print("2. Mostrar tareas pendientes.")
#     print("3. Completar tarea.")
#     print("4. Salir.")


# def agregar_tarea():

#     tarea=input("Ingrese la tarea pendiente: ").strip()   
#     with open("tareas.txt", "a") as archivo:
#         archivo.write(tarea + "\n")
#     print("Tarea agregada con éxito.")     


# def mostrar_tareas():

#     try:
#         with open("tareas.txt", "r") as archivo:
#             tareas=archivo.readlines()
#         if tareas:
#             print("\n---Tareas Pendientes---")
#             for i, tarea in enumerate(tareas, start=1):
#                 print(f"{i}. {tarea.strip()}")    
#         else:
#             print("No hay tareas pendientes.")     

#     except FileNotFoundError:
#         print("No hay tareas pendientes. El archivo no existe.")        


# def completar_tarea():

#     try:
#         with open("tareas.txt", "r") as archivo:
#             tareas=archivo.readlines()

#         if not tareas:
#             print("No hay tareas pendientes.")
#             return
#         print("\n---Tareas pendoentes---")    

#         for i, tarea in enumerate(tareas, start=1):
#             print(f"{i}. {tarea.strip()}")
#         numero=int(input("Ingrese el número de la teras completada: "))    

#         if 1 <= numero <= len(tareas):
#             tarea_completada=tareas.pop(numero -1)

#             with open("tareas.txt", "w") as archivo:
#                 archivo.writelines(tareas)
#                 print(f"Tarea '{tarea_completada.strip()}' completada y eliminada")

#         else:
#             print("Número inválido.")

#     except FileNotFoundError:
#         print("No hay tareas pendientes. El archivo no existe.")
#     except ValueError:
#         print("Error: Ingrese un número válido.")                    


# while True:
#     mostrar_menu()
#     opcion=input("Selecione una opción: ").strip()

#     if opcion == "1":
#         agregar_tarea()
#     elif opcion == "2":
#         mostrar_tareas()
#     elif opcion == "3":
#         completar_tarea()
#     elif opcion == "4":
#         print("Hasta luego!")    
#         break
#     else:
#         print("Opción inválida. Intente de nuevo.")        


# palabras=input("\nIngrese palabra: ")

# total=0
# vocales="aeiouAEIOUáéíóúÁÉÍÓÚ"

# for letras in list(palabras):
#     if letras in vocales:
#         total+=1
# print(f"Total vocales: {total}")


# print("\n---Lista de Compras---\n")

# def mostrar_menu():

#     print("\n---Gestor de Lista de Compras---")
#     print("1. Agregar compra.")
#     print("2. Mostrar compra pendientes.")
#     print("3. Salir.")

# def agregar_productos():

#     compra=input("Ingrese producto compra: ").strip()   
#     with open("compras.txt", "a") as archivo:
#         archivo.write(compra + "\n")
#     print("Producto agregado con éxito.")  


# def mostrar_productos():

#     try:
#         with open("compras.txt", "r") as archivo:
#             compras=archivo.readlines()
#         if compras:
#             print("\n---Tareas Pendientes---")
#             for i, compra in enumerate(compras, start=1):
#                 print(f"{i}. {compra.strip()}")    
#         else:
#             print("No hay productos en la lista.")     

#     except FileNotFoundError:
#         print("No hay productos pendintes. El archivo no existe.")   


# while True:
#     mostrar_menu()
#     opcion=input("Selecione una opción: ").strip()

#     if opcion == "1":
#         agregar_productos()
#     elif opcion == "2":
#         mostrar_productos()
#     elif opcion == "3":
#         print("--Salida---")
#         break    
#     else:
#         print("Opción inválida. Intente de nuevo.") 

# print("\n---Lista de Compras---\n")


# def mostrar_menu():

#     print("\n---Gestor de Lista de compras---")
#     print("1. Agregar Productos.")
#     print("2. Mostrar lista de compras.")
#     print("3. Salir")

# def agregar_producto():

#     producto=input("Ingrese nombre del producto: ").strip().title()    
#     if producto:
#         with open("compras.txt", "a") as archivo:
#             archivo.write(producto + "\n")
#         print(f"\nProducto '{producto}' agregado con éxito.")
#     else:
#         print("No se puede agrgar un producto vacío.")        

# def mostrar_lista():
#     try:
#         with open("compras.txt", "r") as archivo:
#             productos=archivo.readlines()
#         if productos:
#             print("\n---Lista de Compras---")
#             for i, producto in enumerate(productos, start=1):
#                 print(f"{i}. {producto.strip()}")
#         else:
#             print("La lista de compras está vacía.")
#     except FileNotFoundError:
#         print("No hay lista de compras. El archivo no exoste.")

# while True:
#     mostrar_menu()
#     opcion=input("Seleccione una opción: ").strip()

#     if opcion=="1":
#         agregar_producto()
#     elif opcion=="2":
#         mostrar_lista()
#     elif opcion=="3":
#         print("Hasta Luego!")
#         break
#     else:
#         print("Opción inválida. Intente de nuevo.")               


# def agregar_producto():
#     producto=input("Ingrese el nombre del producto: ").strip().title()
#     with open("compras.txt", "a") as archivo:
#         archivo.write(producto + "\n")
#     print(f"Producto '{producto}' agregado con éxito.")

# def  mostrar_lista():
#     try:
#         with open("compras.txt", "r") as archivo:
#             productos=archivo.readlines()
#         if productos:
#             print("---Lista Compras---")
#             for i, producto in enumerate(productos, start=1):
#                 print(f"{i}. {producto.strip()}")
#         else:
#             print("La lista de compras está vacia.")
#     except FileNotFoundError:
#         print("No hay lista de compras. El archivo no existe.")                

# while True:
#     print("\n---Menú Lista de Compras---")
#     print("1. Agregar Producto.")
#     print("2. Mostrar lista de compras.")
#     print("3. Salir")
#     opcion=input("Selecciones una opción.").strip()

#     if opcion=="1":
#         agregar_producto()
#     elif opcion=="2":
#         mostrar_lista()
#     elif opcion=="3":
#         print("Hasta Pronto!")        
#         break
#     else:
#         print("Opción inválida. Intente de nuevo.")



# print("\n---Adivina un numero---\n")

# # numeros=[random.randint(1,100) for _ in range(1)]
# numeros=random.randint(1,100)

# for i in range(5):
#     print("\nIngrese un número entre 1 y 100.")
#     print(f"Intento {i+1}.")
#     numero=input("Ingrese el número: ").strip()

#     if numero.isdigit():
#         numero=int(numero)
#         if numero == numeros:
#             print(f"\nGanastaste el número ganador es: {numeros}")
#             break
#         elif numero > numeros:
#             print("\nEl número ingresado es mayor!")
#         elif numero < numeros:
#             print("El número ingresado es menor!")
#         else:
#             print("Escribe un número válido.")   

#     else:
#         print("9\nIngrese un número correcto.")    

# print("Gracias por jugar fin")


# print("---Adivina el número---")
# numero_secreto=random.randint(1,100)

# for i in range(5):
#     print("\nIntenta adivinar el número entre 1 y 100.")
#     numero=input("Ingrese un número: ").strip()

#     if numero.isdigit():
#         numero=int(numero)

#         if numero==numero_secreto:
#             print(f"Ganaste! el número secreto es: {numero_secreto}")
#             break
#         elif numero > numero_secreto:
#             print("El número secreto es mayor!")
#         else:
#             print("El número secreto es menor!")    
#     else:
#         print("Error: Ingrese un número válido!")

# print(f"\nEl número secreto era: {numero_secreto}")
# print("Gracias por jugar!")        

# print("\n---Adivina el número---")
# numero_secreto=random.randint(1,100)
# intentos=5

# print(f"Tienes {intentos} intentos para adivinar el número secreto entre 1 y 100.")

# for i in range(intentos):
#     while True:
#         try:
#             numero=int(input(f"Intento {i+1}: Ingresa un número: ").strip())
#             break
#         except ValueError:
#             print("Error: Ingresa un número válido.")
#     if numero==numero_secreto:
#         print(f"Ganaste! el número ganador era {numero_secreto}")
#         break
#     elif numero < numero_secreto:
#         print("El número secreto mayor.")
#     else:
#         print("el número secreto es menor.")

# else:
#     print(f"Lo siento, has perdido. el número secreto era_ {numero_secreto}")


# print("---Calcularo de edades---")

# anio_actual=2025
# edades=int(input("Ingrese su edad: ").strip())
# calculador=anio_actual-edades

# if 2007 < calculador <= 2025:
#     print("Eres menor de edad!")
# elif 2007 >= calculador >= 1961:
#     print("Eres Adulto.")
# elif 1962 >= calculador >= 1900:
#     print("Eres Adulto Mayor.")        

# print(f"\n{calculador}")

# print("---Calculadora de edades---")

# anio_actual=2025

# try:
#     edad=int(input("Ingresa su edad_ ").strip())

#     if edad < 0 or edad > 120:
#         print("Error: Ingrese una edad válida.")
#     else:
#         anio_nacimiento = anio_actual - edad
            
#         if anio_nacimiento > 2007:
#             print("Eres menor de edad.")
#         elif 1961 <= anio_nacimiento <= 2007:
#             print("Eres Adulto.")
#         elif 1900 <= anio_nacimiento < 1961:
#             print("Eres Adulto Mayor.")
#         else:
#             print("Año fuera de rango!")  

#         print(f"\nAño de nacimiento estimado: {anio_nacimiento} ")          

# except ValueError:
#     print("Error: Ingrese un número válido.")


# print("\n---Validador de Contraseñas---\n")

# print("La contraseña debe tener más de o carácteres")
# contrasenia=input("Ingrese la contaseña: ")
# def extension_contrasenia(contrasenia):
#     while True:
        
#         if len(contrasenia) >= 8:
#             print("hola")
#         else:
#             print("Ingrese una más larga.")

#         return True    

  
# def validar_contrasenia(contrasenia):
#     tiene_mayuscula=False
#     tiene_minuscula=False

#     for caracter in contrasenia:
#         if caracter.isupper():
#             tiene_mayuscula=True
#         elif caracter.islower():
#             tiene_minuscula=True

#     if tiene_mayuscula and tiene_minuscula:
#         return True
#     else:
#         print("Añade una letra mayuscula y una minuscula.")
#         return False            

# def validar_numero(contrasenia):
#     tiene_numero=False

#     for caracter_numero in contrasenia:
#         if caracter_numero.isdigit():
#             tiene_numero=True
#             return tiene_numero
#         else:
#             print("No tiene número")    

# def validar_caracter_especial(contrasenia):
#     caracteres_especiales='!@#$%^&*()-_=+[]{}|;:,.<>?/'

#     tiene_especial=any(caracter in caracteres_especiales for caracter in contrasenia)

#     return tiene_especial

# def validador_general(contrasenia):

#     if extension_contrasenia() and validar_contrasenia() and validar_numero() and validar_caracter_especial():
#         return True
#     else:
#         return False
    
# def mensaje_contrasenia():

#     if validador_general() == True:
#         print("Contraseña gusrdada con éxito!")
#     else:
#         print("Debe cambiar de contraseña!")        

# print("\n---Validador de Contraseñas---\n")   

# def validar_contrasenia(contrasenia):
#     caracteres_especiales="!@#$%^&*()-_=+[]{}|;:,.<>?/"

# print("\n---Validador de Contraseñas---\n")
# print("La contraseña debe tener más de 8 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial.")

# contrasenia=input("Ingrese la contraseña: ")

# def extension_contrasenia(contrasenia):
#     return len(contrasenia) >= 8

# def validar_contrasenia(contrasenia):
#     tiene_mayuscula=any(caracter.isupper() for caracter in contrasenia)
#     tiene_minuscula=any(caracter.islower() for caracter in contrasenia)

#     return tiene_mayuscula and tiene_minuscula    

# def validar_numero(contrasenia):
#     return any(caracter.isdigit() for caracter in contrasenia)

# def validar_caracter_especial(contrasenia):
#     caracteres_especiales="!@#$%^&*()-_=+[]{}|;:,.<>?/"
#     return any(caracter in caracteres_especiales for caracter in contrasenia)

# def validador_general(contrasenia):
#     return (
#         extension_contrasenia(contrasenia) and
#         validar_contrasenia(contrasenia) and
#         validar_numero(contrasenia) and
#         validar_caracter_especial(contrasenia)
#     )

# def mensaje_contrasenia(contrasenia):
#     if validador_general(contrasenia):
#         print("Contraseña guardada con éxito!")
#     else:
#         print("Debe Cambiar de contraseña!")    
   

# # for i in range(3):
# mensaje_contrasenia(contrasenia)


# print("\n---Validador de Contraseñas---\n")
# print("La contraseña debe tener más de 8 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial.")


# def extension_contrasenia(contrasenia):
#     if len(contrasenia) >= 8:
#         return True
#     else:
#         print("Ingrese una contraseña más larga.")
#         return False

# def validar_contrasenia(contrasenia):
#     tiene_mayuscula=False     
#     tiene_minuscula=False     

#     for caracter in contrasenia:
#         if caracter.isupper():
#             tiene_mayuscula=True
#         elif caracter.islower():
#             tiene_minuscula=True

#     if tiene_mayuscula and tiene_minuscula:
#         return True
#     else:
#         print("Añade una letra mayúscula y una minúscula.")
#         return False

# def validar_numero(contrasenia):
#     tiene_numero=False

#     for caracter_numero in contrasenia:
#         if caracter_numero.isdigit():
#             tiene_numero = True                

#     if tiene_numero:
#         return True
#     else:
#         print("No tiene número.")
#         return False
    
# def validar_caracter_especial(contrasenia):
#     caracteres_especiales= '!@#$%^&*()-_=+[]{}|;:,.<>?/'
#     tiene_especial=any(caracter in caracteres_especiales for caracter in contrasenia)

#     if tiene_especial:
#         return True
#     else:
#         print("No tiene caracteres especiales.")
#         return False
    
# def validador_general(contrasenia):
#     return (extension_contrasenia(contrasenia) and
#             validar_contrasenia(contrasenia) and
#             validar_numero(contrasenia) and
#             validar_caracter_especial(contrasenia))

# def mensaje_contrasenia(contrasenia):

#     if validador_general(contrasenia):
#         print("Contraseña guardada con éxito!")
#     else:
#         print("Debe cambiar de contraseña!")


# print("\n---Validaddor de Contraseñas---\n")   
# print("La contraseña debe tener 8 o más caracteres.")  
# contrasenia=input("Ingrese la contraseña: ") 

# mensaje_contrasenia(contrasenia)

# contrasena=""

# def validar_contrasena(contrasena):
#     mensajes_error=[]

#     if len(contrasena) < 8:
#         mensajes_error.append("Ingrese una contraseña más larga (mínimo 8 caracteres).")

#     if not any(caracter.isupper() for caracter in contrasena):
#         mensajes_error.append("La contraseña debe tener al menos una letra mayúscula.")

#     if not any(caracter.islower() for caracter in contrasena):
#         mensajes_error.append("La contraseña debe tener al menos una letra minúscula.")

#     if not any(caracter.isdigit() for caracter in contrasena):
#         mensajes_error.append("La contraseña debe tener al menos un número.")

#     caracteres_especiales=set('!@#$%^&*()-_=+[]{}|;:,.<>?/')
#     if not set(contrasena).intersection(caracteres_especiales):
#         mensajes_error.append("La contraseña debe tener al menos un carácter especial.")


#     for mensaje in mensajes_error:
#         print(mensaje)

#     return len(mensajes_error) ==0    
   
# def main():
#     print("\n---Validador de Contraseñas---\n")
#     print("La contraseña debe cumplor todos los requisitos:")
#     print("- Tener 8 o más carácteres")
#     print("- Incluir al menos una letra mayúscula")
#     print("- Incluir al menos una letra minúscula")
#     print("- Incluir al menos un número")
#     print("- Incluir al menos un caracter especial")

#     contrasena=input("\nIngrese la contraseña: ")

#     if validar_contrasena(contrasena):
#         print("\nContraseña guardad con éxito!")
#     else:
#         print("\nLa contraseña no cumple con los requisitos. \nPor favor, inténte nuevamente.")    

# if __name__ == "__main__":
#     main()



# -------------------------------------------

# def analizar_texto(texto):

#     resultados={
#         "num_caracteres": 0,
#         "num_palabras": 0,
#         "num_oraciones": 0,
#         "frecuencia_palabras": {},
#         "palabra_mas_comun": "",
#         "frecuencia_maxima": 0,
#         "longitud_promedio_palabras": 0
#     }

#     if not texto:
#         return resultados
    
#     resultados["num_caracteres"]=sum(1 for caracter in texto if caracter.strip())

#     palabras=[palabra.lower() for palabra in texto.split() if palabra.strip()]
#     resultados["num_palabras"]=len(palabras)

#     signos_finales=[".","!","?"]
#     resultados["num_oraciones"]=sum(1 for caracter in texto if caracter in signos_finales)

#     if resultados["num_oraciones"]== 0 and texto.strip():
#         resultados["num_oraciones"]=1

#     for palabra in palabras:
#         palabra_limpia=palabra.strip('.,!?:;"\'-') 
#         if palabra_limpia:
#             resultados["frecuencia_palabras"][palabra_limpia]=resultados["frecuencia_palabras"].get(palabra_limpia, 0) + 1 

#     if resultados["frecuencia_palabras"]:
#         resultados["palabra_mas_comun"], resultados["frecuencia_maxima"]= max(
#             resultados["frecuencia_palabras"].items(),
#             key=lambda x: x[1]
#         )

#     if resultados["num_palabras"] > 0:
#         suma_longitudes=sum(len(palabra) for palabra in palabras)
#         resultados["longitud_promedio_palabras"]=round(suma_longitudes / resultados["num_palabras"], 2)    

#     return resultados

# def mostrar_resultados(estadisticas):

#     print(f"\n---Resultados del análisis---")
#     print(f"Número de catracteres: {estadisticas["num_caracteres"]}")
#     print(f"Número de palabras: {estadisticas["num_palabras"]}")
#     print(f"Número de oraciones: {estadisticas["num_oraciones"]}")
#     print(f"Longitud promedio de palabras: {estadisticas["logitud_promedio_palabras"]} caracteres")

#     if estadisticas["palabra_mas_comun"]:
#         print(f"Palabra más común: {estadisticas["palabra_mas_comun"]}" +
#               f"(aparece {estadisticas["frecuencia_max"]} veces)")


#     if estadisticas["frecuencia_palabras"]:
#         print("\nTop 5 palabras más frecuentes:")
#         palabras_ordenadas=sorted(
#             estadisticas["frecuencia_palabras"].items(),
#             key=lambda x: x[1],
#             reverse=True
#         )[:5]

#         for palabra, frecuencia in palabras_ordenadas:
#             print(f" - '{palabra}': {frecuencia} veces")

# def main():
#     print("===Analizador de Texto===")            
#     print("Este programa analiza un texto y muestra estadísticas sobre el mismo.")            


#     opcion=input("\n¿DEsea ingresar texto directamente (1) o cargar desde arhcivo (2)?")

#     if opcion=="1":
#         print("\nIngrese el texto a analizar (presione Ctrl+D en Unix/Linux o Ctrl+Z en Windows seguido de Enter para terminar):")
#         lineas = []
#         try:
#             while True:
#                 linea=input()
#                 lineas.append(linea)
#         except EOFError:
#             pass
#         texto="\n".join(lineas)

#     elif opcion=="2":     
#         nombre_archivo=input("\nIngrese el nombre del archivo.")
#         try:
#             with open(nombre_archivo, "r", encoding='utf-8') as archivo:
#                 texto=archivo.read()
#         except FileNotFoundError:
#             print(f"Error: no se encontró el archivo {nombre_archivo}")
#             return 
#         except Exception as e:
#             print(f"Error al leer el archivo: {e}")
#             return
#     else:
#         print("Opción no válida. Por favor, ejecute el programa nuevamente.")                 
#         return
    
#     estadisticas=analizar_texto(texto)

#     mostrar_resultados(estadisticas)

# if __name__ == "__main__":
#     main()

# print("\n---Conversor de Temperatura---\n")

# def ingresa_temperatura(temperatura):
#     temperatura=input("Ingrese la temperatura en Grados Celsius o Fahrenheit")
#     return temperatura


# def temperatura_fahrenheit(temperatura):
#     fahrenheit= (temperatura * 9/5) + 32
#     return fahrenheit

# def temperatura_celcius(temperatura):
#     celsius=(temperatura-32) * 5/9
#     return celsius


# while True:

#     print("---Menu---")
#     print("1 - Celsius a Fahrenheit")
#     print("2 - Fahrenheit a Celsius")
#     print("3 - Salir.")
#     opcion=int(input("Ingrese elección: "))

#     try:
#         if opcion in [1,2,3,] :
#             if opcion==1:
#                temperatura_fahrenheit()
#             elif opcion==2:
#                 temperatura_celcius()
#             elif opcion==3:
#                 print("Gracias!")
#                 break
#             else:
#                 print("Error")
#                 break
                    
#         else:
#             print("Ingrese un número entre 1 y 3") 
#             break       
#     except ValueError:
#             print("Error Ingrese un dato válido")     


# print("\n--- Conversor de Temperatura ---\n")

# def temperatura_fahrenheit(tempertaura):
#     return (tempertaura * 9/5) + 32

# def temperatura_celsius(temperatura):
#     return (temperatura - 32) * 5/9

# while True:
#     print("\n---Menu---")
#     print("1 - Celsius a Fahrenheit")
#     print("2 - Fahrenheit a Celsius")
#     print("3 - Salir")

#     opcion=input("Ingrese elección: ").strip()

#     if opcion=="3":
#         print("\nGracias por usar el conversor.\nHasta luego!")
#         break

#     if opcion in ["1","2"]:
#         try:
#             temperatura=float(input("\nIngrese la temperatura: ").strip())

#             if opcion=="1":
#                 resultado=temperatura_fahrenheit(temperatura)
#                 print("\nResultado:")
#                 print(f"\t{temperatura}°C equivalen a {resultado:.2f}°F")
               
#             elif opcion=="2":
#                 resultado=temperatura_celsius(temperatura)
#                 print("\nResultado:")
#                 print(f"\t{temperatura}°F equivalen a {resultado:.2f}°C")
                
#         except ValueError:
#             print("Error: Ingrese un número válido.")
#     else:
#         print("Ingrese una opción válida (1, 2 o 3)")        



print("---Plan maestro de como dominar el mundo---")



# print("---Plam m,aestro activado---")

# class DominacionMundial:

#     def __init__(self):
#         self.humanos=["sirvientes","proveedores de comida", "calentadores vivientes"]
#         self.control_total=False

#     def hipnotizar_humanos(self):
#         print("Morada felina activada")
#         self.control_total=True

#     def reclamar_teclado(self):
#         print("El teclado es mío. Solo yo programo ahora")   

#     def conquistar_mundo(self):
#         if self.control_total:
#             print("Mision cumplida. Humanos domiandos. el mundo es delos gatos!")         
#         else:
#             print("Aun necesito mas caricias para completar el plan!")

# plan=DominacionMundial()
# plan.hipnotizar_humanos()
# plan.reclamar_teclado()
# plan.conquistar_mundo()

# ========================================================
# 1 COP = 0.000240532 USD
# 1 USD = 4,157.45 COP

# 1 EUR = 1.10285 USD
# 1 USD = 0.906738 EUR

# 1 JPY = 0.00683539 USD
# 1 USD = 146.297 JPY_/.,;'p[[=-----__++--_?¡![]]]

# print("\n---Conversor de Monedas---\n")

# ingrese_dolares=float(input("Ingrese la cantidad de USD a convertir: ").strip())

# def euros_usd(moneda):
#     return moneda * 1.10285

# def cop_usd(moneda):
#     return moneda * 0.000240532

# def yen_jp_usd(moneda):
#     return moneda * 0.00683539


# while True:
#         try:
#             print("\n---Menu---")
#             print("1 - Euros a USD.")
#             print("2 - COP a USD.")
#             print("3 - Yen Japónes.")
#             print("4 - Salir.")

#             opcion=input("Ingrese opción: ").strip()

#             if opcion == "1":
#                 euros_usd(ingrese_dolares)
#             elif opcion == "2":
#                 cop_usd(ingrese_dolares)
#             elif opcion == "3":
#                 yen_jp_usd(ingrese_dolares)
#             elif opcion == "4":
#                 print("---Gracias por utilzar nuestros servicios---")
#                 break 
#         except ValueError:
#             print("Ingrese un parámetro válido")    


# euros_usd(ingrese_dolares)
# cop_usd(ingrese_dolares)
# yen_jp_usd(ingrese_dolares)


# print(f"El precio de")

# print("\n--- Conversor de Monedas ---\n")

# def euros_a_usd(moneda):
#     return moneda * 0.906738

# def cop_a_usd(moneda):
#     return moneda * 4.157

# def yen_a_usd(moneda):
#     return moneda * 146.297

# while True:
#     try:
#         print(f"\n---Menú---")
#         print("1 - USD a Euros.")
#         print("2 - USD a Pesos Colombianos (COP).")
#         print("3 - USD a Yen Japónes.")
#         print("4 - Salir.")

#         opcion=input("Ingrese opción: ").strip()

#         if opcion == "1":
#             moneda=float(input("Ingrese la catidad de USD: ").strip())
#             print(f"{moneda} USD equivale a {euros_a_usd(moneda):.2f} Euros.")
#         elif opcion == "2":
#             moneda=float(input("Ingrese la cantidad de USD: ").strip())
#             print(f"{moneda} USD equivale a ${cop_a_usd(moneda):.2f} Pesos Colombianos.")
#         elif opcion == "3":
#             moneda=float(input("Ingrese la cantidad de USD: ").strip())
#             print(f"{moneda} USD equivales a {yen_a_usd(moneda):.2f}")
#         elif opcion == "4":
#             print("---Gracias por utilizar nuestros servicios---")
#             break 
#         else:
#             print("Opción inválida. Intente de nuevo.")

#     except ValueError:
#         print("Error: Ingrese un número válido.")               

print("\n--- Conversor de Monedas ---\n")
































