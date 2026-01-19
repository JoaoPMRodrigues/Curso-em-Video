n = s = c = 0
while True:
    n = int(input("Digite um numero: "))
    if n != 999:
        s += n
        c += 1
    else:
        break
print(f"Você digitou {c} valores e a soma deles é: {s}")