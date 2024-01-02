from tomlkit import integer


class Pessoa:
    """_summary_
    """

    def __init__(self, nome: str, idade: int) -> None:
        """
        Args:
            nome (str): _description_
            idade (int): _description_
        """
        self.nome = nome
        self.idade = idade

    def pessoa_setter(self):
        """_summary_
        """
    @property
    def nome(self):
        """_summary_
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        """_summary_
        """
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade


class Cliente(Pessoa):
    """_summary_

    Args:
        Pessoa (_type_): _description_
    """
