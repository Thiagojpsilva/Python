"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# Solução 1
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

for a, b in zip(lista_a, lista_b):
    lista_soma.append(a+b)
print(lista_soma)

# Codigo mais curto
# Usou for ternario para iterar na lista gerada pelo Zip e atribuiu a lista.
lista_soma2 = [a + b for a, b in zip(lista_a, lista_b)]
print(lista_soma2)
