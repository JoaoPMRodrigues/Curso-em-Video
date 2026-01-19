dados = (str(input("Nome: ")), int(input("Preço: ")), str(input("Nome: ")), int(input("Preço: ")),  str(input("Nome: ")), int(input("Preço: ")),
         str(input("Nome: ")), int(input("Preço: ")),  str(input("Nome: ")), int(input("Preço: ")),  str(input("Nome: ")), int(input("Preço: ")), )
print("-" * 20)
print("Listagem de Preços")
for i in range(0, len(dados)-1, 2):
    print("-"*20)
    print(f"Produto: {dados[i]}")
    print(f"Preço: R${dados[i+1]:.2f}")
print("-" * 20)
