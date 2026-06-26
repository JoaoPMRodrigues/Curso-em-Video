from rich import print, inspect
from classes import *
from rich.traceback import install
from rich.table import Table
install()


def main():
    distancia = 20

    viagem = [Moto(distancia), Caminhao(distancia), Drone(distancia)]

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância", justify="center")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Frete", justify="center")

    for veiculo in viagem:
        tabela.add_row(f"{distancia} Km", f"{type(veiculo).__name__}",
                       f"{veiculo.calcular_frete()}")

    print(tabela)


if __name__ == "__main__":
    main()
