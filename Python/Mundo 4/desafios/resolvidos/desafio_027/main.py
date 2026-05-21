from classes import *
from rich.traceback import install
install()


def main():
    p1 = Guerreiro("Kratos", 2000)
    p2 = Mago("Merlin", 1500)

    p1.atacar(p2, 1000)
    p2.curar()
    p2.atacar(p1, 2000)
    p1.curar()


if __name__ == "__main__":
    main()
