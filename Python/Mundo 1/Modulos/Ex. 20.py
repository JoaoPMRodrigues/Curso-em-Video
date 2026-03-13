from random import shuffle
nomes = []
for i in range(4):
    nomes.append(input(f"Digite o nome do {i+1}º aluno: "))
shuffle(nomes)
print("A ordem de apresentação será: ", nomes)
