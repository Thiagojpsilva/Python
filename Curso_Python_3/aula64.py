# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        return super().upper()


string = MinhaString('Thiago')

print(string.upper())
