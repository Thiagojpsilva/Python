"""
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.
"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
lista = [4, 32, 1, 34, 5, 6, 6, 21]
print('A lista é: \n', lista)
# Ordernar a lista
lista.sort()
print('A lista Ordernar é: \n', lista)
# Ordernar a lista decresente
lista.sort(reverse=True)
print('A lista Ordernar decresente é: \n', lista)

lista = [4, 32, 1, 34, 5, 6, 6, 21]
# Criar uma nova lista já ordenada:
l3 = sorted(lista)
print("A Lista agora é : \n", lista)
print("A nova lista ordenada é : \n", l3)


# sorted(lista)
lista_dictionary = [
    {'nome': 'Luiz', 'sobrenome': 'Xuxa'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista_dictionary, key=lambda item: item['nome'])

l2 = sorted(lista_dictionary, key=lambda item: item['sobrenome'])

print('Printando o l1:\n', l1)

exibir(l1)
exibir(l2)
