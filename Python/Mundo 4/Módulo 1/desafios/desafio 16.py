from rich import print as printf, inspect
from rich.table import Table
from rich.traceback import install
install()


class funcionario():
    def __init__(self, nome, setor, cargo, empresa="Curso em Vídeo"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        printf(
            f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}.")

    def __getstate__(self):
        tabela = Table(title="Funcionário")
        tabela.add_column("[bold]Nome[/]", justify="center", style="Blue")
        tabela.add_column("[bold]Cargo[/]", justify="center", style="Blue")
        tabela.add_column("[bold]Setor[/]", justify="center", style="Blue")
        tabela.add_column("[bold]Empresa[/]", justify="center", style="Blue")

        tabela.add_row(self.nome, self.cargo, self.setor, self.empresa)


func1 = funcionario("Manu", "Marketing", "Gerente", "SODIÊ")
func1.apresentacao()
inspect(func1)
