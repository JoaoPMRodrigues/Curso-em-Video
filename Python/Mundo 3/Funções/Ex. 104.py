def pulalinha():
    print("-" * 30)


def leiaint(n):
    while True:
        if n.isnumeric() and n==int(n):
            print(f"Você digitou o número {n}. ")
            break
        else:
            print("ERRO! Digite um número inteiro válido")
        pulalinha()
        n = input("Digite outro número: ")

leiaint(input("Digite um número: "))
