# Enunciado 
# Letra en frase: 
# Escribir un programa en el que se pregunte 
# al usuario por una frase y una letra, 
# y muestre por pantalla el número 
# de veces que aparece la letra en la frase.



# frase = str(input("Escribe una frase: ").lower())
# letra = str(input("Ingrese una letra: "))

# for letras in frase:
#     letras.split()
#     # print(letras)
#     if letras == letra:
#         numero_letras = len(letras)
#         sum(numero_letras)
#         print(f"Hay {numero_letras} letras de la letra {letras}")
#         break    
# else:
#     print("no hay letra")    

hola = "holoholo"
letra = str(input("ingresa una letra: "))

hola = hola.split()

holas = []

holas.append(hola)

# print(len(holas))

# palabra = len(hola)

for letras in range(0, len(hola), 1):
        if letras == letra:
              # sum(letra)
            print(f"Encontramos  la letra {letra}")
        break
        
else:
    print(f"no hay letra {letra} ")


# print(palabra)







