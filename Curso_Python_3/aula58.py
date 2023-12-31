# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

# from functools import partial


class Foo:

    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'IssO é protegido'
        self.__privete = 'valor privado'

    def metodo_publico(self):
        return 'metodo_publico'

    @property
    def _metodo_proteced(self):
        return '_metodo_protected'


f = Foo()
print(f.public)
print(f.metodo_publico())
# Por convenção não deve ser usado _(Protected) e __(Private) fora da classe
print(f._protected)
# Por convenção não deve ser usado _(Protected) e __(Private) fora da classe
print(f._metodo_proteced)
# So deve ser usado entro da classe fora da classe está errado.
# print(f._Foo__privete)
