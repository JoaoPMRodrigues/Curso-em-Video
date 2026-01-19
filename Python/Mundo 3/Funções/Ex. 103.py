def ficha(nome="Desconhecido", gols=0):
    print(f"O jogador {nome} fez {gols} gols.")

#Programa Principal
while True: 
    n=str(input("Nome do jogador: "))
    g=str(input("Gols: "))

    if g.isnumeric():
        g=int(g)
    else:
        g=0
    if n.strip()=="":
        ficha(gols=g)
    else:
        ficha(n,g)
    while True:
        rsp=str(input("Quer continuar? [S/N] ")).upper().split()[0]
        if rsp in "SN":
            break
        else:
            print("Erro! Responda somente S ou N")
    if rsp in "N":
        break