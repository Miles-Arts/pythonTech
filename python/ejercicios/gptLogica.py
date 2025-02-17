import random 
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

print(f"\n---Cajero Automático---\n")
pin=1234
saldo=20
retiro=0
nuevo_saldo=0

pin_cuenta=int(input("Ingrese el pin: "))

for i in range(1):
    if pin == pin_cuenta:
        print("Pin correcto!")
        print(f"El Saldo de la cuenta es: {saldo}")

    elif pin != pin_cuenta:
        for i in range(3):
            print(f"Intento {i+1}")
            print("El PIN es incorrecto: ingrese nuevamente")

def consultar_saldo(saldo):
    print(f"Saldo: ${saldo}")
    return

def retirar_dinero(saldo):
    saldo =- retiro   
    return saldo

def depositar_dinero(saldo):
    saldo += nuevo_saldo
    return saldo   
            
def menu():

    
    pass


























