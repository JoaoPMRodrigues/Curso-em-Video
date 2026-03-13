ano = int(input("Digite um ano: "))

if ano % 2 == 0 and ano % 4 != 0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
