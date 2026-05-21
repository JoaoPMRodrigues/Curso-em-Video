from rich import print
from classes import *


def main():
    p1 = Quadrado(12)

    print(f"Perímetro: {p1.perimetro()}")
    print(f"Área: {p1.area()}")

    p2 = Circulo(12)

    print(f"Comprimento: {p2.perimetro()}")
    print(f"Área: {p2.area()}")


if __name__ == "__main__":
    main()
