from random import randint
tentativas = 0
while not chute == senha:
    senha = (randint(0, 10))
    chute = int(input("Digite seu chute: "))
    tentativas += 1
print(f"Foram necessários {tentativas} tentativas para acertar")
