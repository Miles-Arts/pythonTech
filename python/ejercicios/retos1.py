peso=float(input("Ingrese peso tornillo en gramos: "))

if peso >= 1 and peso < 3:
    print("El tornillo es ligero.")
elif  peso >= 3 and peso < 5 :
    print("El tornillo es medio.")
elif  peso >= 5 and peso < 7.5 :
    print("El tornillo es pesado.")
elif  peso >= 7.5 and peso <= 10 :
    print("El tornillo es muy pesado.")
elif  peso > 10 :
    print("El tornillo es extremadamente pesado.") 
else:
    print("El peso ingresado no es valido.")   








