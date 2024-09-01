import pandas as pd

# DataFrame: 

# Crea un programa que utilice la librería 
# Pandas para crear un DataFrame con la siguiente 
# información sobre 5 estudiantes: nombres, 
# edades y calificaciones. 

# Muestra el DataFrame resultante.

print("-"*60)
print()

estudiantes={
    "Nombre":           ["Juan Cataño", "Anita Lozano", "Carla España", "Samuel Tenorio", "Juaita Lucas"],
    "Edades":           [     20,            23,              24,           19,                 30      ],
    "Calificaciones" :  [     3.5,           36,               5,          4.6,                4.4      ]
}

df=pd.DataFrame(estudiantes)
print(df)

departamentos={
    "Departamentos" : ["Cundinamarca",      "Boyacá", "Quindio", "Meta"         ],
    "Ciudad" :        [   "Bogotá",         "Tunja",  "Armenia", "Villavicencio"],
    "Programadores" : [      7500,            1040,     1890,      400          ]
}

print("-"*60)
print()

df1=pd.DataFrame(departamentos)
print(df1)

print("-"*60)
print()


programadores={
    "Nombre":       ["Juan Cataño",     "Anita Lozano",     "Carla España",          "Samuel Tenorio", "Juaita Lucas"           ],
    "Experiencia":  ["Senior",          "Junior",           "Trainee",               "Semi-Senior",    "Junio"                  ],
    "Lenguaje":     ["Java",            "Python",           "Cobol",                 "Go",             "PHP"                    ],
    "Localización": ["Virtual",         "Precencial",       "Hibrido",               "Virtual",        "Virtual"                ],
    "Idioma":       ["Español",         "Español/Inglés",   "Italiano/Español",      "Español",        "Español/Mandarin"     ]
}

df2=pd.DataFrame(programadores)
print(df2)












