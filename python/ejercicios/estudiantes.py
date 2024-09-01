import pandas as pd

# DataFrame: 

# Crea un programa que utilice la librería 
# Pandas para crear un DataFrame con la siguiente 
# información sobre 5 estudiantes: nombres, 
# edades y calificaciones. 

# Muestra el DataFrame resultante.


estudiantes={
    "Nombre":           ["Juan Cataño", "Anita Lozano", "Carla España", "Samuel Tenorio", "Juaita Lucas"],
    "Edades":           [     20,            23,              24,           19,                 30      ],
    "Calificaciones" :  [     3.5,           36,               5,          4.6,                4.4      ]
}

df=pd.DataFrame(estudiantes)
print(df)

















