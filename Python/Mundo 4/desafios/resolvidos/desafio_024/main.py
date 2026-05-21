from rich import print
from classes import *
from rich.traceback import install
install()


def main():
    cafe = Cafe()
    cafe.preparar()
    print()
    cha = Cha()
    cha.preparar()
    print()
    leite = Leite()
    leite.preparar()


if __name__ == "__main__":
    main()
