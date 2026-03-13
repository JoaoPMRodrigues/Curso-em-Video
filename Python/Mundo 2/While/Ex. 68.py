from random import randint
vitoria = soma = jogador = computador = 0
escolha = ""
while True:
    escolha = str(input("Você quer impar ou par? "))
    if escolha.lower() == "par":
        jogador = int(input("Digite um número: "))
        computador = int(randint(0, 10))
        soma = jogador+computador
        if soma % 2 == 0:
            vitoria += 1
        else:
            break
    elif escolha.lower() == "impar":
        jogador = int(input("Digite um número: "))
        computador = int(randint(0, 10))
        soma = jogador+computador
        if soma % 2 == 1:
            vitoria += 1
        else:
            break
    else:
        print("Opção inválida. Tente novamente.")
print(f"Você teve {vitoria} vitórias consecutivas.")
