# DICCIONARIOS

# CLAVE : VALOR, coma
#  mp hay POSICION
# Se buscan por las claves,

# con PARENTESIS son Funciones acciones,
# , cuando no tienen () con atributos

diccionario = {"clave1":"valor2", 2:True, "clave3": 79,
                4:"valor4", "clave5":[1,2,3], 6:("a", "b","c")}

print(diccionario)
print(len(diccionario))
print(diccionario[2])
print(diccionario["clave5"])
print(diccionario["clave1"] + " " + str (diccionario[2]))
diccionario[4] = False
print(diccionario)
diccionario["clave1"] = 67
print(diccionario)
diccionario["clave5"][1] = True
print(diccionario)
del diccionario["clave3"]
print(diccionario)
print("clave1" in diccionario)
print(4 not in diccionario)
print(len(diccionario))

# diccionario COLLecion no ordenada de valores
# Las claves no se repiten,



diccionario1 = {"clave1":"valor2", 2:True, "clave3": 79,
                4:"valor4", "clave5":[1,2,3], 6:("a", "b","c")}

print(diccionario1)
diccionario1 = dict([("clave1","valor2"), (2,True), ("clave3", 79), (4,"valor4"), ("clave5",[1,2,3]), (6,("a", "b","c"))])
print(diccionario)
diccionario1 = dict(clave1="valor2", clave2=True, clave3= 79, clave4="valor4", clave5=[1,2,3], clave6=("a", "b","c"))



































