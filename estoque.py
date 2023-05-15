nome_produto = input("Digite o nome do produto que deseja comprar:_")

preco_produto = float(input("Digite o preco do produto:_"))

qtde_produto = int(input("Digite a quantidade que deseja comprar:_"))

total_pagar = preco_produto * qtde_produto

print("---------------------------")
print("     LISTA DE COMPRAS      ")
print("---------------------------")
print(nome_produto)
print(preco_produto, "x", qtde_produto, "=", total_pagar)
print("---------------------------")