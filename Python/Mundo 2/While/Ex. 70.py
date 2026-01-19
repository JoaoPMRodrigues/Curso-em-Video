preco = total = contaMaior1000 = 0
menorPreco = float("inf")
produto = nomeMenor = rsp = ""
print("----------------------")
print("==Loja Super Baratão==")
print("----------------------")
while True:
    produto = str(input("Produto: "))
    preco = int(input("Preço: R$"))
    total += preco
    if preco > 1000:
        contaMaior1000 += 1
    if preco < menorPreco:
        nomeMenor = produto
        menorPreco = preco
    rsp = str(input("Quer continuar? [S/N]")).upper()
    if rsp == "N":
        break
print(f"""-------Fim do Programa-------
O total da compra foi: R${total:.2f}
Temos {contaMaior1000} compras que custaram mais de R$100.00
A menor compra foi {nomeMenor} que custou R${menorPreco:.2f}
""")
