def pulalinha():
    print("-"*30)


def titulo(msg):
    mg = len(msg)+10
    print("-"*mg)
    print(" " * 5, end="")
    print(f"{msg}")
    print("-"*mg)


def moeda(numero):
    return f"R${numero:.2f}"


def aumentar(numero, aumento, boole=False):
    porcentagem = 1 + (aumento/100)
    rsp = numero*(porcentagem)
    if boole:
        return moeda(rsp)
    return rsp


def diminuir(numero, reducao, boole=False):
    porcentagem = 1 - (reducao/100)
    rsp = numero*(porcentagem)
    if boole:
        return moeda(rsp)
    else:
        return rsp


def dobro(numero, boole=False):
    rsp = 2*numero
    if boole:
        return moeda(rsp)
    else:
        return rsp


def metade(numero, boole=False):
    rsp = numero/2
    if boole:
        return moeda(rsp)
    else:
        return rsp


def resumo(preco, aumento=0, reducao=0):
    titulo("Resumo do Valor")
    print(f"Preço analisado: R${preco:.2f}")
    print(f"Dobro do preço: {dobro(preco, True)}")
    print(f"Metade do preço: {metade(preco, True)}")
    print(f"{aumento}% de aumento: {aumentar(preco, aumento, True)}")
    print(f"{reducao}% de aumento: {diminuir(preco, reducao, True)}")
