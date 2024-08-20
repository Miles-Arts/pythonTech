def hola():
    print("hola mi gente")

flores_especies = [
    {"flores": "Girasol", "color": "amarillo", "precio": 20},
    {"flores": "Rosa", "color": "rojo", "precio": 10},
    {"flores": "Orquidea", "color": "morado", "precio": 40},
]


def ver_flores():
    print(flores_especies)

def agregar_flores():
    print("Agregar Flores")
    flores = input("Ingrese nueva flor: ")
    color = input("Ingrese color de la flor: ")
    precio = float(input("Ingrese valor de la flor: "))
    flor={"flores": flores, "color": color, "precio": precio}
    flores_especies.append(flor) 


def editar_flores():
    print("Editar Flores")
    editar_flor = input("Ingrese nombre flor a editar: ")
    for flor in flores_especies:
        if editar_flor == flor["flores"]:
            color_nuevo = input("Ingrese color de la flor: ")
            precio_nuevo = float(input("Ingrese valor de la flor: "))
            flor["color"]=color_nuevo
            flor["precio"]=precio_nuevo
            print("Flor editada")
            return
    print("\nIngrese un nombre válido")        



def elimninar_flores():
    print("Eliminar Flores") 
    eliminar_flor = input("Ingrese la flor a eliminar: ")
    flores_anterior = len(flores_especies)
    flores_especies[:]=[flor for flor in flores_especies if eliminar_flor != flor["flores"]]
    if flores_anterior > len(flores_especies):
        print("Flor eliminada")
    else:
        print("Escriba un parámetro válido")    

def menu_salir():
    print("\n---FIN---")       

def menu_flores():
    while True:
        print("\n---Menu Flores---")
        print("\n1. Ver flores.")
        print("2. Agregar flores.")
        print("3. Editar flores.")
        print("4. Eliminar flores.")
        print("5. Salir del menú.")
        opcion = int(input("\nIngrese un numero: "))
                    
        if opcion == 1:
            ver_flores()
        elif opcion == 2:
            agregar_flores()
        elif opcion == 3:
            editar_flores()
        elif opcion == 4:
            elimninar_flores()
        elif opcion == 5:
            menu_salir()
            break
        else:
            print("\nDato incorrecto")                
    
menu_flores()