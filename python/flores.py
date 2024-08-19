def hola():
    print("hola mi gente")

flores = [
    {"flores": "Girasol", "color": "amarillo", "precio": 20},
    {"flores": "Rosa", "color": "rojo", "precio": 10},
    {"flores": "Orquidea", "color": "morado", "precio": 40},
]


def ver_flores():
    print(flores)

def agregar_flores():
    print("Agregar Flores")

def editar_flores():
    print("Editar Flores")

def elimninar_flores():
    print("Eliminar Flores") 

def salir_menu():
    print("\n---FIN---")       


while True:
    print("---Menu Flores---")
    print("\n1. Ver flores.")
    print("2. Agregar flores.")
    print("3. Editar flores.")
    print("4. Eliminar flores.")
    print("5. Salir del menú.")
    opcion = input("\nIngrese un numero: ")
                 
    if opcion == "1":
        ver_flores()
    elif opcion == "2":
        agregar_flores()
    elif opcion == "3":
        editar_flores()
    elif opcion == "4":
        elimninar_flores()
    elif opcion == "5":
        salir_menu()
        break
    else:
        print("Dato incorrecto")                


    break