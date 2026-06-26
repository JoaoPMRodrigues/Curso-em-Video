from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    salario_minimo = 1612
    inss = 7.5

    def __init__(self, nome):
        self.nome = nome
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        correspondencia = self.salario/Funcionario.salario_minimo

        mensagem = f"O salário de [blue]{self.nome}[/]([purple]{type(self).__name__}[/]) é de "
        mensagem += f"[green]R${self.salario:.2f}[/]\ne corresponde a [yellow]{correspondencia:.1f} salários "
        mensagem += f"mínimos[/]."
        painel = Panel(mensagem, title="Análise de Salário", expand=False)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, hora_trabalhada):
        super().__init__(nome)
        self.hora = valor_hora
        self.trabalho = hora_trabalhada

    def calcular_salario(self):
        self.salario = (self.hora*self.trabalho)*(100-7.5)/100


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salario_bruto*(100-7.5)/100
        return self.salario
