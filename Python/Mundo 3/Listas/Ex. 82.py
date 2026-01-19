num = []
pares = []
impares = []
rsp = ""
while True:
    n = int(input("Digite um numero: "))
    if n not in num:
        num.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    rsp = str(input("Quer continuar? [S/N]")).upper()
    if rsp in "N":
        break
print(f"A lista completa é: {num}")
print(f"A lista de pares é: {pares}")
print(f"A lista de impares é: {impares}")