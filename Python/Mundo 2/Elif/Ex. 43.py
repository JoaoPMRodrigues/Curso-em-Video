peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura**2
print(f"Seu imc é: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso. ")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal.")
elif 25 <= imc < 30:
    print("Você está em sobrepeso.")
elif 30 <= imc < 40:
    print("Você está em obesidade")
else:
    print("Você está em obesidade mórbida.")
