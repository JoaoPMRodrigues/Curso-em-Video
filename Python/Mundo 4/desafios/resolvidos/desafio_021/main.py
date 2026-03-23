from rich import print
from rich.traceback import install
install()


class caneta():
    def __init__(self, cor):
        match cor.lower():
            case "verde":
                self.cor = "[green]"
            case "azul":
                self.cor = "[blue]"
            case "vermelho":
                self.cor = "[red]"
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def quebra_linha(self, n):
        for _ in range(n):
            print()

    def escrever(self, mensagem):
        if not self.tampada:
            print(f"{self.cor}{mensagem}[/]")
        else:
            print(f":no_entry_sign: A {self.cor}caneta[/] está tampada.")


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
