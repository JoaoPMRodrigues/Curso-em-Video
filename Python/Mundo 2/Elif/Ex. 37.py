n = int(input("Digite um numero inteiro: "))
print('''Suas bases de conversão
[1] Converte para binário      
[2] Converte para octal      
[3] Converte para hexa decimal ''')
op = int(input("Sua opção: "))

if op == 1:
    print(f"{n} convertido para binário é: {bin(n)}")
elif op == 2:
    print(f"{n} convertido para octal é: {oct(n)}")
elif op == 3:
    print(f"{n} convertido para hexadecimal é: {hex(n)}")
else:
    print("Opção inválida! Tente novamente.")
