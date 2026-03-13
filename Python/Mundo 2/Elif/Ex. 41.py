ano = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano

if idade <= 9:
    print("Sua categoria é: Mirim")
elif idade > 9 and idade <= 14:
    print("Sua categoria é: Infantil")
elif idade > 14 and idade <= 19:
    print("Sua categoria é: Junior")
elif idade == 20:
    print("Sua categoria é: Sênior")
else:
    print("Sua categoria é: Master")
