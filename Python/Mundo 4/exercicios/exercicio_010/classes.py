from rich import print


class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Criando atributo validável
    @property
    def nota(self):  # getter
        return self._nota

    @nota.setter
    def nota(self, nota):  # setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("[red]Nota inválida![/]")

    @nota.deleter
    def nota(self):
        # Você pode criar uma validação na hora de excluir o atributo
        pass
