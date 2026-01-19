sal = int(input("Qual o seu salário? "))
casa = int(input("Qual o valor da casa? "))
ano = int(input("Em quantos anos você pretende pagar? "))
pres = casa/(12*ano)

if pres < 0.3*sal:
    print(f"Empréstimo aprovado! As prestações serão de: R${pres:.2f}")
else:
    print("Empréstimo negado! O valor da prestação excede 30% do seu salário.")
