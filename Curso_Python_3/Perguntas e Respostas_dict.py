# Exercício - sistema de perguntas e respostas

import random
import os

def input_asward():
    return input('Resposta: ') 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

perguntas = [
        {
            'Pergunta': 'Quanto é 2+2?',
            'Opções': ['1', '3', '4', '5'],
            'Resposta': '4',
        },
        {
            'Pergunta': 'Quanto é 5*5?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': '25',
        },
        {
            'Pergunta': 'Quanto é 10/2?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': '5',
        },
    ]

v_acertos = 0
# Jogo irá realizar apenas 3 perguntas 
for _ in range(3):
    clear_screen()
    # Atribuido a varial r_dict um dict da lista aleatoriamente
    r_dict = (random.choice(list(perguntas)))
    
    print(f'Pegunta: {r_dict['Pergunta']} ')
    # Presentar as opções de resposta na tela:
    for i, vl in enumerate(r_dict['Opções']):
        print(f'{i+1}) {vl} ')
        
    r_ok = True
    while r_ok:
        
        # Invocar a função para coletar a Resposta.
        answard_idx=input_asward()
        
        # Validar se a resposta é valida.
        if answard_idx.isdigit():
            if int(answard_idx) in (range(1,5)):
                r_ok = False
            else:
                print('As opção são de 1 a 4.')
        else:
                print('Apenas números de 1 a 4 são aceitos.')
                
    #Pegar o valor da resposta escolhida.        
    answard_vl= r_dict['Opções'][int(answard_idx)-1]

    #Validar se a resposta escolhida é igual a resposta correta.
    if answard_vl == r_dict['Resposta']:
         print('Acertou ✅!!!')
         v_acertos += 1
         input()
    else:
         print('Errou ❌!!!')
         input()
    # Excluir a pergunta feita da lista para evitar que seja apresentada novamente.
    perguntas.remove(r_dict)
    
print(f'Você respondeu {v_acertos} corretamente !!!')

"""
# Solucao professos:

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
"""
