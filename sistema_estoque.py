nome = input("Digite o seu nome:_")
cpf = input("Digite o seu CPF:_")
print("----------------------")

codigo_produto1 = "1234" #cod produto
produto1 = input("Digite o nome do produto:_")
preco_produto1 = float(input("Informe o preço do produto:_"))
qtde_produto1 = int(input("Digite a quantidade:_"))
print("----------------------")

codigo_produto2 = "1548" #cod produto
produto2 = input("Digite o nome do produto:_")
preco_produto2 = float(input("Informe o preço do produto:_"))
qtde_produto2 = int(input("Digite a quantidade:_"))
print("----------------------")

codigo_produto3 = "4521" #cod produto
produto3 = input("Digite o nome do produto:_")
preco_produto3 = float(input("Informe o preço do produto:_"))
qtde_produto3 = int(input("Digite a quantidade:_"))
print("----------------------")

total_pagar = float

total_produto1 = float #declaração de variáveis
total_produto2 = float
total_produto3 = float
reajuste = float

total_produto1 = preco_produto1 * qtde_produto1
total_produto2 = preco_produto2 * qtde_produto2
total_produto3 = preco_produto3 * qtde_produto3

total_pagar = total_produto1+ total_produto2 + total_produto3

reajuste = total_pagar - (total_pagar * 0.10)

print("[1]. DINHEIRO")
print("[2]. CARTÃO DE DÉBITO")
print("[3]. CARTÃO DE CRÉDITO")
print("[4]. PIX")

opcao = int(input("Como deseja efetuar o pagamento:_"))

if(opcao == 1):

    print("---LISTA DE COMPRAS---")
    print(produto1)
    print(codigo_produto1, preco_produto1, "x", qtde_produto1, "=", total_produto1)
    print(produto2)
    print(codigo_produto2, preco_produto2, "x", qtde_produto2, "=", total_produto2)
    print(produto3)
    print(codigo_produto3, preco_produto3, "x", qtde_produto3, "=", total_produto3)
    print("TOTAL A PAGAR: ", total_pagar)
    print("VALOR A PAGAR C/ DESCONTO: ", reajuste)
    print("--PAGO VIA DINHEIRO--")
    print("----------------------")
    print("NOME: ", nome)
    print("CPF: ", cpf)
    print("----------------------")
    
elif (opcao == 2):
    
    print("---LISTA DE COMPRAS---")
    print(produto1)
    print(preco_produto1, "x", qtde_produto1, "=", total_produto1)
    print(produto2)
    print(codigo_produto2, preco_produto2, "x", qtde_produto2, "=", total_produto2)
    print(produto3)
    print(codigo_produto3, preco_produto3, "x", qtde_produto3, "=", total_produto3)
    print("TOTAL A PAGAR: ", total_pagar)
    print("--PAGO VIA C. DE DÉBITO--")
    print("----------------------")
    print("NOME: ", nome)
    print("CPF: ", cpf)
    print("----------------------")
elif (opcao == 3):
    print("---LISTA DE COMPRAS---")
    print(produto1)
    print(codigo_produto1, preco_produto1, "x", qtde_produto1, "=", total_produto1)
    print(produto2)
    print(codigo_produto2, preco_produto2, "x", qtde_produto2, "=", total_produto2)
    print(produto3)
    print(codigo_produto3, preco_produto3, "x", qtde_produto3, "=", total_produto3)
    print("TOTAL A PAGAR: ", total_pagar)
    print("--PAGO VIA C. DE CRÉDITO--")
    print("----------------------")
    print("NOME: ", nome)
    print("CPF: ", cpf)
    print("----------------------")
    
elif (opcao == 4 ):
    print("---LISTA DE COMPRAS---")
    print(produto1)
    print(codigo_produto1, preco_produto1, "x", qtde_produto1, "=", total_produto1)
    print(produto2)
    print(codigo_produto2, preco_produto2, "x", qtde_produto2, "=", total_produto2)
    print(produto3)
    print(codigo_produto3, preco_produto3, "x", qtde_produto3, "=", total_produto3)
    print("TOTAL A PAGAR: ", total_pagar)
    print("VALOR A PAGAR C/ DESCONTO: ", reajuste)
    print("--PAGO VIA PIX--")
    print("----------------------")
    print("NOME: ", nome)
    print("CPF: ", cpf)
    print("----------------------")
    
else:
    print("Método de pagamento inválido!")