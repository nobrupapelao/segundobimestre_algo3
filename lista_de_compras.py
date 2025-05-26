compras = []
opcao = input(print("Voce deseja adicionar mais algo ?"))
while opcao=="sim":
    adicionar=input("quais itens deseja adicionar ?apenas um por vez.")
    compras.append(adicionar)
    print(compras)
    opcao=input("deseja continuar?")

organizar=input("deseja organisar a lista?")

if organizar=="sim":
    compras_ordenadas=sorted(compras)
    print(compras_ordenadas)
    
    for item in compras:
        print("-", item)

elif organizar=="nao":
    print(compras)