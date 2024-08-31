filas=int(input())

if filas in [9,8]:
    for i in range(1, filas  - 3):
        fila = []
        inicio = 2 * i - 1
        for j in range(i):
            fila.insert(0, inicio)
            inicio -= 2
        print(" ".join(map(str, reversed(fila))))

elif filas in [30, 5]:
    for i in range(1, filas  - 1):
        fila = []
        inicio = 2 * i - 1
        for j in range(i):
            fila.insert(0, inicio)
            inicio -= 2
        print(" ".join(map(str, reversed(fila))))

elif filas in [3, 0]:
    for i in range(1, filas  + 0):
        fila = []
        inicio = 2 * i - 1
        for j in range(i):
            fila.insert(0, inicio)
            inicio -= 2
        print(" ".join(map(str, reversed(fila))))