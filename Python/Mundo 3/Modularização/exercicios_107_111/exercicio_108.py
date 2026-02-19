from utilidades import moeda
from utilidades import dado

p = dado.leiadinheiro("Digite o preço: R$ ")
print(f"A metade de {p} é: {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {p} é: {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}")
