from random import randint
numeros = (randint(0, 9) for i in range(6))
ordem_numeros = sorted(numeros)
ultimo = len(ordem_numeros)-1
print(f"O maior valor da tupla é: {ordem_numeros[ultimo]}")
print(f"O menor valor da tupla é: {ordem_numeros[0]}")
