from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class ControleRemoto():
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self):
        self.ligado = False
        self.erro = False
        self.volume = 1
        self.canal = 1

    def ligar(self):
        self.ligado = not self.ligado

    def passa_canal(self):
        if self.ligado:
            self.canal += 1
            if self.canal > self.canal_max:
                self.canal = self.canal_min

    def volta_canal(self):
        if self.ligado:
            self.canal -= 1
            if self.canal < self.canal_min:
                self.canal = self.canal_max

    def aumenta_volume(self):
        if self.ligado and self.volume < self.volume_max:
            self.volume += 1

    def diminui_volume(self):
        if self.ligado and self.volume > self.volume_min:
            self.volume -= 1

    def alerta(self):
        self.erro = True

    def tela(self):

        if not self.ligado:
            mensagem = ":no_entry_sign: [red]A TV está desligada[/]"
            painel = Panel(mensagem, title="[ TV ]", expand=False)
        elif self.erro:
            mensagem = " :no_entry_sign: [red]Comando errado![/]"
            painel = Panel(mensagem, title="[ TV ]", expand=False)
            self.erro = False
        else:
            canal = "CANAL = "
            for i in range(self.canal_max):
                if self.canal == i+1:
                    canal += f"[on yellow]{i+1}[/] "
                else:
                    canal += f"{i+1} "

            blocos = "[white on green] [/]"*self.volume
            blocos += "[white on red] [/]"*(self.volume_max-self.volume)

            mensagem = canal
            mensagem += f"\nVOLUME = {blocos}"
            painel = Panel(mensagem, title="[ TV ]", expand=False)

        print(painel)


tv = ControleRemoto()

while True:
    tv.tela()
    botao = str(input(f"< CH{tv.canal} > - VOL{tv.volume} + "))

    match botao:
        case "0":
            break
        case "@":
            tv.ligar()
        case ">":
            tv.passa_canal()
        case "<":
            tv.volta_canal()
        case "+":
            tv.aumenta_volume()
        case "-":
            tv.diminui_volume()
        case _:
            tv.alerta()
