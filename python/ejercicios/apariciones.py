# # Enunciado

# # Apariciones: 
# # Realizar un algoritmo que reciba una cadena 
# # y devuelva un diccionario con la cantidad 
# # de apariciones de cada palabra en la cadena. 

# # Por ejemplo, si recibe "Qué lindo día que hace hoy" 
# # debe devolver: 
# # 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


CADENA_TEXTO=str(input("Ingrese una frase: ")).rstrip()

diccionarios={}


for i, diccionario in enumerate(CADENA_TEXTO, start=1):
    diccionarios[diccionario] = i
print(diccionarios, i )







# VOWELS = 'aeiou'

# enum_vowels = {}

# for i, vowel in enumerate(VOWELS, start=1):
#     enum_vowels[vowel] = i
#     print(enum_vowels)













