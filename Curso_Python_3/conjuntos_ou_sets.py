# criando um set (Conjunto) vazio.
s1=set()
# Pode ser criando um consunto com dados {1,2}, diferença do Dicionario que que não é chave valor
# somente valor.
s4={1,2}

#se for criado um set apenas com valores imutavais ex str: ele irá inteirar(incluir letra a letra.)

s5=set('Thiago')
print(s5)
s5.add('Johnatas')
print(s5)

# Update tambem add porem ele faz iteracao.
s5.update('Johnatas')
print(s5)

# Para evitar isso tem que ser feito com () 'tupla' obs: Tupla tem uma virgula ser for apenas um valor.
s5.update(('Silva',))
print(s5)

# s1.clear()
#s1.discard('Olá mundo')
#s1.discard('Luiz')
#print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print('Conjunto s1:')
print(s1)
print('Conjunto s2:')
print(s2)
print('\n\n')
s3 = s1 | s2
print(s3)
print('É a união dos conjuntos.') 
s3 = s1 & s2
print(s3) 
print('É intersecão dos conjuntos.')
s3 = s1 - s2
print(s3)
print('Diferença dos consuntos conjunto 1 - conjunto 2.' )
s3 = s2 - s1
print(s3)
print('Diferença dos consuntos conjunto 2 - conjunto 1.' )
s3 = s1 ^ s2
print(s3)
