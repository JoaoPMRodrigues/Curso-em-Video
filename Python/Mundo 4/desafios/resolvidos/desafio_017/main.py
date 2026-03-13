from rich import print as printf
from rich.text import Text
from rich.align import Align
from rich.console import Group
from rich.panel import Panel
from rich.traceback import install
install()


class Produto():
    def __init__(self, nome=" ", preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        nome = Text(f"{self.nome}")
        nome = Align.center(nome)
        linha = Text("-"*30)
        preco_formatado = f"R${self.preco:,.2f}"
        preco = Text(preco_formatado)
        preco = Align.center(preco)
        conteudo = Group(nome, linha, preco)
        mensagem = Panel(conteudo, title='Produto', width=34)
        printf(mensagem)


celular = Produto("Iphone 17", 6000)
celular.etiqueta()
