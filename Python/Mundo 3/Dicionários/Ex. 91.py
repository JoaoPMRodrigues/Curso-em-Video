from random import randint
dados = list()
jogador = {}
for i in range(4):
    jogador["nome"] = str(input("Nome: "))
    jogador["resultado"] = int(randint(1, 6))
    dados.append(jogador.copy())
print("-=-=-=Resultados-=-=-=")
for j in dados:
    print(f"{j["nome"]} tirou {j["resultado"]}.")
for i in range(4):
    for j in range(i, 4):
        if dados[i]["resultado"] < dados[j]["resultado"]:
            dados[i], dados[j] = dados[j], dados[i]
print("-=-=-=Premições-=-=-=")
c=1
for j in dados:
    print(f"{c}º lugar: {j["nome"]} com {j["resultado"]}pontos")
    c+=1
