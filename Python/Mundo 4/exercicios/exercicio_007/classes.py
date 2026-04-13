from rich import inspect, print
from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a aula.")

    def estudar(self):
        print(f"[red]{self.nome}[/] está concluindo o doutorado.")


class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turme = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez sua matrícula.")

    def estudar(self):
        print(f"[red]{self.nome}[/] está no 2º período de CComp")


class Funcionario(Pessoa):
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"O funcionário {self.nome} acabou de bater ponto.")

    def estudar(self):
        print(f"[red]{self.nome}[/] está fazendo pós graduação da PUC.")
