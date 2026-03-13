from math import factorial
n = int(input("Digite um valor: "))
# fat = factorial(n)
fat = 1
c = n
while c > 1:
    fat *= c
    c -= 1
print(f"{n} fatorial ({n}!) é igual a: {fat}")
