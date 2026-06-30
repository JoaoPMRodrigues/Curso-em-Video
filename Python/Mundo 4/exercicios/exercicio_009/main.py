from classes import Avaliacao
from rich import inspect


def main():
    av1 = Avaliacao("João", "Matemática", 8)

    av1.set_nota(11)
    inspect(av1, private=True)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}")


if __name__ == "__main__":
    main()
