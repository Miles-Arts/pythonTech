import json
# JSON

# [{"clave1": 1,"clave2":2}]

# diccionario = {"nombre":"Rodolfo", "edad": 38, "ciudad": "cúcuta"}


# # dato= json.dumps(diccionario, ensure_ascii=False)
# dato= json.dumps(diccionario)

# print(dato)

diccionario={
    "nombre":"Rodolfo", 
    "edad": 38, 
    "ciudad": "cúcuta",
    "padres": ("jose", "luisa"),
    "hijos": None,
    "mascotas": [
        {"tipo": "gato", "edad":2},
        {"tipo": "perro", "edad":10}   
    ]
}

datos= json.dumps(diccionario)
print(datos)


