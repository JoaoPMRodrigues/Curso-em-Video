from random import randint
jogos = list()
n = int(input("Quantos jogos você vai jogar? "))
print(f"-=-=-= Sorteando {n} jogos -=-=-=")
for i in range(n):
    aux = list()
    for j in range(6):
        aux.append(randint(1, 60))
    jogos.append(aux[:])
    jogos[i].sort()
    print(f"Jogo {i+1}: {jogos[i]}")
print("-=-=-=-=-= Boa sorte! -=-=-=-=-=")
