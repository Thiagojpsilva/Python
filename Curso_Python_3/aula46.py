"""
 Decoradores com paramentros
"""


def decoradora(func):
    """_summary_

    Args:
        func (_type_): _description_

    Returns:
        _type_: _description_
    """
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada


@decoradora
def soma(x, y):
    """_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    """
    return x + y


resultado = soma(10, 5)
