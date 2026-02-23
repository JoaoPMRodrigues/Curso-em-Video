from rich import print as printf
from rich.panel import Panel
from rich.align import Align
from rich.traceback import install
install()


class Produto():
    def __init__(self, nome=" ", preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        painel = Panel(conteudo, title=f" Produto ", width=34)
        printf(painel)


celular = Produto("Iphone 17", 6000)
celular.etiqueta()
