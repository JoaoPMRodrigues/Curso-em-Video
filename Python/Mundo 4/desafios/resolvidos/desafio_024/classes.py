from abc import ABC, abstractmethod
from rich import print


class BebidaQuente(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def ferver_agua(self):
        return "Fervendo água a 100 graus Celcius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def ferver_agua(self):
        return super().ferver_agua()

    def misturar(self):
        return "Passando água pressurizada pelo po de café moido."

    def servir(self):
        return "Servindo em xícara pequena."

    def preparar(self):
        print("--- [red]Iniciando o Preparo[/] ---")
        print(f"1. {self.ferver_agua()}")
        print(f"2. {self.misturar()}")
        print(f"3. {self.servir()}")
        print("--- Bebida Pronta ---")


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def ferver_agua(self):
        return super().ferver_agua()

    def misturar(self):
        return "Mergulhando o sachê de ervas na água."

    def servir(self):
        return "Servindo na caneca de procelana com limão"

    def preparar(self):
        print("--- [green]Iniciando o Preparo[/] ---")
        print(f"1. {self.ferver_agua()}")
        print(f"2. {self.misturar()}")
        print(f"3. {self.servir()}")
        print("--- Bebida Pronta ---")


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def ferver_agua(self):
        return super().ferver_agua()

    def misturar(self):
        return "Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "Servindo na caneca grande, já com café."

    def preparar(self):
        print("--- [blue]Iniciando o Preparo[/] ---")
        print(f"1. {self.ferver_agua()}")
        print(f"2. {self.misturar()}")
        print(f"3. {self.servir()}")
        print("--- Bebida Pronta ---")
