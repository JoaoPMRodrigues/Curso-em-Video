num=[]
rsp=""

while True:
    num.append(int(input("Digite um valor: ")))
    rsp=str(input("Quer continuar? [S/N] ")).upper()
    if rsp in "N":
        break
num.sort(reverse=True)
print(f"A lista tem {len(num)} elementos.")
print(num)
if 5 in num:
    print(f"O 5 está na lista, na posição: {num.index(5)}")
else:
    print("O numero 5 não está na lista.")