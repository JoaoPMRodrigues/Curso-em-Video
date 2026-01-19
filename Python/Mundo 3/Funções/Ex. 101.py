def pulalinha():
    print("-"*30)
def voto(nasc):
    """Calcula a idade da pessoa a partir do ano em que ela nasceu
    e verifica a necessidade de voto nas eleições"""
    idade=2025-nasc
    if idade<16:
        return "NEGADO"
    elif 16<= idade <18:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"
while True:
    pulalinha()
    rsp=int(input("Em que ano você nasceu? "))
    print(f"Voto: {voto(rsp)}")
    while True:
        r=str(input("Quer continuar? [S/N]")).upper().split()[0]
        if r in "SN":
            break
        else:
            print("Erro! Digite só S ou N")
    if r in "N":
        break