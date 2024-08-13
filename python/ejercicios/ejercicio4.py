# Enunciado 
# Tornillo: Cree un programa que solicite el tamaño 
# de un tornillo e imprima su tamaño de acuerdo 
# a las sigueintes condiciones:
# 
# De 1 cm(incluido) hasta 3 cm(no incluido) es pequeño 
# De 3 cm(incluido) hasta 5 cm(no incluido) es mediano 
# De 5 cm(incluido) hasta 6.5 cm(no incluido) es grande 
# de 6.5cm (incluido) hasta 8.5 cm(no incluido) es muy grande 
# De 8.5 cm(incluido) en adelante es gigante


tamano = float(input("Ingrese el tamaño del tornillo"))


if tamano >= 1 or tamano < 3:
    medida = "El tornillo 1 cm (incluido) hasta 3 cm (no incluido) es pequeño"
elif tamano >= 3 and tamano <= 5:
    medida = "De 3 cm(incluido) hasta 5 cm(no incluido) es mediano"
elif tamano >= 5 and tamano <= 6.5:
    medida = "De 5 cm(incluido) hasta 6.5 cm(no incluido) es grande"
elif tamano >= 6.5 and tamano <= 8.5:
    medida = "De 6.5cm (incluido) hasta 8.5 cm(no incluido) es muy grande"     
else:
    print("De 8.5 cm(incluido) en adelante es gigante")     

