c = n = s = 0
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    s += n
    c += 1
print(f"Você digitou {c} valores e a soma deles é: {s}")
