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



































