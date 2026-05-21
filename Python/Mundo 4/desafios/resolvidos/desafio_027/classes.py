from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from random import random


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {dano:.0f}[/]! ")

    def atacar(self, inimigo, forca):
        dado = random()
        dano = forca*dado
        print(
            f"[green]{self.nome}[/]([aqua]{self.vida:.0f}[/]) atacou [red]{inimigo.nome}[/]([blue]{inimigo.vida:.0f}[/]) com um soco de força [blue]{forca:.0f}[/]")
        inimigo.receber_dano(dano)

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = 20
        dado = random()
        vida = cura*dado
        self.vida += vida
        print(
            f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {vida:.0f} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = 50
        dado = random()
        vida = cura*dado
        self.vida += vida
        print(
            f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {vida:.0f} pontos[/] de vida.")
