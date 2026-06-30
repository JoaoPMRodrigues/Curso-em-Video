from rich import print


class Retangulo:
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        self._area = base*altura
        self._medidas = (base, altura)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base < 0:
            raise TypeError("\033[31mValor Inválido para base!\033[0m")
        self._base = base
        self._area = self._base*self._altura
        self._medidas = (self._base, self._altura)

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura < 0:
            raise TypeError("\033[31mValor Inválido para altura!\033[0m")

        self._altura = altura
        self._area = self._base*self._altura
        self._medidas = (self._base, self._altura)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self):
        raise TypeError(
            "\033[31mNão é possível mexer na área isoladamente!\033[0m")

    @property
    def medidas(self):
        return f"Base = {self._base}\nAltura = {self._altura}\nÁrea = {self._area}"

    @medidas.setter
    def medidas(self, med=(0, 0)):
        self.base = med[0]
        self.altura = med[1]
