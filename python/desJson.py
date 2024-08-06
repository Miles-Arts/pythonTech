import json

# Objeto Python (diccionario)
data = '''{
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["lectura", "música", "deportes"]
}'''

# Serialización: Convertir el objeto Python a una cadena JSON
# json_data = json.dumps(data, indent=4)
# print("Cadena JSON:")
# print(json_data)

# Deserialización: Convertir la cadena JSON de nuevo a un objeto Python
data_from_json = json.loads(data)
print("\nObjeto Python:")
print(data_from_json)

# Acceder a los datos del diccionario deserializado
print("\nDatos deserializados:")
print(f"Nombre: {data_from_json['nombre']}")
print(f"Edad: {data_from_json['edad']}")
print(f"Ciudad: {data_from_json['ciudad']}")
print(f"Hobbies: {', '.join(data_from_json['hobbies'])}")