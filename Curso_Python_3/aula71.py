# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...


class OutherError(Exception):
    ...


def raiser():
    execption_ = MyError('a', 'b', 'c')
    execption_.add_note('Olhar a nota anterior')
    execption_.add_note('Voce erro tal coisa.')
    raise execption_


try:
    # 1/0
    raiser()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutherError('Vou lançar de novo.')
    exception_.__notes__ += error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error
