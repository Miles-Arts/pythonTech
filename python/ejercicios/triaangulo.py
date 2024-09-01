print("---Triángulo Rectángulo---")
altura=int(input("Ingrese la Altura: "))

for i in range(1, altura + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
        # return
    print()


