numero=int(input("Ingrese un número: "))

cuadrado =0
nivel=0

while cuadrado < numero:
    nivel+=1
    cuadrado= nivel * nivel

    triangular = (nivel*(nivel+1))//2


if cuadrado == numero:
    print(f"{numero} es adecuado para apilar en forma cuadrado")
else:
    print(f"{numero} no es adecuado para apilar en forma cuadrada.")


















