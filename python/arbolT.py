datos_arboles=[
    {
        "nombreComun": "Duraznillo",
        "descripcion": {
            "tamano": "20 mt",
            "color": "Verde",
            "caracteristicas": "Mediano",
            "comportamiento": "Crecimiento rápido"
        },
        "multimedia": {
            "fotos": ["ruta/foto1.png", "ruta/foto2.png"],
            "video": ["ruta/video1.mp4", "ruta/video2.mp4"]
        },
        "observacione": [
            {"fecha": "2024-06-08", "lugar": "Tuta - San Nicolás", "avistamiento": 20},
            {"fecha": "2024-08-20", "lugar": "Tuta - La Playa","avistamientos": 50}
        ]
    }
]


def mostrar_arboles():
    print(datos_arboles)

# print("Hola")
mostrar_arboles()