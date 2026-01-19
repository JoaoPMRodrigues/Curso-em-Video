pessoas = []
velho = []
mulheres = []

tot_idade = media = 0
while True:
    dados = {}
    dados["nome"] = str(input("Nome: "))
    dados["idade"] = int(input("Idade: "))
    while True:  # dados["Sexo"]
        dados["sexo"] = str(input("Sexo: [M/F] ")).upper()
        if dados["sexo"] in "MF":
            break
        else:
            print("Erro! Por favor, digite apenas M ou F.")
    tot_idade += dados["idade"]
    pessoas.append(dados.copy())
    
    rsp = str(input("Quer continuar? [S/N] "))
    if rsp in "Nn":
        break
media = float(tot_idade/len(pessoas))
for i in pessoas:
    if i["sexo"] == "F":
        mulheres.append(i["nome"])
    if i["idade"] > media:
        velho.append(i)
print("-="*30)
print(f"O grupo tem {len(pessoas)} pessoas.")
print(f"A media das idades é: {media:.2f}")
print(f"as mulheres do grupo são: {mulheres}")
print(f"As pessoas com idade acima da média são:", end=" ")
for i in velho:
    print(f"\n{i}")
