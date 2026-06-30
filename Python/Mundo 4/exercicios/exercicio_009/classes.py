from rich import print


class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Métodos acessores: Getters and Setters
    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("[red]Nota inválida![/]")
            self.set_nota(int(input("Digite a nota correta: ")))

    def get_nota(self):
        return self._nota
