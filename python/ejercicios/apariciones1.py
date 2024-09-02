# # Enunciado

# # Apariciones: 
# # Realizar un algoritmo que reciba una cadena 
# # y devuelva un diccionario con la cantidad 
# # de apariciones de cada palabra en la cadena. 

# # Por ejemplo, si recibe "Qué lindo día que hace hoy" 
# # debe devolver: 
# # 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


# palabras_entrada=input("Ingrese cadena de texto: ").lower()
# palabras=palabras_entrada.split()
# diccionario={}

# for palabra in palabras:
#     if palabra in diccionario:
#         diccionario[palabra]+= 1
#     else:
#         diccionario[palabra]= 1

# print("Pabras")
# for clave, valor in diccionario.items():
#     print(f"'{clave}':{valor}")

entrada=input("Ingrese cadena de texto: ").lower()
palabras=entrada.split()
diccionario={}

for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra]+=1
    else:
        diccionario[palabra]=1

print("Palabras repetidas y cantidad")

for clave, valor in diccionario.items():
    print(f"{clave}:{valor}")














