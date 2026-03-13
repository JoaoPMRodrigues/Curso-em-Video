km=float(input("Quantos quilometros o carro percorreu? "))
d=int(input("Por quantos dias o carro foi alugado? "))
valor=60*d + 0.15*km
print("Será cobrado um valor de R${:.2f}".format(valor))