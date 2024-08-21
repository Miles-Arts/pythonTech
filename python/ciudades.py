

ciudades = [
    {"Departamento": "Cundinamarca", "Ciudad": "Bogotá", "Clima": "frío"},
    {"Departamento": "Antioquia", "Ciudad": "Medellín", "Clima": "templado"},
    {"Departamento": "Boyacá", "Ciudad": "Tunja", "Clima": "frío"}
]

def mostrar_ciudades():
    print("---Ciudades---")
    print(ciudades)

def anadir_ciudad():
    print("--Añadir Ciudad--")
    ciudad = input("Ingrese una nueva ciudad: ")
    departamento= input("Ingrese nuevo departamento: ")
    clima= input("Ingrese nuevo clima: ")
    nueva_ciudad={"Ciudad": ciudad, "Departamento": departamento, "Clima": clima}
    ciudades.append(nueva_ciudad)

def editar_ciudad():
    print("--Editar Ciudad--")    
    ciudad = input("Ingrese la ciudad a editar: ")
    for ciudad_ed in ciudades:
        if ciudad == ciudad_ed["Ciudad"]:
            nuevo_departamento=input("Ingrese la edición del departamento: ")
            nuevo_clima=input("Ingrese clima a editar: ")
            ciudad_ed["Departamento"]=nuevo_departamento
            ciudad_ed["Clima"]=nuevo_clima
            print("Ciudad Actualizada")
            return
    print("ingrese un dato válido")          

def eliminar_ciudad():
    print("---Eliminador---")
    sin_eliminar = str(input("Ingrese el valor a eliminar: "))
    cantidad_casas_anterior = len(ciudades)
    ciudades[:]=[ciudad for ciudad in ciudades if sin_eliminar != ciudad["Ciudad"]]
    if cantidad_casas_anterior > len(ciudades):
        print("Casa eliminada")
    else:
        print("Ciudad no encontrada")    
    print(ciudades)

def menu_ciudades():
    while True:
      print("")
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


     






menu_ciudades()



# eliminar_ciudad()
help(id)