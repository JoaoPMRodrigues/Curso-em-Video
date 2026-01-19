import moeda

#107
p=moeda.leiadinheiro("Digite o preço: R$")#112
print("Ex.: 107")
print(f"A metade de {p} é: {moeda.metade(p)}")
print(f"O dobro de {p} é: {moeda.dobro(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p)}")
print(f"Reduzindo 13%, temos {moeda.diminur(p)}")
moeda.pulalinha()
#108
print("Ex.: 108")
print(f"A metade de {p} é: {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {p} é: {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p))}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminur(p))}")
moeda.pulalinha()
#109
print("Ex.:109")
print(f"A metade de {p} é: {moeda.metade(p, True)}")
print(f"O dobro de {p} é: {moeda.dobro(p, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, True)}")
print(f"Reduzindo 13%, temos {moeda.diminur(p, True)}")
moeda.pulalinha()
#110
print("ex.:110")
moeda.resumo(p,80,35)