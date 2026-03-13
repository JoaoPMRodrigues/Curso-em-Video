# Declaração de Classe
class ContaBancaria:
    """
    Essa classe cria a conta bancária de uma pessoa
    Para criar uma nova conta, faça:
    variavel = ContaBancaria(nome,id,saldo)
    """

    def __init__(self, nome, id, saldo=0):
        self.titular = nome
        self.id = id
        self.saldo = saldo

    def depositar(self, valor=0):
        print(
            f"\033[32mDepósito de R${valor:,.2f} autorizado na conta {self.id}!\033[0m")
        self.saldo += valor

    def sacar(self, valor=0):
        if valor <= self.saldo:
            print(
                f"\033[32mSaque de R${valor:,.2f} autorizado na conta {self.id}.\033[0m")
            self.saldo -= valor
        else:
            print(f"\033[31mSaldo insuficiente! Saque recusado.\033[0m")

    def __str__(self):
        return f"""
O titular da conta é: {self.titular}.
O id de sua conta é: {self.id}.
Seu saldo atual é de: {self.saldo}
"""

    def __getstate__(self):
        return f"Status: Titular = {self.titular} ; id = {self.id} ; saldo = R${self.saldo:.2f}"


# Declaração de Objeto


conta1 = ContaBancaria("João", 2611, 100)
conta1.depositar(100)
conta1.sacar(500)

# Imprimindo
print(conta1)
print(conta1.__getstate__())
