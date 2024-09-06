decimal=int(input())
absoluto=abs(decimal)

if  absoluto == 0:
    resultado = "0"
else:
    hexadecimal=[]

    while absoluto > 0:
        hexadecimal.append(str(absoluto % 2))
        absoluto//=2
    resultado= "".join(reversed(hexadecimal))    

print(resultado)












