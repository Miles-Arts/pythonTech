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
objetoJSON = """
{
    "nombre": "Rodolfo",
    "edad":34,
    "ciudad":"Cúcuta"
}
"""

diccionario= json.loads(objetoJSON)
print(diccionario)
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["ciudad"])

