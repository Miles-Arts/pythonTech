

ciudades = [
    {"ciudad": "bogota", "departamento": "cundinamarca", "clima": "frío"},
    {"ciudad": "medellin", "departamento": "antioquia", "clima": "templado"},
    {"ciudad": "tunja", "departamento": "boyacá", "clima": "frío"}
]

def mostrar_ciudaes():
    print("---Ciudades---")
    print(ciudades)

def eliminar_elemento():
    print("---Eliminador---")
    sin_eliminar = str(input("Ingrese el valor a eliminar: "))
    cantidad_casas_anterior = len(ciudades)
    ciudades[:]=[ciudad for ciudad in ciudades if sin_eliminar != ciudad["ciudad"]]
    if cantidad_casas_anterior > len(ciudades):
        print("Casa eliminada")
    else:
        ("Ingrese un parametro válido")    
    print(ciudades)





eliminar_elemento()