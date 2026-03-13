from rich import print as printf
from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.traceback import install
install()


class churrasco():
    def __init__(self, evento, convidados):
        self.titulo = evento
        self.convidados = convidados

    def analisar(self):
        consumo = 0.4 * self.convidados  # Consumo padrão = 0.4 Kg por pessoa
        preco = 82.4 * consumo  # preço do quilo da carne em R$ 82,40
        pagamento = preco/self.convidados

        mensagem = Group(
            f"Analisando [green]{self.titulo}[/] com [blue]{self.convidados}[/] convidados",
            "Cada participante comerá 0.4 Kg e cada Kg custa R$82.40 ",
            f"Recomendo comprar [blue]{consumo:.3f}[/] Kg de carne",
            f"O custo total será de [green]R${preco:2f}[/]",
            f"Cada pessoa terá que pagar [yellow]R${pagamento:.2f}[/] para participar.")

        painel = Panel(mensagem, title=self.titulo, expand=False)

        printf(painel)


churras1 = churrasco("Churras de cria", 15)
churras1.analisar()
