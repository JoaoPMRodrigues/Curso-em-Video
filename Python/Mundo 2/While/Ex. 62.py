a1 = int(input("Digite o primeiro termo da progressão: "))
r = int(input("DIgite a razão da progressão: "))
n = resposta = 1
rsp = 0
inicio = 10
while not resposta == 0:
    inicio += rsp
    while n <= (inicio):
        print(a1, end="...")
        a1 += r
        n += 1
    rsp = resposta = int(input("\nQuer ver mais algum valor? "))
print("Fim")
