from classes import ContaBancaria
from rich.traceback import install
install()
# Declaração de Objeto


def main():
    c1 = ContaBancaria("João", 2611, 1000)
    c1.depositar(1000)
    c1._saldo = 0
    c1.titular = "Pedro"
    # Imprimindo
    print(c1)
    print(c1.__getstate__())


if __name__ == "__main__":
    main()
