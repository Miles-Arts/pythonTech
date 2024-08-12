import puntaje

valores=[("Pepe", 108, "4:16"),("Juana", 2315, "8:42")]

puntaje.guardar_puntajes("puntajes.txt", valores)
recuperado = puntaje.recuperar_puntajes("puntajes.txt")
print(recuperado)























