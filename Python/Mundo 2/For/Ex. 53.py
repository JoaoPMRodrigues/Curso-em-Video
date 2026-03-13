frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f"o inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palindromo.")
else:
    print("A frase não é um palindromo.")
