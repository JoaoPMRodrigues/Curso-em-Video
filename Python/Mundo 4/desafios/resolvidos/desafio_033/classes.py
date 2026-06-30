from rich import print


class Pessoa:
    ano = 2026

    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento
        self.idade = Pessoa.ano-self._nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        if 1915 <= self.nascimento <= Pessoa.ano:
            self._nascimento = nascimento
            self.idade = Pessoa.ano - self._nascimento
        else:
            raise ValueError(f"\033[31mAno {nascimento} é inválido!\033[0m")

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, idade=0):  # Preciso consertar isso ainda
        raise PermissionError(
            "\033[31mVocê não tem permição de alterar a idade\033[0m")


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ["ADM", "CC", "ENG", "CONT"]
        self._curso = curso

    @property
    def cursos_oficiais(self):
        return self.cursos_oficiais

    @cursos_oficiais.setter
    def add_curso(self, curso):
        if 3 <= len(curso) < 6:
            self.cursos_oficiais.append(curso)
        else:
            print("[red]Curso inválido![/]")

    @property
    def curso(self):
        return self.curso

    @curso.setter
    def curso(self, materia):
        if materia not in self.cursos_oficiais:
            print(f"[red]{materia} não é um curso oficial![/]")
        else:
            self._curso = materia
