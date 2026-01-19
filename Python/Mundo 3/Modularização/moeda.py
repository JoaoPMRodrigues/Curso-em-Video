def pulalinha():
    print("-"*30)


def titulo(msg):
    mg = len(msg)+10
    print("-"*mg)
    print(f"     {msg}")
    print("-"*mg)


def aumentar(n, s=False):
    rsp = n*1.1
    if s:
        return f"R${rsp:.2f}"
    return n*rsp


def diminur(n, s=False):
    rsp = n*0.87
    if s:
        return f"R${rsp:.2f}"
    else:
        return rsp


def dobro(n, s=False):
    rsp = 2*n
    if s:
        return f"R${rsp:.2f}"
    else:
        return rsp


def metade(n, s=False):
    rsp = n/2
    if s:
        return f"RS{rsp:.2f}"
    else:
        return rsp


def moeda(n):
    return f"R${n:.2f}"


def resumo(preco, aumento=0, redução=0):
    titulo("Resumo do Valor")
    print(f"Preço analizado: R${preco:.2f}")
    print(f"Dobro do preço: RS{dobro(preco):.2f}")
    print(f"Metade do preço: R${metade(preco):.2f}")
    print(f"{aumento}% de aumento: R${preco*(100+aumento)/100:.2f}")
    print(f"{redução}% de aumento: R${preco*(100-redução)/100:.2f}")


def leiadinheiro(msg):
    while True:
        rsp = str(input(msg)).replace(",",".")

        if rsp.isalpha():
            print(f"\033[0;31mErro! \"{rsp}\" é um preço inválido.\033[m")
        else:
            return float(rsp)
            break