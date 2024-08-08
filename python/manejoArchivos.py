import json
# JSON

# [{"clave1": 1,"clave2":2}]

# diccionario = {"nombre":"Rodolfo", "edad": 38, "ciudad": "cúcuta"}


# # dato= json.dumps(diccionario, ensure_ascii=False)
# dato= json.dumps(diccionario)

# print(dato)

# PASAR DE DICCIONARIO A JSON COPN DUMPS

# diccionario={
#     "nombre":"Rodolfo", 
#     "edad": 38, 
#     "ciudad": "cúcuta",
#     "padres": ("jose", "luisa"), #Tupla
#     "hijos": None,
#     "mascotas": [ #lista
#         {"tipo": "gato", "edad":2},
#         {"tipo": "perro", "edad":10}   
#     ]
# }

# datos= json.dumps(diccionario)
# datos= json.dumps(diccionario, indent=4, sort_keys=True, separators=(".","="))
# print(datos)

# PASAR DE JSON A DICCIONARIO CON LOADS
# objetoJSON = """
# {
#     "nombre": "Rodolfo",
#     "edad":34,
#     "ciudad":"Cúcuta"
# }
# """

# diccionario= json.loads(objetoJSON)
# print(diccionario)
# print(diccionario["nombre"])
# print(diccionario["edad"])
# print(diccionario["ciudad"])


# cadena1=""" 
# [
#     {
#         "codigo": "1",
#         "descripción": "papas",
#         "precio": "15"
#     },
#     {
#         "codigo": "2",
#         "descripción": "naranjas",
#         "precio": "25"
#     }
# ]
# """

# print(type(cadena1))
# print(cadena1)
# print("_"*80)
# lista=json.loads(cadena1)
# print(type(lista))
# print(lista)
# print("_"*80)
# cadena2=json.dumps(lista)
# print(type(cadena2))
# print(cadena2)

# contactos=[
#     (" Juanita", "Desarrolladora Back", "juanita@backmaria.com"),
#     ("Carla", "Analista", "carla@backmaria.com"),
#     ("José", "Desarrollador Front", "jose@backmaria.com"),
#     ("Peter", "Diseño UX/UI", "peter@backmaria.com")
# ]

# datos=[]

# for nombre, empleo, email in contactos:
#     datos.append({"nombre":nombre, "empleo":empleo, "email": email})

# with open("contactos.json") as archivoJson:
#     json.dump(datos, archivoJson)

# with open(contactos.json) as archivoJson:
#     datos = json.load(archivoJson)  
#     for contacto in datos:
#         print(contacto["nombre"], contacto["empleo"], contacto["email"])


# Convertir TUPLA a DICCIONARIO
# Desacople de tuplas

print("----------------")

lista=[
    ("usuario1", "cargo1", "email1"),
    ("usuario2", "cargo2", "email2"),
    ("usuario3", "cargo3", "email3"),
    ("usuario4", "cargo4", "email4")
]
# print("Tupla: ")
# print(lista)
datos =[]


print("Desacople de tuplas")
print("-------------")

# for nombre, cargo, email in ("usuario1", "cargo1", "email1"):


for nombre, cargo, email in lista:
    datos.append({ "nombre": nombre, "cargo": cargo, "email": email})

    # print(nombre, cargo, email)
print(f"a {datos}")

# Funcion apuntar la direccion del ARCHIVO
# ESCRIBIENDO COnvertir crear o sobre escribir archivo JSON
# Lo que encuentre en PYTHON lo pasa a JSON.
with open("usuarios.json", "w") as archivoJSON:
    json.dump(datos, archivoJSON)

# LEER del archivo JSON y convertir a Python
print(" ")
with open("usuarios.json", "r") as archivoJSON:
    datos = json.load(archivoJSON)
    print("Lectura de JSON")
    print(datos)

