cesta={}

while True:
    articulo=input("Ingrese nombre artículo: ( o 'FIN' para finalizar): ")
    if articulo.upper() == "FIN":
        break
    precio=float(input(f"Ingrese el precio de {articulo}: "))
    cesta[articulo]=precio

print("\nLista de la compra: ")
total=0
for articulo, precio, in cesta.items():
    print(f"{articulo}\t{precio}")  
    total += precio
print(f"\tTOTAL\t{total}")      




