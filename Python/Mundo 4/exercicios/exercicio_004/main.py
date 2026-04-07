from rich import inspect
from rich.traceback import install
install()


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a aula.")


class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turme = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez sua matrícula.")


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} acabou de bater ponto.")


aluno1 = Aluno("João", 18, "Ciência da Computação", "25.2")
aluno1.fazer_aniversario()
aluno1.fazer_matricula()

professor1 = Professor("Wallace", 80, "Matematica", "Doutor")
professor1.dar_aula()

funcionario1 = Funcionario("Claudia", 43, "Gerente", "RH")
funcionario1.bater_ponto()

inspect(aluno1, methods=True)
