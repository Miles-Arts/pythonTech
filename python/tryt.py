# while True print("Hola Gente")

# 10 *(1/0)

# "2" + 2

# Try Except
# 
# try:
#     print(x)    
# except:
#     print("Ocurrio una excepción")


# while True:
#     numero=input("Ingrese un numero: ")
#     try:
#         suma=numero+1
#     except TypeError:
#         print("\n No ha ingresado un número")
#     else:
#         break 
       
# print(suma)

# while True:
#     try:
#         numero=int(input("Ingrese un número: "))
#     except ValueError:
#         print("\n No ha ingresado un número")
#     else:
#         break;

# suma=numero+1
# print(suma)  

# print("------------------")

# while True:
#     try:
# #         x = int(input("Ingrese un número: "))
# #         break
# #     except ValueError:
# #         print("Error, sólo ingrese números. ")

# # print(x)

# # print("------------------")

# # try:
# #     print("Llamar...")
# # except:
# #     print("Error al llamar")
# # # else:
# # #     print("Entrando llamada...")     

# # # print("------------------")       

# # # try:
# # #     print(x)
# # # except:
# # #     print("Algo salió mal")
# # # finally:
# # #     print("El 'try except' ha terminado")        

# # # print("------------------")       

# # # try:
# # #     print(x)
# # # except NameError:
# # #     print("la variable x no está definida")
# # # finally:
# # #     print("El 'try except' ha terminado")  



# # # # x = -1
# # # # if x < 0:
# # # #     raise Exception("No hay número por debajo de cero")

# # # x = "Hello"
# # # if not type(x) is int:
# # #     raise TypeError("sólo se permite números enteros")

# # # Listas Operadores Especiales
# # print("------------------")  

# # lista=["a","b","c","d","a","b","c","d","a","b","c","d"]

# # while True:
# #     print("Nueva Busqueda")
# #     letra=input("ingresa la letra a buscar: ")
# #     indiceInicio=input("Indice para inicar búsqueda: ")
# #     indiceFinal=input("Indice para terminar búsqueda: ")
# #     noExiste=False
# #     try:
# #         indiceInicio=int(indiceInicio)
# #         indiceFinal=int(indiceFinal)
# #         try:
# #             posicion=lista.index(letra, indiceInicio, indiceFinal)
# #         except ValueError:
# #             noExiste=True
# #             raise 
# #     except ValueError as mensajeError:
# #         if(noExiste):
# #             print(f"La letra {letra} no esta en la lista.")
# #         else:
# #             print("Solo se puede ingresar numeros.") 
# #         print(f"Error: {mensajeError}")
# #     else:
# #         print(f"la letra \"{letra}\" está en la posición: ", posicion)
# #         respuesta=None
# #         while(respuesta!="2"):
# #             print("¿Desea buscar otra letra? \n1.si\n2.no")
# #             respuesta=input()
# #             if(respuesta=="1"):
# #                 break
# #             elif(respuesta=="2"):
# #                 continue       
# #             else:
# #                 print("Opción no válida")
# #         else:
# #             break
# # print("Busqueda finalizada")                        


# # Restaurante El COMELÓN
# # Nombre Cliente
# # Dirección
# # Cantidad de Productos
# # Nombres Productos
# # PRecio
# # 
# # Mostrar en CONSOLA
# # Nombre Cliente - Dirección - 5 productos con nombre precio.
# # 

# #  
# # VALIDAR DATOS de ENTRADA 
# #  

# print("---RESTAURANTE---")
# print("---EL COMELÓN---")

# def restaurante():
#     cliente={}
#     continuar="s"
#     while continuar=="s":
#         print("Bienvenidos")
#         nombre_cliente=input("Ingrese su nombre: ")
#         direccion_cliente=input("Ingrese su dirección: ")
#         # continuar2="s"
#         lista_productos=[]
#         # while continuar2=="s":
#         for i in range(1,6): 
#             print(f"Producto numero: {i} ")
#             nombre_productos=input("Ingrese nombre productos: ")
#             precio_productos=float(input("Ingrese precio de productos: $"))
#             lista_productos.append((nombre_productos,precio_productos))
#             cliente[(nombre_cliente,direccion_cliente)]=lista_productos
#             # continuar2=input("Desea añadir más productos? [s/n]")
#             i+=1     
#         continuar=input("¿Desea ingresar más productos? [s/n]")  
#     return cliente      

# def imprimir(cliente):
#     print("--------------")
#     for nombre_cliente in cliente:
#         print("Cliente: ", nombre_cliente[0])
#         for nombre_cliente, lista_productos in cliente:
#             print("Con dirección: " , lista_productos)
#             print("Lista completa de productos")

# def productos(cliente):
#     # lista_productos=str(input("Nombre Cliente: "))
#     for lista_productos in cliente:
#         for nombre_producto, precio_productos in cliente[lista_productos]:
#             print(f"Producto: {nombre_producto}")
#             print(f"Precio: ${precio_productos}")

# # Mostrar el SUB TOTAL - IVA 19%
# # Total a PAGAR 
# # DESCUENTO 25% por cada 2 PRODUCTOS sobre el valor del producto
# # def precio(cliente):
# #      for lista_productos in cliente:
# #          for precio_productos in lista_productos:
# #             try:    
# #                 # precios_numericos = [float(p) for p in precio_productos]
# #                 precio_sin_iva = sum(precio_productos)
# #                 # precio_producto = int(precio_productos[1,2])
# #                 iva = 0.19
# #                 # precio_producto= sum(precio_producto)
# #                 precio_producto_iva=precio_sin_iva + (precio_sin_iva * iva)
# #                 print(f"Precio {precio_producto_iva:.2f}")
# #             except:
# #                 print("ERROR")    


# def precio(cliente):
#     for (nombre_cliente, direccion_cliente), lista_productos in cliente.items():
#         total_sin_iva = sum(precio for nombre, precio in lista_productos)
#         iva = 0.19
#         total_con_iva = total_sin_iva + (total_sin_iva * iva)
        
#         # Descuento del 25% por cada 2 productos
#         descuento = 0
#         if len(lista_productos) >= 2:
#             descuento = sum(precio for nombre, precio in lista_productos) * 0.25
        
#         total_con_descuento = total_con_iva - descuento
        
#         print(f"Cliente: {nombre_cliente}")
#         print(f"Total sin IVA: ${total_sin_iva:.2f}")
#         print(f"Total con IVA: ${total_con_iva:.2f}")
#         print(f"Descuento: ${descuento:.2f}")
#         print(f"Total a pagar: ${total_con_descuento:.2f}")
#         print("--------------")

# cliente=restaurante()
# imprimir(cliente)  
# productos(cliente) 
# precio(cliente)       


# RECURSIVIDAD

# def jugar(intento=1):
#     try:
#             respuesta=str(input("¿De qué color es la naranja?: ").lower())
#             if respuesta != "naranja":         
#                 if intento < 3:
#                     print("\nFallaste! Inténtalo de nuevo")
#                     intento+=1
#                     jugar(intento)
#                 else:
#                     print("\nPerdiste!") 
                     
#             else:
#                 print("\nGanaste!")
#     except ValueError:
#          print("err")
               
              
# jugar()        
# --------------------------------------

# LISTA MULTIDIMENSIONAL

# matriz=[[1,2,3], [4,5,6], [7,8,["a",True,0.9]]]

# print(matriz)
# print(matriz[0])
# print(matriz[0][1])
# print(matriz[2][2][1])

# print("---------------")

# matriz=[[1,2,3], [4,5,6], [7,8,["a",True,0.9]]]

# for fila in matriz:
#     print(fila)


# LISTA MULTIDIMENSIONAL
print("---------------")

# matriz=[[1,2,3], [4,5,6], [7,8,["a",True,0.9]]]

# for fila in matriz:
#     print(fila[2])

# for i in range(len(matriz)):
#     print(matriz[2][i])

# for i in range(len(matriz)):
#     print(matriz[i][2])  
# 
# # LISTA MULTIDIMENSIONAL
# print("---------------")

# matriz=[
#     [1,2,3], 
#     [4,5,6], 
#     [7,8,["a",True,0.9]]
#     ]

# for fila in range(len(matriz)):
#     for columna in range(len(matriz[fila])):
#         print(matriz[fila][columna], end="")
#     print()

# print("---------------")

# sublista=matriz[2][2]       

# for valor in sublista:
#     print(valor)

# print("---------------")

# matriz=[
#     [1,2,3], 
#     [4,5,6], 
#     [7,8,["a",True,0.9]]
#     ]

# for fila in  matriz:
#     for columna in fila:
#         print(columna, end="")
#     print()    


# MATRICES IRREGULARES
# print("---------------")

# irregulares=[
#     [15,2,8,5,3],
#     [3,3,7],
#     [9,1,16,13],
#     [],
#     [5]
# ]

# for column in irregulares:
#     for item in column:
#         print(item, end=" ")
#     print("")

# 183


# LISTA de COMPRESION


# [print([columna for columna in fila]) for fila in matriz ]
# [print([columna[fila] for columna in matriz]) for fila in range(len(matriz)) ]


# matriz.append([9,10,11])
# matriz[0].extend([12,13,14])
# matriz[2].reverse()

# print(matriz)

# print("---------------")

# matriz=[     
#     [1,2,3], 
#     [4,5,6], 
#     [7,8,["a",True,0.9]]
#     ]

# matriz[0][0]="m"
# matriz[1][2]="n"
# matriz[2][1]="o"

# print(matriz)

# print("---------------")
# import random

# matriz=[     
#     [1,2,3], 
#     [4,5,6], 
#     [7,8,["a",True,0.9]]
#     ]

# filas=int(input("Ingrese el número de filas: "))
# columnas=int(input("Ingrese el número de columnas: "))
# matriz=[]

# # matriz=[[random.randint(0,9) for c in range(columnas)] for f in range(filas)]

# # print(matriz)

# for f in range(filas):
#     temporal=[]
#     for c in range(columnas):
#         temporal.append(random.randint(0,9))
#     matriz.append(temporal)    

# print(matriz)

print("---------------")

fila=[]

for f in range(3):
    columna=[]
    for c in range(5):
        columna.append(0)
    fila.append(columna)  

for columna in fila:
    for valor in columna:
        print(valor, end=" ")
    print          







