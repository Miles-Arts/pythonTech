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


print(f"\n---Gestor de Calificaciones Escolares---\n")

#entrada de datos
num_estudiantes=int(input("Ingresa cantidad de estudiantes: "))
estudiantes=[]

for i in range(num_estudiantes):
    print(f"\nIngresando datos de estudiantes {i+1}")
    nombre=str(input("Nombre de estudiante: ")).title()
    notas=[] #lista para almacenar notas

        #pedir 3 calificaiones
    for j in range(3):
        nota=float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)

    #guardar estudiante
    estudiante={
        "nombre": nombre,
        "notas": notas,
        "promedio": sum(notas) / len(notas) #calcular promedio
    }
    estudiantes.append(estudiante)

#Procesamieto de datos
mejor_estudiantes=max(estudiantes, key=lambda e: e['promedio']) 
peor_estudiantes=min(estudiantes, key=lambda e: e['promedio'])   
estudiantes_aprobados=sum(1 for aprobo in estudiantes if aprobo['promedio'] >= 3.0)
lista_ordenada=sorted(estudiantes, key=lambda e: e['promedio'], reverse=True)

#Funcion para calificar notas
def clasificar_nota(nota):
    if nota >= 4.5:
        return "Excelente"
    elif nota >= 4.0:
        return "Muy bien"
    elif nota >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"            

#Salida de datos
print(f"\n---Resumen de calificaciones---")

for e in estudiantes:
    estado=clasificar_nota(e['promedio'])
    print(f"\nEstudiante: {e['nombre']}")
    print(f"Notas: {e['notas']}")
    print(f"Promedio: {e['promedio']:.2f} - {estado}.")

print(f"\nMejor estudiante {mejor_estudiantes['nombre']} con {mejor_estudiantes['promedio']:.2f}")    
print(f"Peor estudiante {peor_estudiantes['nombre']} con {peor_estudiantes['promedio']:.2f}")
print(f"Estudiantes aprobados: {estudiantes_aprobados} de {num_estudiantes}")

print(f"\nLista de estudiantes ordenados por promedio:")
for e in lista_ordenada:
    estado=clasificar_nota(e['promedio'])
    print(f"{e['nombre']}: {e['promedio']:.2f} - {estado}.")


























