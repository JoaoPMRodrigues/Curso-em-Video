n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
if m >= 7:
    print("Aprovado.")
elif m < 5:
    print("Reprovado.")
else:
    print("Recuperação.")
