dados=dict()

dados["nome"]=str(input("Aluno: "))
dados["media"]=float(input(f"Média de: {dados["nome"]}"))

if dados["media"]>=6:
    dados["situação"]="Aprovado"
elif 6>dados["media"]>4:
    dados["situação"]="Recuperação"
else:
    dados["situação"]="Reprovado"
for c in dados.values():
    print(c)