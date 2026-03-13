a1 = int(input("Digite o primeiro termo da progressão: "))
r = int(input("DIgite a razão da progressão: "))
n = 1
while n <= 10:
    print(a1, end="...")
    a1 += r
    n += 1
print("Fim")
