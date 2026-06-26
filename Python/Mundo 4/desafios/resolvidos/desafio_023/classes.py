from abc import ABC, abstractmethod
from rich import print
from rich.traceback import install
install()


class Poligono(ABC):
    def __init__(self, tamanho):
        self.tamanho = tamanho

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.lados = 4

    def area(self):
        return f"{self.tamanho**2:.2f}"

    def perimetro(self):
        return f"{self.tamanho*self.lados:.2f}"


class Circulo(Poligono):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.lados = 0
        self.pi = 3.14

    def perimetro(self):
        return f"{2*self.pi*self.tamanho:.2f}"

    def area(self):
        return f"{self.pi*self.tamanho*self.tamanho:.2f}"
