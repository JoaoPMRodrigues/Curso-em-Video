from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.traceback import install
install()


class televisao():
    def __init__(self):
        self.ligado = False
        self.volume = 0
        self.canal = 1

    def acao(self, botao):
        if not self.ligado:
            painel = Panel(
                ":no_entry_sign: [red]A TV está desligada[/]", title="[ TV ]", expand=False)
            print(painel)
            print(f" < CH{self.canal} >     - VOL{self.volume} + ")
        else:
            mensagem = Group("Canal = 1 2 3 4 5 ")


tv = televisao()
while True:
    botao = str(input())
    if botao.isalnum():
        if not int(botao):
            break
    tv.acao(botao)
