numero = int(input("Digite um numero para saber a tabuada: "))

for numero in range(numero, 5):
    print("Tabuada do ", numero)
    for numero2 in range(11):
        print(numero, "x", numero2, " = ", numero*numero2)
