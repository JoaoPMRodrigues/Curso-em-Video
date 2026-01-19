c = idade = n_maior = n_homem = n_mulher = 0
sexo = rsp = ""
while not rsp == "N":
    rsp = sexo = ""
    print("----------------------")
    print("Cadastre uma pessoa: ")
    print("----------------------")
    idade = int(input("Idade: "))
    while not sexo in ["M", "F"]:
        sexo = str(input("Sexo: [M/F]").upper())
    print("----------------------")
    c += 1
    if idade >= 18:
        n_maior += 1
    if sexo == "M":
        n_homem += 1
    if sexo == "F" and idade < 20:
        n_mulher += 1
    while not rsp in ["S", "N"]:
        rsp = str(input("Quer continuar? [S/N]").upper())

print(f"""====Fim do Programa====
Total de pessoas com mais de 18 anos: {n_maior}
Ao todo temos {n_homem} homens cadastrados
E temos {n_mulher} mulher(es) com menos de 20 anos
""")
