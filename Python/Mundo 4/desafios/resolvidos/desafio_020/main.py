from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.traceback import install
install()


class jogador():
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nick = nickname
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        self.jogos.sort()
        lista_jogos = "\n".join([f"🎮 {jogo}" for jogo in self.jogos])
        if not lista_jogos:
            lista_jogos = Text(
                f"{self.nick} não tem jogos favoritos", style="red")
        mensagem = Group(f"Nome real: [black on blue]{self.nome}[/]",
                         "Jogos favoritos: ",
                         lista_jogos)

        painel = Panel(
            mensagem, title=f"Jogador(a) <{self.nick}>", expand=False)
        print(painel)


j1 = jogador("João Paulo", "Guibisson_912")
j1.add_favoritos("Clash Royale")
j1.add_favoritos("Minecraft")
j1.add_favoritos("Pokemon")
j1.ficha()
j2 = jogador("Caio", "Caioba")
j2.ficha()
