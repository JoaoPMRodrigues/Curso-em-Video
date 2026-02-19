from rich import print as printf
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.traceback import install
install()


class produto():
    def __init__(self, nome=" ", preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):

        mensagem = Group(Text(" "*11, end=""), f"{self.nome}",  # Linha 1
                         "-"*30,                               # Linha 2
                         # Linha 3
                         Text("."*10, end=""), Text(f"R${self.preco:.2f}", end=""), Text("."*11, end=""))

        painel = Panel(mensagem, title=f" Produto ", expand=False)
        printf(painel)


celular = produto("Celular", 6000)
celular.etiqueta()
