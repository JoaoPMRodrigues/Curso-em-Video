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

    def desligado(self):
        return ":no_entry_sign: [red]A TV está desligada[/]"

    def mensagem_erro(self):
        self.erro = False
        return " :no_entry_sign: [red]Comando errado![/]"

    def mensagem(self):
        mensagem = "CANAL = "
        for i in range(self.canal_min, self.canal_max+1):
            if self.canal == i+1:
                mensagem += f"[on yellow]{i}[/] "
            else:
                mensagem += f"{i+1} "
        blocos = "[white on green] [/]"*self.volume
        blocos += "[white on red] [/]"*(self.volume_max-self.volume)

        mensagem += f"\nVOLUME = {blocos}"
        return mensagem

    def tela(self):
        if not self.ligado:
            msg = self.desligado()
        elif self.erro:
            msg = self.mensagem_erro()
        else:
            msg = self.mensagem()
        painel = Panel(msg, title="[ TV ]", expand=False)

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
