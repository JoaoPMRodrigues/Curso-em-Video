l1 = int(input("Digite o valor do lado 1: "))
l2 = int(input("Digite o valor do lado 2: "))
l3 = int(input("Digite o valor do lado 3: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        print("Existe triângulo e ele é equilátero.")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("Existe triângulo e ele é isóceles.")
    else:
        print("Existe triângulo e ele é escaleno.")
else:
    print("Não é possível formar triângulo.")
