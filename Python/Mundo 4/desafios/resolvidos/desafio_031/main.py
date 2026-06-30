from classes import Retangulo
from rich import print, inspect


def main():
    ret = Retangulo(9, 9)
    ret.base = 14
    ret.altura = 10
    inspect(ret, private=True, methods=True)
    ret.medidas = (5, 4)
    print(ret.medidas)


if __name__ == "__main__":
    main()
