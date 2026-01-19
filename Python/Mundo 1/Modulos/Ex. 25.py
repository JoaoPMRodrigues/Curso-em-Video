nome=input(("Digite seu nome: "))
nome=nome.split()
silva = False
fim=len(nome)

for i in range(fim):
    if nome[i].upper() == "SILVA":
        silva= True

if silva==True:
    print("Há Silva no nome.")
else:
    print("Não há Silva no nome.")