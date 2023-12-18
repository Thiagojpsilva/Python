# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 =  ['BA', 'SP', 'MG', 'RJ']

# Não foi usado nessa atividade.
# def decoradora(func):
#     def aninhada(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res
#     return aninhada
    
def zipper(lista1,lista2):
    # print(min(1,2))
    # print(min(300,200))
    # print(f'{len(lista1)} - City')
    # print(f'{len(lista2)} - Stage')
    # print(min(len(lista1),len(lista2)))
    # print(min(lista1,lista2))
    intervalo_maximo = min(len(lista1),len(lista2))
    return [
        ## For ternario
        (lista1[i],lista2[i]) for i in range(intervalo_maximo)
    ]
print(zipper(l1,l2))

#Outra forma de fazer:    
print(list(zip(l1,l2)))

#Mais uma forma de fazer (Porém a iteração é feita pela lista mais longa.)
#fillvalue substitui o none por algum valor determinado.
print(list(zip_longest(l1,l2,fillvalue='SEM CIDADE')))




