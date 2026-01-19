a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
s = a+b
m = a*b
d = a/b
di = a//b
e = a**b
r = a % b
print(f"A soma vale: {s}, a multiplicação vale: {m}", end=" ")
print(f"A divisão vale: {d:.2f}")
print(f"A divisão inteira vale: {di}, \n A exponenciação vale: {e} \n O resto da divisão vale: {r}")
