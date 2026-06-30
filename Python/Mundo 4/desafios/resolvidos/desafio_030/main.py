from classes import Diario
from rich import inspect


def main():
    d = Diario("rayan")
    d.escrever("Oi")
    d.escrever("Boa noite")
    d.escrever("Será que vai ter gol do Rayan hoje")

    inspect(d, private=True, methods=True)
    d.ler("rayan")


if __name__ == "__main__":
    main()
