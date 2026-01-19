num = [[], []]

for i in range(7):
    n = int(input(f"Digite o {i+1} valor: "))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

for i in range(len(num[0])-1):
    for j in range(i+1, len(num[0])):
        if num[0][j] < num[0][i]:
            num[0][j], num[0][i] = num[0][i], num[0][j]

for i in range(len(num[1])-1):
    for j in range(i+1, len(num[1])):
        if num[1][j] < num[1][i]:
            num[1][j], num[1][i] = num[1][i], num[1][j]
print(f"Somente os pares: {num[0]}")
print(f"Somente os impares: {num[1]}")
