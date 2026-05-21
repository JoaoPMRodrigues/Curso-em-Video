from rich import print
from classes import *
from rich.traceback import install
install()


def main():
    f1 = Horista("Wallace", 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = Mensalista("CLT padrão", 9500)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
