def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Digite um numero inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Digite um numero real válido.\033[m")
            continue
        else:
            return n
