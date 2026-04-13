from rich import inspect
from classes import *

aluno1 = Aluno("João", 18, "Ciência da Computação", "25.2")
aluno1.fazer_aniversario()
aluno1.fazer_matricula()
aluno1.estudar()

professor1 = Professor("Wallace", 80, "Matematica", "Doutor")
professor1.dar_aula()
professor1.estudar()

funcionario1 = Funcionario("Claudia", 43, "Gerente", "RH")
funcionario1.bater_ponto()
funcionario1.estudar()

inspect(aluno1, methods=True)
