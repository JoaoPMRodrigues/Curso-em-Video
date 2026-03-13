def escreva(a):
    print("~"*(len(a)+4))
    print(f"  {a}")
    print("~"*(len(a)+4))

while True:
    escreva(str(input()))
    while True:
        rsp=str(input("Quer continuar? [[S/N]] ")).upper()
        if rsp in "SN":
            break
    if rsp in "N":
        break