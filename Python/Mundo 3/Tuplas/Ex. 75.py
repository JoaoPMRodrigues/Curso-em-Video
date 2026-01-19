numeros = (int(input("Digite um número: ")), int(input("Digite um número: ")),
           int(input("Digite um número: ")), int(input("Digite um número: ")))
pares = []
print(f"O valor 9 apareceu {numeros.count(9)} vez(es)")
print(f"O valor 3 apareceu pela 1º vez na posição {numeros.index(3)}")
for i in range(4):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
print(f"Os numeros pares foram: {pares}")
