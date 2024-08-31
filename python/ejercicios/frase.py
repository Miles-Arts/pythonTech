entrada=input("Ingrese una frase: ").lower()
letra=input("Elija una letra: ").lower()

# salida = entrada.count(letra)

# print(salida)
   


if len(letra) == 1 and letra.isalpha():
    cantidad_apariciones = entrada.count(letra)
    print(f"La letra {letra} aparece {cantidad_apariciones} veces en la frase.")
else:
    print("Entrada no válida.")    
    print("Por favor, ingrese una letra.")    
























