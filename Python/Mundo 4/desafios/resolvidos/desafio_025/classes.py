from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        return f"R$ {self.distancia*Moto.fator:.2f}"


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return "Raio mínimo de 50 km"
        return f"R$ {self.distancia*Caminhao.fator:.2f}"


class Drone(Transporte):
    fator = 0.95

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            return "Raio máximo de 10 km"
        return f"R$ {self.distancia*Drone.fator:.2f}"
