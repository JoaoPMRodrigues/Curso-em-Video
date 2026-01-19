def pulalinha():
    print("-"*30)


def area(c, l):
    a = c*l
    print(f"A área de um terreno {c:.2f} x {l:.2f} é de {a:.2f}m².")


while True:
    print(" Controle de terrenos")
    pulalinha()
    area(float(input("Comprimento (m): ")), float(input("Largura (m): ")))
    while True:
        rsp = str(input("Quer calcular outro terreno? [S/N]")).upper()
        if rsp in "SN":
            break
        else:
            print("Erro! Digite S ou N")
    if rsp in "N":
        break
