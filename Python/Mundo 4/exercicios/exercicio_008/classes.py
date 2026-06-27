from rich import print

# Declaração de Classe


class ContaBancaria:
    """
    Essa classe cria a conta bancária de uma pessoa
    Para criar uma nova conta, faça:
    variavel = ContaBancaria(nome,id,saldo)
    """

    def __init__(self, nome, id, saldo=0):
        self._titular = nome
        self.id = id
        self.__saldo = saldo
        print(
            f"[blue]Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}[/]")

    def depositar(self, valor=0):
        valor = abs(valor)
        print(
            f"[green]Depósito de R${valor:,.2f} autorizado na conta {self.id}![/]")
        self.__saldo += valor

    def sacar(self, valor=0):
        valor = abs(valor)
        if valor <= self.__saldo:
            print(
                f"[green]Saque de R${valor:,.2f} autorizado na conta {self.id}.\033[/]")
            self.__saldo -= valor
        else:
            print(f"[red]Saldo insuficiente! Saque recusado.[/]")

    def __str__(self):
        return f"""
O titular da conta é: {self._titular}.
O id de sua conta é: {self.id}.
Seu saldo atual é de: {self.__saldo}
"""
