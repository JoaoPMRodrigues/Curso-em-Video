time = list()
g = p = 0
cont = 1

# Coletando os dados de cada jogador

while True:
    jogador = dict()    
    jogador["nome"] = str(input("Nome do jogador: "))
    p = int(input(f"Quants partidas {jogador['nome']} jogou? "))
    gols = list()
    t = 0
    for i in range(p):
        g = int(input(f"Qauntos gols {jogador["nome"]} fez na {i+1}º partida? "))
        gols.append(g)
        t += g
    jogador["gols"] = gols[:]
    jogador["total"] = t
    time.append(jogador.copy())

    while True:
        rsp = str(input("Quer continuar? [S/N]")).upper()
        if rsp in "SN":
            break
        else:
            print("Erro! Responda apenas S ou N")
    if rsp in "N":
        break

# Escrevendo os dados fde todos os jogadores

print("-="*30)
print(" cod ", end="")

for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
for k, v in enumerate(time):
    print(f"{(k+1):>4}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
cont = 1

# Escrevendo o número de gols do jogador escolhido pelo usuário

while True:
    n = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if n == 999:
        break
    elif 0 <= n < len(time):
        print(f"--Levantamento do jogador {time[n]["nome"]}: ")
        for i in time[n]["gols"]:
            print(f"   No jogo {cont} fez {time[n]["gols"][cont-1]}")
            cont += 1
        cont = 1
    else:
        print("Tente outro valor.")
