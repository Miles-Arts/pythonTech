import statistics as prom
# # def materias():
# #     materias={}
# #     continuar="s"
# #     while continuar == "s":
# #     #     print("Ingrese las materias: ")
# #     #     materia=str(input("Ingrese materias: "))
# #         continuar1="s"
# #         lista=[]
# #         while continuar1 == "s":
# #                 materia=str(input("Escriba Materia: "))
# #                 nota=float(input("Ingrese nota: "))
# #                 lista.append((materia,nota))
# #                 materias[lista]
# #         continuar1=input("Agregar otra materia? (S/N)")
# #     return materias    


# # materias()








# def agregar_materias():
#     # cantidad=int(input("Ingrese cantidad materias: "))
#     # for _ in range(cantidad):
    
#     materias={}
#     continuar = "s"
#     while continuar == "s":
#         print("Ingrese materias")
#         materia=str(input("Ingrese la materia: "))
#         nota=float(input("Ingrese la nota: "))
#         materias[materia]=(nota)
#         continuar=input("Desea continuar (S/N) ")
#         # can_materias={"materia": materia, "nota": nota}
#         # materias.append(can_materias)
#     return materias

# def imprimir(materias):
#      print("\n ---Materias--- \n")
#      print(materias)
#     #  for materia in materias:
#     #      print(materia, materias) 
        
# materia_notas= agregar_materias()
# imprimir(materia_notas)


materias = [
    "Matemáticas", 
    "Física", 
    "Química", 
    "Historia", 
    "Lenguaje", 
    "Programacóin"
]

notas=[]

for materia in materias:
    nota=float(input(F"Ingrese la nota de {materia}: "))
    notas.append(nota)

promedio = prom.mean(notas)

print("\nResumen de notas:")
for i in range(len(materias)):
    print(f"En {materias[i]} has sacado {notas[i]}")
print(f"Promedio de notas: {promedio}")



















