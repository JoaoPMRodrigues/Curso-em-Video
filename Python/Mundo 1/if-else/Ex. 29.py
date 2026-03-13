velocidade = int(input("Digite a velocidade do carro: "))

if velocidade > 80:
    multa = 7*(velocidade-80)
    print(f"Você passou do limite e terá que pagar uma mulda de R${multa:.2f}")
else:
    print("Você estava dentro do limite de velocidade.")
