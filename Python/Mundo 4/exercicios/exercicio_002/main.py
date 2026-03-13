# Declaração de Classe
class gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nove pessoa, use:
    variavel = gafanhoto(nome,idade)
    """

    def __init__(self, nome="Vazio", idade=0):  # Método Construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

        # Métodos de instância

    def aniversario(self):
        self.idade += 1
        return self.idade

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!"

    def __str__(self):  # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
# Declaração de Objetos


# Gafanhoto 1
g1 = gafanhoto("João", 18)

g1.aniversario()
# Gafanhoto 2
g2 = gafanhoto("Pedro", 112)

# Gafanhoto 3
g3 = gafanhoto(idade=12)

# Gafanhoto 4
g4 = gafanhoto()

# Imprimindo atributos

print(g1.mensagem())
print(g2.nome)
print(g3.aniversario())
print(g4.mensagem())

print()
print("-" * 30)

# Impriminto dunders


print(g1.__doc__)
print(g1)
print(g4)
print(g1.__dict__)  # Sempre imprime a mesma coisa
print(g1.__getstate__())  # Pode ser mudado na classe
print(g3.__class__)
