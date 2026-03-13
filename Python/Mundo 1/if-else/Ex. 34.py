sal = int(input("Digite o seu salário: "))

if sal <= 1250:
    sal *= 1.15
    print(f"Seu novo salário será de: R${sal:.2f}")
else:
    sal *= 1.1
    print(f"Seu novo salário será de: R${sal:.2f}")
