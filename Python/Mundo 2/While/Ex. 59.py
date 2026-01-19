n = [int(input(f"Digite o {i+1} nnúmero: ")) for i in range(2)]
op = 0
print("""Menu de opções:
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Sair
""")
while op != 5:
    op = int(input("Digite sua opção:"))
    match op:
        case 1:
            print(f"A soma de {n[0]} e {n[1]} é igual a: {n[0]+n[1]}")
        case 2:
            print(f"A subtração de {n[0]} e {n[1]} é igual a: {n[0]-n[1]}")
        case 3:
            print(f"A multiplicação de {n[0]} e {n[1]} é igual a: {n[0]*n[1]}")
        case 4:
            print(f"A divisão de {n[0]} e {n[1]} é igual a: {n[0]/n[1]}")
