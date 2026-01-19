ano = int(input("Informe o seu ano de nascimento: "))
idade = abs(2025-ano)

if idade == 18:
    print("Já é hora de se alistar.")
elif idade < 18:
    print(f"Ainda falta(m) {abs(idade-18)} ano(s) para você se alistar.")
else:
    print(f"Você deveria ter se alistado a {abs(idade-18)} ano(s).")
