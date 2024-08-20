

ciudades = [
    {"Ciudad": "Bogotaá", "Departamento": "Cundinamarca", "clima": "frío"},
    {"Ciudad": "Medellín", "Departamento": "Antioquia", "clima": "templado"},
    {"Ciudad": "Tunja", "Departamento": "Boyacá", "clima": "frío"}
]

def mostrar_ciudades():
    print("---Ciudades---")
    print(ciudades)

def anadir_ciudad():
    print("--Añadir Ciudad--")

def editar_ciudad():
    print("--Editar Ciudad--")    

def eliminar_ciudad():
    print("---Eliminador---")
    sin_eliminar = str(input("Ingrese el valor a eliminar: "))
    cantidad_casas_anterior = len(ciudades)
    ciudades[:]=[ciudad for ciudad in ciudades if sin_eliminar != ciudad["ciudad"]]
    if cantidad_casas_anterior > len(ciudades):
        print("Casa eliminada")
    else:
        ("Ingrese un parametro válido")    
    print(ciudades)

def menu_ciudades():
    while True:
      print("---Menu Ciudades---")  
      print("")
      print("1. Mostrar Ciudades")
      print("2. Añadir Ciudades")
      print("3. Editar Ciudades")
      print("4. Eliminar Ciudades")
      print("5. Salir del menú")
      print("")
      opcion = int(input("Ingrese número: "))

      if opcion == 1:
            mostrar_ciudades()
      elif opcion == 2:
            anadir_ciudad()
      elif opcion == 3:
            editar_ciudad()
      elif opcion == 4:
            eliminar_ciudad()
      elif opcion == 4:
           print("")
           print("---Fin---")   
      else:
           print("Ingrese un parámetro válido")                    


     






mostrar_ciudades()



eliminar_ciudad()
