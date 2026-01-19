p = float(input('Qual o preço do produto? '))
fp = int(input("""Qual a forma de pagamento?
[1] à vista ou cheque
[2] à vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartão
Opcao escolhida: """))
if fp == 1:
    print(f'Voce deverá pagar R${(p-p*0.1):.2f},00')
elif fp == 2:
    print(f'Voce deverá pagar R${p-(p*0.05):.2f},00')
elif fp == 3:
    print(f'Voce pagará R${p:.2f},00 e cada parcela ficará em R${p/2},00')
elif fp == 3:
    np = int(input())
    tot = p*1.2
    print(f'Voce pagará R${tot:.2f},00 em {np} parcelas e o valor de cada parcela ficará em R${tot/np},00')
