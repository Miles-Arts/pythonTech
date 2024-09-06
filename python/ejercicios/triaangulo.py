# print("---Triángulo Rectángulo---")
# altura=int(input("Ingrese la Altura: "))

# for i in range(1, altura + 1, 2):
#     for j in range(i, 0, -2):
#         print(j, end=" ")
#         # return
#     print()


altura=int(input("Ingrese numero entero: "))
           
           
if altura % 2 !=0:
    altura -= 1   

for i in range(2, altura + 2, 2):
    for j in range(i, 0, -2):
        print(j,  end=" ")        
    print()        
           
           
           
           
           
           
           
           
           