# casa = "a"
# perro = "antes"

# b = 0
# c = 5

# a = b or c

# color = "#FF0000"

# match color:
#     case "#FF0000":
#         print("🔴")
#     case "#00FF00":
#         print("🟢") 
#     case "#0000FF":
#         print("🔵")       


# color1="#AF549B"

# match color1:
#     case "#FF0000":
#             print("🔴")
#     case "#00FF00":
#     	    print("🟢")
#     case    "#0000FF":
#              print("🔵")
#     case _:        
#                  print("Unknown Color!")    



# point = (2, 5)

# match point:
#     case (x,y):
#         print(f"({x},{y}) is in plane")
#     case (x,y,z):
#         print(f"({x},{y},{x}) is in space")

# point = (3,1,7)

# match point:
#     case (x,y):
#         print(f"({x},{y}) is in plane")
#     case (x,y,z):
#         print(f"({x},{y},{z}) is in plane")

# print("-"*60)

# point2 = ("2","6")

# match point2:
#     case (x,y):
#         print(f"({x},{y}) is in plane")
#     case (x,y,z):
#         print(f"({x},{y},{z}) is in space")
#     case _:
#         print("Unknown ")        



# print("-"*60)


# point3 = ("2", "5")

# match point3:
#     case (int(), int()):
#         print(f"({point}) is in plane")
#     case (int(),int(),int())  :
#         print(f"({point}) is in space")
#     case _:
#         print("Unknown!")      


# print("-"*60)

# point4 = (3,1,9)

# match point4:
#     case (int(),int()):
#         print(f"({point}) is in plane")
#     case (int(),int(),int()):
#         print(f"({point4}) is in space")
#     case _:
#         print("Unknown!")        

# print("-"*60)

# point5 = (8,3,5)
# match point5:
#     case (int(x),int(y)):
#         dist_to_origin =(x ** 2 + y ** 2) ** (1 / 2)
#         print(dist_to_origin)
#     case (int(x), int(y), int(z)):
#         dist_to_origin =(x ** 2 + y ** 2 + z **2) ** (1 / 2)
#         print(dist_to_origin)
#     case _:
#         print("Unknown!")

# print("-"*60)

# point6 = ("8",3,6)
# match point6:
#     case (int(x), int(y)):
#         dist_to_origin = (x ** 2 + y ** 2) ** (1 / 2) 
#         print(dist_to_origin)
#     case (int(x), int(y), int(z)):
#         dist_to_origin =(x ** 2 + y ** 2 + z **2) ** (1 / 2)
#         print(dist_to_origin)
#     case _:
#         print("Unknown!")

# print("-"*60)

# #Lista de diccionarios

# auths=[
#     {"user_name": "juan", "password": "1234"},
#     {"email": "juan@gmail.com", "password": "43212"},
#     {"email": "tes@gmail.com", "password": "ABCD"},
#     {"user_name": "juan", "password": 1234}
# ]
# for auth in auths:
#     print(auth)
#     match auth:
#         case {"user_name": str(user_name), "password": str(password)}:
#             print("Authenticating witch username and password")
#             print(f"{user_name}:{password}")
#         case {"email": str(email), "token": str(token)}:
#             print("Authenticating with email and token")
#             print(f"{email}:{token}")
#         case _:
#             print("Authenticathing method not valid!")
#     print("-"*10)        


# autenticacion=[
#     {"nombre_usuario": "juan", "contrasena": "1234"},
#     {"email": "juan@gmail.com", "token": "1234"},
#     {"email": "juan@gmail.com", "contrasena": "ABCD"},
#     {"nombre_usuario": "juan", "token": 1234}
# ]

# for autenticar in autenticacion:
#     print(autenticar)
#     match autenticar:
#         case {"nombre_usuario": str(nombre_usuario), "contrasena": str(contrasena)}:
#             print("1")
#             print("Autenticación con Nombre Usuario y Contraseña")
#             print(f"{nombre_usuario}:{contrasena}")
#         case {"email": str(email), "token": str(token)}:
#             print("2")
#             print("Autenticación con Nombre Usuario y Contraseña")
#             print(f"{email}:{token}") 
#         case {"email": str(email), "contrasena": str(contrasena)}:
#             print("3")
#             print("Autenticación con Nombre Usuario y Contraseña")
#             print(f"{email}:{contrasena}")
#         case {"nombre_usuario": str(nombre_usuario), "token": int(token)}: 
#             print("4")
#             print("Autenticación con Nombre Usuario y Contraseña")
#             print(f"{nombre_usuario}:{token}")   
#         case _:
#             print("Ingrese nombre usurio y contraseña correctos")
#     print("-"*10)    

# print("-"*60)

age=21

match age:
    case 0 | None:
        print("Not a person")
    case n if n < 17:
        print("Nop")
    case n if n < 22:
        print("Not is the USA")
    case _:
        print("Yes!")

print("-"*40)        


# Operador MORSE

# print("\n")

# radius=4.5
# perimeter= 2 * 3.14 * radius
# if perimeter < 100:
#     print("Increase radius to reach minimunperimeter")
#     print("Actual perimeter: ", perimeter)

# print("-"*60)

# radius = 4.5
# if (perimeter := 2 * 3.14 * radius) < 100:
#     print("Increase radius to reach minimunperimeter")
#     print("Actual perimeter: ", perimeter)

# print("-"*60)


# saludos = "S"

# while saludos == "S":
#     print("Hola qué tal!")
#     saludos = input("Quieres otro saludos? [S/N] ")
# print("Que tengas buen día!")


print("-"*60)


# MAX_GREETS = 4
# num_greets = 0
# saludos = "S"

# while saludos == "S":
#     print("Hola qué tal!")
#     num_greets += 1
#     if num_greets == MAX_GREETS:
#         print("Máximo número de saludos alcanzado.")
#         break
#     saludos = input("Quieres otro saludos? [S/N] ")
# print("Que tengas buen día!")











print("-"*60)


