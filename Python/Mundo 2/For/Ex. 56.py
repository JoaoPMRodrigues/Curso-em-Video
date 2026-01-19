n = int(input("Quantas pessoas tem no grupo? "))
ivelho = 0
mulheres = 0
sidade = 0
for i in range(n):
    nome = str(input("Digite seu nome: "))
    genero = str(input("Digite seu gênero:").lower())
    idade = int(input("Digite sua idade: "))
    sidade += idade
    if genero == "masculino":
        if idade > ivelho:
            nvelho = nome
            ivelho = idade
    if genero == "feminino":
        if idade < 20:
            mulheres += 1

print(f"A média de idade do grupo é:{sidade/n}")
print(f"O nome do homem mais velho é: {nvelho}")
print(f"O numero de mulheres com menos de 20 anos é igual a {mulheres}")
