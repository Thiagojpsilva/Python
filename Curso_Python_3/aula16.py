# nome  = input('Qual seu nome? ')
# print (f'O seu nome é {nome}') # se colocar o valor '=' apos a Var e possivel
# ver o nome e valor.

entrada = input('Você quer "Entrar" ou "Sair": ')


if entrada.upper() == 'ENTRAR':
    print('Você entrou no sistema!')

elif entrada.upper() == 'SAIR':
    print('Você saiu do sistema!')

else:
    print('Você não digitou nem Entrar nem Sair.')
