total = n50 = n20 = n10 = n1 = rest0 = 0
while True:
    total = float(input("Quanto você quer sacar? "))
    if total//1==total:
        break
    else:
        print("Não trabalhamos com centavos. Tente outro valor")
        total= float(input("Quanto você quer sacar? "))

while True:
    n50 = total//50
    resto = total % 50
    n20 = resto//20
    resto = resto % 20
    n10 = resto//10
    resto = resto % 10
    n1 = resto //1 
    resto = resto%1
    if resto == 0:
        break
print(f"""Valor Sacado
R$50:{n50} notas
R$20:{n20} notas
R$10:{n10} notas
R$1:{n1} moedas""")
