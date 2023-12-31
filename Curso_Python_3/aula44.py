"""
Exercício - Adiando execução de funções

"""


def soma(x, y):
    return x + y


def multiplica(x, y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x * y


def criar_funcao(funcao, x):
    """_summary_

    Args:
        funcao (_type_): _description_
        x (_type_): _description_

    """
    def aguarda_y(y):
        return funcao(x, y)
    return aguarda_y


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(5))
