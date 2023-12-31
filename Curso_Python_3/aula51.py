# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(a):
    return a['nota']


alunos_agrupados = sorted(alunos, key=ordena)

# for aluno in alunos_agrupados:
#    print(aluno)

# alunos = ['a','a','a','a','b','c','a','b']
# alunos.sort()

# grupos = groupby(alunos)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(f'Nota {chave}:')
    for aluno in grupo:
        print(aluno['nome'])
    print('')
