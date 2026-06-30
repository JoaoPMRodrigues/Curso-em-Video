from classes import Aluno
from rich import inspect


def main():
    a1 = Aluno("João", 2007, "CC")
    inspect(a1)


if __name__ == "__main__":
    main()
