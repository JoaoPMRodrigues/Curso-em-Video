from classes import ContaBancaria
from rich import inspect


def main():

    cc = ContaBancaria("João", 123, 5000)
    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()
