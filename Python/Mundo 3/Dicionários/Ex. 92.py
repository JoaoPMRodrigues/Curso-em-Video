carteira = dict()
carteira["nome"] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
carteira["idade"] = (2025 - nascimento)
carteira["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))
if carteira["ctps"]==0:
    print("-="*30)
    for c,k in carteira.items():
        print(f"{c}: {k}")
else:
    carteira["contrato"]=str(input("Ano de contratação: "))
    carteira["salario"]=float(input("Salário: "))
    aux=int(carteira["contrato"])
    ano_aposenta=aux+25
    carteira["aposentado"]=ano_aposenta-nascimento
print("-="*30)
for c,k in carteira.items():
    print(f"{c}: {k}")