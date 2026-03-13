num = []
rsp = ""
aux = 0
verifica = False
while True:
    verifica = False
    aux = int(input("Digite um valor: "))
    if aux in num:
        print("Este valor já foi cadastrado. Tente novamente.")
    else:
        num.append(aux)
        print("Valor adcionado.")
    rsp = str(input("Você quer continuar? [S/N]")).upper()
    if rsp in "N":
        break
num.sort()
print(num)