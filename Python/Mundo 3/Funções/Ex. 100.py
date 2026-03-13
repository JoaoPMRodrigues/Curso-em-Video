from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print("Sorteando 5 valores da lista: ")
    for i in range(5):
        n = randint(0, 100)
        lista.append(n)
        print(f"{n}", end="...", flush=True)
        sleep(0.3)
    print("Pronto!")


def soma(p):
    t = c = 0
    for i in p:
        if i % 2 == 0:
            t += i
            c += 1
    print(
        f"A soma dos valores pares de {p} é {t} e haviam {c} valores pares. ")


sorteia(numeros)
soma(numeros)
