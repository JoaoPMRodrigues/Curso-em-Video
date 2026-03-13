tabuada = int(input("Qual tabuada você deseja? "))
fim = int(input("Até onde ela vai? "))
for i in range(1, fim+1):
    print(f"{tabuada} x {i} = {tabuada*i}")
