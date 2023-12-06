# nome  = input('Qual seu nome? ')
# print (f'O seu nome é {nome}') # se colocar o valor '=' apos a Var e possivel ver o nome e valor.

v1 = input('Digite um valor": ')
v2 = input('Digite outro valor: ')

v1 = int(v1)
v2 = int(v2)

if v1 > v2:
    print(f'Primeiro valor {v1} é maior que o Segundo valor {v2}')
    
elif v1 < v2:
    print(f'Segundo valor {v2} é maior que o Primeiro valor {v1}')
    
else:
    print(f'Primeiro valor {v1} é igual o segundo valor {v2}')
