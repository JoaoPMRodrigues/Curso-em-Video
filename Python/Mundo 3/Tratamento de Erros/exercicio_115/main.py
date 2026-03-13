from lib.interface import menu, cabecalho, leiaint
from lib.arquivo import arquivoExiste, criaArquivo, lerArquivo, cadastrar
from time import sleep

arquivo = "data/dados.txt"

if not arquivoExiste(arquivo):
    criaArquivo(arquivo)

while True:

    opcao = menu(["Ver pessoas cadastradas",
                  "Cadastras nova pessoa", "Sair do sistema"])
    if opcao == 1:
        lerArquivo(arquivo)
    elif opcao == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arquivo, nome, idade)
    elif opcao == 3:
        print("Saindo do sistema... Até logo!")
        break
    elif opcao == -1:
        break   # Caso de KeyboardInterrupt
    else:
        print("\033[031mErro! Digite uma opção válida.\033[m")
    sleep(0.5)
