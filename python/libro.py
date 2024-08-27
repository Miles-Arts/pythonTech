casa = "a"
perro = "antes"

b = 0
c = 5

a = b or c

color = "#FF0000"

match color:
    case "#FF0000":
        print("🔴")
    case "#00FF00":
        print("🟢") 
    case "#0000FF":
        print("🔵")       


color1="#AF549B"

# match color1:
#     case "#FF0000":
#             print("🔴")
#     case "#00FF00":
#     	    print("🟢")
#     case    "#0000FF":
#              print("🔵")
#     case _:        
#                  print("Unknown Color!")    



point = (2, 5)

match point:
    case (x,y):
        print(f"({x},{y}) is in plane")
    case (x,y,z):
        print(f"({x},{y},{x}) is in space")

point = (3,1,7)

match point:
    case (x,y):
        print(f"({x},{y}) is in plane")
    case (x,y,z):
        print(f"({x},{y},{z}) is in plane")

print("-"*60)

point2 = ("2","6")

match point2:
    case (x,y):
        print(f"({x},{y}) is in plane")
    case (x,y,z):
        print(f"({x},{y},{z}) is in space")
    case _:
        print("Unknown ")        



print("-"*60)


point3 = ("2", "5")

match point3:
    case (int(), int()):
        print(f"({point}) is in plane")
    case (int(),int(),int())  :
        print(f"({point}) is in space")
    case _:
        print("Unknown!")      


print("-"*60)

point4 = (3,1,9)

match point4:
    case (int(),int()):
        print(f"({point}) is in plane")
    case (int(),int(),int()):
        print(f"({point4}) is in space")
    case _:
        print("Unknown!")        






























print("-"*60)


