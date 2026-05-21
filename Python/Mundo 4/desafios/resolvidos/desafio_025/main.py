from rich import print
from classes import *
from rich.traceback import install
from rich.table import Table
install()


def main():
    distancia = 8
    moto = Moto(distancia)
    caminhao = Caminhao(distancia)
    drone = Drone(distancia)

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância", justify="center")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Frete", justify="center")

    tabela.add_row(f"{distancia} Km", f"{type(moto).__name__}",
                   f"{moto.calcular_frete()}")

    tabela.add_row(f"{distancia} Km", f"{type(caminhao).__name__}",
                   f"{caminhao.calcular_frete()}")

    tabela.add_row(f"{distancia} Km", f"{type(drone).__name__}",
                   f"{drone.calcular_frete()}")

    print(tabela)


if __name__ == "__main__":
    main()
