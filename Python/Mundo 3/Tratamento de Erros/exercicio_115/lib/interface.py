def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Digite um numero inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return -1
        else:
            return n


def linha(tamanho=42):
    return "-"*tamanho


def cabecalho(txt):
    margem = 14
    tamanho = len(txt) + margem
    print(linha(tamanho))
    print(txt.center(tamanho))
    print(linha(tamanho))


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i in range(len(lista)):
        print(f"\033[33m{i+1}\033[m - \033[34m{lista[i]}\033[m")

    opcao = leiaint("Sua opção: ")
    return (opcao)
