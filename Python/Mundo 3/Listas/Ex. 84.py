pessoas = []
dados = []
maiorpeso = -float("inf")
total = c = 0
menorpeso = float("inf")
maispesado = []
maisleve = []
while True:
    print("-"*20)
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    if pessoas[c][1] >= maiorpeso:
        maiorpeso = dados[1]
    elif pessoas[c][1] <= menorpeso:
        menorpeso = dados[1]
    dados.clear()
    total += 1
    c += 1
    rsp = str(input("Quer continuar? [S/N]")).upper()
    if rsp in "N":
        break
for c in range(len(pessoas)-1):
    if pessoas[c][1] == maiorpeso:
        maispesado.append(pessoas[c][0])
    elif pessoas[c][1] == menorpeso:
        maisleve.append(pessoas[c][0])
print("-"*20)
# print(pessoas)
print(f"Ao todo, você cadastrou {total} pessoas.")
print(f"O maior peso foi de {maiorpeso:.2f}Kg. Peso de: {maispesado}")
print(f"O menor peso foi de {menorpeso:.2f}Kg. Peso de: {maisleve}")
