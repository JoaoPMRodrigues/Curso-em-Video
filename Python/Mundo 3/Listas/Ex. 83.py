exp = str(input("Digite sua expressão: "))
c = 0
for i in range(len(exp)):
    if exp[i] == "(":
        c+=1
    elif exp[i] == ")":
        if c > 0:
            c -= 1
        else:
            c -= 1
            break
if c == 0:
    print("A expressão é válida.")
else:
    print("A expressão não é válida.")
