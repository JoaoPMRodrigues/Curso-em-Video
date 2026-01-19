c = s = n = 0
maiorv = -float("inf")
menorv = float("inf")
rsp = ""
while not rsp.upper() not in "N":
    n = int(input("Digite um valor: "))
    s += n
    c += 1
    if n > maiorv:
        maiorv = n
    elif n < menorv:
        menorv = n
    rsp = str(input("Deseja continuar? [S/N]"))
media = s/c
print(f"""O maior valor é: {maiorv}
      O menor valor é: {menorv}
      A média dos valores é: {media}""")
