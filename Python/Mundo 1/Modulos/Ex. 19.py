from random import choice
nomes = []
for i in range(4):
    nomes.append(input("Digite o nome do {}º aluno.".format(i+1)))
escolha = choice(nomes)
print(f"O aluno escolhido será o: {escolha}")
