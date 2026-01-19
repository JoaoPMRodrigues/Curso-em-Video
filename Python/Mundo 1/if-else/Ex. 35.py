l = [int(input("Digite o lado {}: ".format(i+1))) for i in range(3)]

if l[1]+l[2] > l[0] and l[0] + l[1] > l[2] and l[0] + l[2] > l[1]:
    print("É possível formar um triângulo")
else:
    print("Não é possível formar um triângulo.")
