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
#         x = int(input("Ingrese un número: "))
#         break
#     except ValueError:
#         print("Error, sólo ingrese números. ")

# print(x)

# print("------------------")

# try:
#     print("Llamar...")
# except:
#     print("Error al llamar")
# else:
#     print("Entrando llamada...")     

# print("------------------")       

# try:
#     print(x)
# except:
#     print("Algo salió mal")
# finally:
#     print("El 'try except' ha terminado")        

# print("------------------")       

# try:
#     print(x)
# except NameError:
#     print("la variable x no está definida")
# finally:
#     print("El 'try except' ha terminado")  



# # x = -1
# # if x < 0:
# #     raise Exception("No hay número por debajo de cero")

# x = "Hello"
# if not type(x) is int:
#     raise TypeError("sólo se permite números enteros")

# Listas Operadores Especiales
print("------------------")  

lista=["a","b","c","d","a","b","c","d","a","b","c","d"]

while True:
    print("Nueva Busqueda")
    letra=input("ingresa la letra a buscar: ")
    indiceInicio=input("Indice para inicar búsqueda: ")
    indiceFinal=input("Indice para terminar búsqueda: ")
    noExiste=False
    try:
        indiceInicio=int(indiceInicio)
        indiceFinal=int(indiceFinal)
        try:
            posicion=lista.index(letra, indiceInicio, indiceFinal)
        except ValueError:
            noExiste=True
            raise 
    except ValueError as mensajeError:
        if(noExiste):
            print(f"La letra {letra} no esta en la lista.")
        else:
            print("Solo se puede ingresar numeros.") 
        print(f"Error: {mensajeError}")
    else:
        print(f"la letra \"{letra}\" está en la posición: ", posicion)
        respuesta=None
        while(respuesta!="2"):
            print("¿Desea buscar otra letra? \n1.si\n2.no")
            respuesta=input()
            if(respuesta=="1"):
                break
            elif(respuesta=="2"):
                continue       
            else:
                print("Opción no válida")
        else:
            break
print("Busqueda finalizada")                        


# Restaurante El COMELÓN
# Nombre Cliente
# Dirección
# Cantidad de Productos
# Nombres Productos
# PRecio
# 
# Mostrar en CONSOLA
# Nombre Cliente - Dirección - 5 productos con nombre precio.
# 
# Mostrar el SUB TOTAL - IVA 19%
# Total a PAGAR 
# DESCUENTO 25% por cada 2 PRODUCTOS sobre el valor del producto
#  
# VALIDAR DATOS de ENTRADA 
#  

























