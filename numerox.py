fim = int(input("Digite um número a imprimir:"))
x = 0
while (x <= fim):           #verificacao loop
    print("O valor eh:", x) #imprimindo x
    if(x%2 == 0):
        print("par")
    else:
        print("impar")
    x = x + 1               #contador

