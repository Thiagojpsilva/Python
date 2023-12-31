"""
Try e Execpt em Python

Try -> Tentar executar o Código
Execpt -> Ocorreu algum erro ao tentar executar
"""

nome = input('Qual seu nome:')
idade = input('Qual sua idade:')

if (nome and idade):

    print(f'Seu nome é : {nome}')
    print(f'Sua idade é : {idade}')
    print(f'Seu nome investido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaço.')
        print(f'Seu nome tem {len(nome)-1} letras')
    else:
        print('Seu nome não contém espaço.')
        print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    #  v_len=len(nome)-1
    #  print(f'A Ultima letra do seu nome é: {nome[v_len]}')
    print(f'A Ultima letra do seu nome é: {nome[-1]}')
else:
    print("Nome ou Idade não foram preenchidos.")
