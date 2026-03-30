from rich import print
from rich.traceback import install
from time import sleep
install()


class livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.posicao = 1

        print(
            f""":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.paginas} páginas[/] no total. Você está na [yellow]{self.posicao} página[/][/blue]""")

    def fim_do_livro(self):
        return True if self.paginas == self.posicao else False

    def avancar_paginas(self, n):
        numero_avanco = 0

        while not self.fim_do_livro() and numero_avanco < n:
            numero_avanco += 1
            self.posicao += 1
            print(f"Pag{self.posicao} :arrow_forward:", end=" ")
            sleep(0.3)

        print(
            f"[purple]Você avançou {numero_avanco} páginas e está na[/] [yellow]página {self.posicao}[/]")

        if self.fim_do_livro():
            print(
                f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")


l1 = livro("Grokking Algorithms", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
