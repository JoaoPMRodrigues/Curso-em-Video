num = []
maiorValor = -float("inf")
menorValor = float("inf")
for i in range(5):
    num.append(int(input("Digiite um numero: ")))
    if num[i] > maiorValor:
        maiorValor = num[i]
        pmaior = i
    elif num[i] < menorValor:
        menorValor = num[i]
        pmenor = i

print(f"O maior valor da lista é {maiorValor} e está na posição {pmaior}")
print(f"O menor valor da lista é {menorValor} e está na posição {pmenor}")
