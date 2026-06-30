from rich import print


class Termostato:
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura
        self.ftemperatura = f"{temperatura}{chr(176)}C"

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if float(temperatura*2) != int(temperatura*2):
            raise ValueError(
                f"\033[31mTemperatura de {temperatura}{chr(176)}C inválida!\033[0m")

        if 16 <= temperatura <= 24:
            self.__temperatura = temperatura
            self.ftemperatura = f"{temperatura}{chr(176)}C"
            return
        print("[red]Valor inválido![/]")
