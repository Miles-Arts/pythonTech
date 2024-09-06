decimal=int(input("Ingrese un número entero decimal: "))

absoluto=abs(decimal)

if absoluto == 0:
    resultado = "0"
else:
    hex_char="0123456789ABCDEF"
    hexadecimal=[]

    while absoluto > 0:

        hexadecimal.append(hex_char[absoluto % 16])
        # hexadecimal.append(str[absoluto % 2])
        absoluto//=16
        # absoluto//=2


    resultado= "".join(reversed(hexadecimal))    



if decimal < 0:
    resultado= "-" + resultado    
print(f"El equivalente hexadecimal es: {resultado}")












