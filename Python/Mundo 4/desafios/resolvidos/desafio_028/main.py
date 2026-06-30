from classes import Termostato
from rich import print, inspect


def main():
    termostato = Termostato()
    termostato.temperatura = 17
    inspect(termostato)

    print(f"A sua temperatura é de: {termostato.ftemperatura}")


if __name__ == "__main__":
    main()
