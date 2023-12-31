# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe: ', self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Thiago', 'Johnatas')
a1 = Aluno('Katarina', 'Guilherme')


print(f'Cliente: {c1.nome} {c1.sobrenome}')
c1.falar_nome_classe()


print(f'Aluno: {a1.nome} {a1.sobrenome}')
a1.falar_nome_classe()

help(Cliente)
