dados = []
while True:
    nome = (str(input("Nome: ")))
    nota1 = (float(input("Nota 1: ")))
    nota2 = (float(input("Nota 2: ")))
    media = (float((nota1+nota2)/2))
    dados.append([nome, [nota1, nota2], media])
    rsp = str(input("Quer continuar? "))
    if rsp in "Nn":
        break
print("-="*15)
print(f"{"No.":<4}  {"NOME":<10} {"MÉDIA":>13}")
print("_"*30)
for i in range(len(dados)):
    print(f"{i:<4}  {dados[i][0]:<10}     {dados[i][2]:>8.2f}")
print("-"*30)
while True:
    n = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    if n == 999:
        print("Fim!")
        break
    elif n < len(dados):
        print(
            f"As notas de {dados[n][0]} são: {dados[n][1][0]:.2f} e {dados[n][1][1]:.2f}")
    else:
        print("O valor digitado está incorreto. Tente novamente!")
