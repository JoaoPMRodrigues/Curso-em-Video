from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

aluno1 = Aluno("João", 18, "Ciência da Computação", "25.2")
aluno1.fazer_aniversario()
aluno1.fazer_matricula()

professor1 = Professor("Wallace", 80, "Matematica", "Doutor")
professor1.dar_aula()

funcionario1 = Funcionario("Claudia", 43, "Gerente", "RH")
funcionario1.bater_ponto()

inspect(aluno1, methods=True)
