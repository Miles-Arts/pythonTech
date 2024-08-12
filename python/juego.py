import puntaje

valores=[
    
    ("Pepe", 108, "4:16"),
    ("Juana", 2315, "8:42"),
    ("Paco", 315, "16:42"),
    ("Luisa", 6315, "4:16")
                          
]

puntaje.guardar_puntajes("puntajes.txt", valores)
recuperado = puntaje.recuperar_puntajes("puntajes.txt")
print(recuperado)























