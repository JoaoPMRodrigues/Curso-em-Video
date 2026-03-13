maior = -float("inf")
menor = float("inf")
for i in range(5):
    peso = float(input("Digite seu peso: "))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(maior)
print(menor)
