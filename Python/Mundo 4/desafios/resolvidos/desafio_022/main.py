from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.traceback import install
install()


class televisao():
    def __init__(self):
        self.ligado = False
        self.volume = 1
        self.canal = 1

    def acao(self, botao='0'):
        
        if not self.ligado and botao in "@":
            self.ligado=True
        elif self.ligado and botao in "@":
            self.ligado = False
        
        if not self.ligado:
            mensagem = ":no_entry_sign: [red]A TV está desligada[/]"
            painel = Panel(mensagem, title="[ TV ]", expand=False)
            print(painel)
            print(f" < CH{self.canal} >     - VOL{self.volume} + ")
        else:
            if self.volume<5 and botao in "+":
                self.volume+=1
            elif self.volume>1 and botao in "-":
                self.volume-=1
            elif botao in ">":
                self.canal+=1
            elif botao in "<":
                self.canal-=1
            
            if self.canal>5:
                self.canal=1
            elif self.canal<1:
                self.canal=5

            blocos = "[white on green] [/]"*self.volume
            blocos += "[white on red] [/]"*(5-self.volume)
            canal = "CANAL = "
            for i in range(1,6):
                if self.canal == i:
                    canal+=f"[on yellow]{i}[/] "
                else:
                    canal +=f"{i} "
            mensagem = canal
            mensagem+=f"\nVOLUME = {blocos}"
            painel = Panel(mensagem,title="[ TV ]",expand= False)
            print(painel)
            
tv = televisao()
tv.acao()
while True:
    botao = str(input())
    if botao in "#":
        break      
    tv.acao(botao)
