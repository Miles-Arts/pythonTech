entrada=str(input("Ingrese la frase: ")).lower()
frase=entrada.split()
frases={}

for palabra in entrada:
    if palabra in frases:
        frases[palabra]+=1
    else:
        frases[palabra]=1

print("Palabras Repetidas")

for clave, valor in frases.items():
    print(f"{clave} y {valor}")













