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

print("------------------")       

try:
    print(x)
except NameError:
    print("la variable x no está definida")
finally:
    print("El 'try except' ha terminado")  