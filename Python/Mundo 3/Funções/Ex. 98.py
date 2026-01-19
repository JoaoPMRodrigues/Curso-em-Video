from time import sleep


def pulalinha():
    """
    -> Pulalinha é capaz de pular uma linha e separar oq está em cima do que está em baixo
    """
    print()
    print("-="*30)


def conta(i, f, p):
    """
    ->Conta é capaz de contar de um número inteiro a outro seguindo 
    um passo, com todos os parâmetros definidos pelo usuário
    i=Inicio da contagem
    f=Fim da contagem
    p=Passo da contagem
    """
    for c in range(i, f, p):
        sleep(0.5)
        print(c, end=" ", flush=True)
    print("FIM!")


def contador(i, f, p):
    """
    Aplica a função conta para todas as diferentes combinações
    de início, fim e passo
    """
    pulalinha()
    print(f"Contagem de {i} a {f} de {p} em {p}")
    if (i < f and p > 0):
        conta(i, f+1, p)
    elif (i > f and p < 0):
        conta(i, f-1, p)
    elif (i > f and p > 0):
        p *= -1
        conta(i, f-1, p)
    elif (i < f and p < 0):
        p *= -1
        conta(i, f+1, p)
    elif p == 0:
        if i < f:
            p = 1
            conta(i, f+1, p)
        elif i > f:
            p = -1
            conta(i, f-1, p)
    else:
        print("Mds, oq foi que vc fez?????")

help(contador)
contador(1, 10, 1)
contador(10, 1, -2)
pulalinha()
print("Agora é sua vez de personalizar a contagem! ")
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))
