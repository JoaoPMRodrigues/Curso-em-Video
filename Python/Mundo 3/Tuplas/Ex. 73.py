tabela = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Mirassol', 'Botafogo', 'Bahia', 'São Paulo', 'Bragantino', 'Corinthians', 'Fluminense',
          'Ceará', 'Internacional', 'Atlético Mineiro', 'Grêmio', 'Vasco', 'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')
print("Os 5 primeiros colocados são: ", end="")
for i in range(0, 6):
    print(F"{tabela[i]}, ", end="")
print("")
print("\n Os 5 ultimos são: ", end="")
for i in range(15, 20):
    print(f"{tabela[i]}, ", end="")
print("")
print("O Corinthians está na posição: ", tabela.index("Corinthians")+1)
print("")
print("Tabela do Brasileirão 2025 em ordem alfabética")
tabelaA=sorted(tabela)
for i in range(20):
    print(f"{i+1} {tabelaA[i]}")