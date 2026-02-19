# Declaração de Classe
class gafanhoto:
    def __init__(self):  # Método Construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

        # Métodos de instância

    def aniversário(self):
        self.idade += 1
        return self.idade

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!"


# Declaração de Objetos

# Gafanhoto 1
g1 = gafanhoto()
g1.nome = "João"
g1.idade = 18
g1.aniversário()
# Gafanhoto 2
g2 = gafanhoto()
g2.nome = "Pedro"
g2.idade = 112
# Gafanhoto 3
g3 = gafanhoto()
g3.idade = 12
# Imprimindo
print(g1.mensagem())
print(g2.nome)
print(g3.idade)
print(g3.aniversário())
