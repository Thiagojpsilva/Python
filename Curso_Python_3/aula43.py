""" copy, sorted, produtos.sort
 Exercícios
 Aumente os preços dos produtos a seguir em 10%
 Gere novos_produtos por deep copy (cópia profunda)
 Ordene os produtos por nome decrescente (do maior para menor)
 Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
 Ordene os produtos por preco crescente (do menor para maior)
 Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

import copy
from dados import produtos
from aula_43_package import percent_10

novos_produtos = copy.deepcopy(produtos)
for i in novos_produtos:
    i['preco'] = float((percent_10(i['preco'])))

produtos_ordenados_por_nome = sorted(
    produtos, key=lambda item: item['nome'], reverse=True)
produtos_ordenados_por_preco = sorted(produtos, key=lambda item: item['preco'])
produtos_ordenados_decre_preco = sorted(
    produtos, key=lambda item: item['preco'], reverse=True)
# print(*produtos,sep='\n')
print('Produtos:')
# exibir(produtos)
print(*produtos, sep='\n')
print('Novos Produtos:')
print(*novos_produtos, sep='\n')
# exibir(novos_produtos)
print('Ordenado Nome:')
print(*produtos_ordenados_por_nome, sep='\n')
# exibir(produtos_ordenados_por_nome)
print('Ordenado Preco:')
print(*produtos_ordenados_por_preco, sep='\n')
# exibir(produtos_ordenados_por_preco)
print('Ordenado Decrescente Preco:')
print(*produtos_ordenados_decre_preco, sep='\n')
# exibir(produtos_ordenados_decre_preco)
