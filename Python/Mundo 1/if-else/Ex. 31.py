d = int(input("Digite a distância da viagem: "))

if d <= 200:
    p = d*0.50
    print(f"O preço da viagem será de R${p:.2f}")
else:
    p = d*0.45
    print(f"O preço da viagem será de R${p:.2f}")
