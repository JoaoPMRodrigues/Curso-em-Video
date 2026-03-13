n = int(input("Digite um numero: "))
total_div = 0
for i in range(1, n+1):
    if n % i == 0:
        total_div += 1
if total_div == 2:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")
