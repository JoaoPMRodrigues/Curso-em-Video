from rich import print
from rich.console import Console
from rich.traceback import install
install()


class caneta():
    def __init__(self, cor):
        match cor.lower():
            case "verde":
                self.cor = "green"
            case "azul":
                self.cor = "blue"
            case "vermelho":
                self.cor = "red"
        self.destampada = False

    def destampar(self):
        self.destampada = True

    def quebra_linha(self, n):
        for _ in range(n):
            print()

    def escrever(self, mensagem):
        console = Console()
        if self.destampada:
            console.print(mensagem, style=self.cor, end="")
        else:
            console.print(
                f":no_entry_sign: A [{self.cor}]caneta[/] está tampada.", emoji=True)


c1 = caneta("Azul")
c2 = caneta("vermelho")
c3 = caneta("VERDE")

c1.destampar()
c2.destampar()

c1.escrever("Bom dia ")
c2.escrever("Meu povo")
c1.quebra_linha(2)
c3.escrever("Acorda")
c3.quebra_linha(1)
