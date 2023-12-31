"""

Atividade aula 66 a 68 (Calculadora Simples)

"""

while True:

    num_1 = input('Digite o Primerio número interio: ')
    num_2 = input('Digite o Segundo número interio: ')
    operador = input('Digite a operação que deseja realizar(-,+,*,x,/): ')

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        numeros_validos = True
        if (operador == '*' or operador == 'x' or operador == 'X'):
            print(f'O resultado da Multiplicação dos numeros {
                  num_1} e {num_2} é: {num_1 * num_2}.')
        elif operador == '+':
            print(f'O resultado da Soma dos numeros {
                  num_1} e {num_2} é: {num_1 + num_2}.')
        elif operador == '-':
            print(f'O resultado da Subtração dos numeros {
                  num_1} e {num_2} é: {num_1 - num_2}.')
        elif operador == '/':
            print(f'O resultado da Divisão dos numeros {
                  num_1} e {num_2} é: {num_1 / num_2}.')
        else:
            print('Operador inválido.')
            continue

    except ImportError:
        numeros_validos = False

    if not numeros_validos:
        print('Um ou Ambos os números digitados não é/são válido[s].')
        continue

    sair = input(
        'Digite [s]air para encerrar a Calculadora: ').lower().startswith('s')

    if sair:
        print('Até a Proxima!')
        break
