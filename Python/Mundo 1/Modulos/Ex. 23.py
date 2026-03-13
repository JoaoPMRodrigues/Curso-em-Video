n = int(input("Digite um numero: "))
u = n % 10
d = n % 100//10
c = n % 1000//100
m = n//1000
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
