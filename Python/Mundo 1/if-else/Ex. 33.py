n = input("Digite 3 números: ")
a, b, c = n.split()
# vendo o maior
maior = a
if b > a and b >= c:
    maior = b
if c > a and c > b:
    maior = c
# vendo o menor
menor = a
if b < a and b <= c:
    menor = b
if c < a and c < b:
    menor = c

print(maior)
print(menor)
