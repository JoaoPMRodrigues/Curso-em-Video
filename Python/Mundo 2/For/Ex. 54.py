n = int(input("Quantas pessoas têm no grupo? "))
maior = menor = 0
for i in range(n):
    nascimento = int(input("Digite seu ano de nascimento: "))
    idade = 2025-nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"No grupo tem {maior} maiores de idade e {menor} menores de idade.")
