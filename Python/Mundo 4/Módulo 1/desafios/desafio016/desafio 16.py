from rich import print as printf, inspect
from rich.table import Table
from rich.traceback import install
install()


class Funcionario():
    """
    Cria um funcionário da empresa Curso em Vídeo
    Para criar um funcionário, faça:
    f1 = Funcionario(nome,setor,cargo)
    """

    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}."

    def __getstate__(self):
        tabela = Table(title="Funcionário")
        tabela.add_column("[bold]Nome[/]", justify="center", style="Blue")
        tabela.add_column("[bold]Cargo[/]", justify="center", style="Blue")
        tabela.add_column("[bold]Setor[/]", justify="center", style="Blue")
        tabela.add_column("[bold]Empresa[/]", justify="center", style="Blue")

        tabela.add_row(self.nome, self.cargo,
                       self.setor, self.empresa)


func1 = Funcionario("Manu", "Marketing", "Gerente")
func1.empresa = "Hostnet"
printf(func1.apresentacao())

func2 = Funcionario("João", "TI", "Programador")
printf(func2.apresentacao())

inspect(Funcionario)
inspect(func1)
inspect(func2)
