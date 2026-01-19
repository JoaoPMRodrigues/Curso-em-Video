a1 = int(input("Digite o primeiro termo da pa: "))
r = int(input("Digite sua razão: "))
spa = 0
for i in range(10):
    print(a1, end="...")
    spa += a1
    a1 += r

print(f"A soma dos n primeiros termos da pa é: {spa}")
