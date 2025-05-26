compras = ["pao", "cafe", "leite"]
print(compras)

#pode ser removido pelo nome ou pelo indice
compras.remove(compras[0])
print(compras)

compras.append("açucar" )
print(compras)
#append acrescenta um item por vez

compras_ordenada = sorted(compras)
print(compras_ordenada)

for panela in compras:
    print("-", panela)
    #independente do nome apos o for , vair rodar do msm jeito

    