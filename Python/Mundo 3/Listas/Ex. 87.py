mat = [[], [], []]
scol = spar = maiorvalor = 0

for l in range(3):
    for c in range(3):
        valor = (int(input(f"Digite um valor para [{l},{c}]: ")))
        mat[l].append(valor)

print("-"*30)

for l in range(3):
    for c in range(3):
        print(f"[ {mat[l][c]} ]", end=" ")
    print("\n")

for l in range(3):
    for c in range(3):
        if mat[l][c] % 2 == 0:
            spar += mat[l][c]

for l in range(3):
    scol += mat[l][2]

for c in range(3):
    if mat[1][c] > maiorvalor:
        maiorvalor = mat[1][c]

print("-"*30)
print(f"A soma dos pares é: {spar}")
print(f"A soma dos valores da segunda coluna é: {scol}")
print(f"O maior valor da segunda coluna é: {maiorvalor}")
