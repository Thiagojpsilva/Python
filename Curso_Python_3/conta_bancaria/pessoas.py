import contas


class Pessoa:
    """_summary_
    """

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        """_summary_

        Args:
            idade (int): _description_
        """
        self._idade = idade

    def __repr__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    """_summary_

    Args:
        Pessoa (_type_): _description_
    """

    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    #    p1 = Pessoa('Thiago', 37)
    #    print(p1.nome, p1.idade)
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)

    c2 = Cliente('Jose', 20)
    c2.conta = contas.ContaPoupanca(333, 444)
    print(c2)
    print(c2.conta)
