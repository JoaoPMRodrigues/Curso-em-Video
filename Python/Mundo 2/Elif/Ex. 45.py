from random import randint
print('''Vamos jogar pedra, papel, tesoura
[1] Pedra
[2] Papel
[3] Tesoura
''')
jc = int(randint(1, 3))
j1 = int(input("Qual a sua jogada? "))

if jc == j1:
    print("Empate.")
elif (j1 == 1 and jc == 3) or (j1 == 2 and jc == 1) or (j1 == 3 and jc == 2):
    print("Você venceu.")
else:
    print("O computador venceu.")
