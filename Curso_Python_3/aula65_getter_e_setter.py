class Pessoa:
    """_summary_
    """

    def __init__(self, nome, idade):
        self._name = nome
        self._idade = idade

    @property
    def nome(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._name

    @property
    def idade(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._idade

    # @nome.setter
    # def nome(self, novo_name):
    #     self._name = novo_name

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            print("A idade deve ser um número positivo.")


# Criando uma instância da classe Pessoa
pessoa = Pessoa("João", 30)

# Usando o getter implicitamente
print(pessoa.nome)  # Saída: João

# Usando o setter implicitamente
pessoa.idade = 35
print(pessoa.idade)  # Saída: 35

# pessoa.nome = 'Thiago'
# print(pessoa.nome)  # Saída: João

# Tentando definir uma idade negativa (o setter não permite)
pessoa.idade = -5  # Saída: A idade deve ser um número positivo.
