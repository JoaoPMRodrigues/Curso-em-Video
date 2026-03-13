jogador=dict()
gols=list()
t=g=p=0
cont=1
jogador["nome"]=str(input("Nome do jogador: "))
p=int(input(f"Quants partidas {jogador['nome']} jogou? "))
for i in range(p):
    g=int(input(f"Qauntos gols {jogador["nome"]} fez na {i+1}º partida? "))
    t+=g
    gols.append(g)
jogador["gols"]=gols[:]
jogador["total"]=t
print("-="*30)
print(jogador)
print("-="*30)
print(f"O jogador {jogador["nome"]} jogou {p} partidas.")
for c in gols: 
    print(f"Na {cont}ª partida foram {c} gols.")
    cont+=1
print("-="*30)
print(f"O total de gols foi: {t}")