#Reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 20},
    {'nome': 'Produto 3', 'preco': 30},
    {'nome': 'Produto 2', 'preco': 40},
    {'nome': 'Produto 4', 'preco': 50},
]

# def fucao_do_reduce(acumulador,produto):
#     print(acumulador)
#     return acumulador + produto['preco']

total = reduce(
    #fucao_do_reduce,
    lambda ac,p: ac + p['preco'],
    produtos,
    0.0 #valor inicial
)

print('Total é:',total)