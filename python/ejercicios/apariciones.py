# # Enunciado

# # Apariciones: 
# # Realizar un algoritmo que reciba una cadena 
# # y devuelva un diccionario con la cantidad 
# # de apariciones de cada palabra en la cadena. 

# # Por ejemplo, si recibe "Qué lindo día que hace hoy" 
# # debe devolver: 
# # 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


# CADENA_TEXTO=str(input("Ingrese una frase: ")).split(" ")

# diccionarios={}

# for i, diccionario in enumerate(CADENA_TEXTO, start=1):
#     diccionarios[diccionario] = i
# print(diccionarios, i )

cadena=input("Ingrese una cadena de texto: ").lower()
palabras=cadena.split()
apariciones={}

for palabra in palabras:
    if palabra in apariciones:
        apariciones[palabra]+=1
    else:
        apariciones[palabra]=1


print("\nDiccionario de apariciones: ")
for palabra, cantidad in apariciones.items():
    print(f"'{palabra}':{cantidad}")















