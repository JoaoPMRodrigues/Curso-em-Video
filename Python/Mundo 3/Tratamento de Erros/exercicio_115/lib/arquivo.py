from lib.interface import cabecalho


def arquivoExiste(arquivo):
    try:
        with open(arquivo, "rt"):
            return True
    except FileNotFoundError:
        return False


def criaArquivo(nome):
    try:
        with open(nome, "wt+"):
            print(f"Arquivo \033[32m{nome}\033[m criado com sucesso.")
    except:
        print("Houve um erro na criação do arquivo")


def lerArquivo(arquivo):
    try:
        with open(arquivo, "rt") as a:
            cabecalho("PESSOAS CADASTRADAS")
            for item in a:
                nome, idade = item.split(";")
                idade = idade.replace("\n", "")
                print(f"{nome:<20} {idade:>3} anos")
            print()
    except:
        print("\033[31mErro ao ler o arquivo\033[m")


def cadastrar(arquivo, nome="Desconhecido", idade=0):
    try:
        with open(arquivo, "at") as a:
            a.write(f"{nome};{idade}\n")
        print(f"\033[32mNovo registro de {nome} adicionado!\033[m")
    except:
        print("\033[31mHouve um erro na hora de escrever no arquivo!\033[m")
