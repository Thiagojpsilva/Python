# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:

    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        return ((self.x + self.y) > (other.x + other.y))

    def __lt__(self, other):
        return ((self.x + self.y) < (other.x + other.y))

    # def __str__(self) -> str:
    #     return f'({self.x}, {self.y})'

    def __repr__(self):
        class_name = type(self).__name__  # self.__class__.__name__
        return f'{class_name} : (x={self.x!r}, y={self.y!r}),z={self.z!r})'


if __name__ == '__main__':

    p1 = Ponto(5, 1)
    p2 = Ponto(5, 2)

    p3 = p1 + p2
    print(p1)
    print(p2)
    print(p3)
    # print(repr(p1))
    # print(p2)
    print('P1 é Maior que P2',  'Verdadeiro' if (p1 > p2) == True else 'Falso')
    print('P1 é Menor que P2',  'Verdadeiro' if (p1 < p2) == True else 'Falso')
