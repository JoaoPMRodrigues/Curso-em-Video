from math import sqrt
co=int(input("Digite o valor do cateto oposto: "))
ca=int(input("Digite o valor do cateto adjacente: "))
hip=sqrt(co**2+ca**2)
print(f"O valor da hipotenusa é: {hip:.2f}")