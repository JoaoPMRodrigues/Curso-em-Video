from rich import print
from rich.traceback import install
from rich.text import Text
from time import sleep
from rich.console import Console
install()


class livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.posicao = 2

    def avancar_paginas(self, n):
        seta = "[bold white]\u27A4[/]"
        numero_avanco = 0
        for _ in range(n):
            if self.posicao <= self.paginas:
                print(f"Pág{self.posicao} {seta}", end=" ")
                numero_avanco += 1
                self.posicao += 1
                sleep(0.5)
            else:
                break
        print(
            f"[purple]Você avançou {numero_avanco} páginas e está na[/] [yellow]página {self.posicao-1}[/]")

        if not self.posicao < self.paginas:
            console = Console()
            console.print(
                f":closed_book: Você chegou ao final do livro '{self.titulo}'", emoji=True, style="red")


l1 = livro("Grokking Algorithms", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
