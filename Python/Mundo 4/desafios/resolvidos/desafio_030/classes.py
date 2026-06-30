from rich import print


class Diario:
    def __init__(self, senha="senha"):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, mensagem):
        self.__segredos.append(mensagem)

    def ler(self, senha=""):
        if senha != self.__senha:
            raise PermissionError(
                "\033[31mVocê não tem permissão para ler!\033[0m")
        for segredo in self.__segredos:
            print(f"- {segredo}")
