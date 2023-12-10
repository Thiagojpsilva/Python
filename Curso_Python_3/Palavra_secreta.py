"""

JOGO DA PALAVRA OCULTA AULA 76
Palavra secreta.


Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""
import random
import os

# Função de limpeza de tela.
def clear_screen(total):
    if total > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-'*60)
        title='PALAVRA OCULTA'
        print(f'{title:^60}')
        print('-'*60)
        print(f'Tentativas Realizadas:{total}')
        print("\n\n")
    else:
         os.system('cls' if os.name == 'nt' else 'clear')
    
# Codigo principal.
while True:
    # Incia o codigo apresentado o titulo.
    title='PALAVRA OCULTA'
    print('-'*60)
    print(f'{title:^60}')
    print('-'*60)
    print("\n\n")
    
    # Variavel para sair do codigo.
    v_out = None
    
    # Criar um Vetor vazio.
    vt_used = []
    
    ## Criar um vertor com algumas palavras aleatorias
    lst_words = ['banana','computador','escola','abacaxi','livro','janela','escrita','avião','teclado','cachorro','Casa','Papagaio','elevador','telefone']

    ## Abribuir em uma variavel uma das palavras do vetor de forma aleatoria.
    r_word = random.choice(lst_words).upper()
    
    ## Variavel para determinar as tentativas
    v_try = 0    
    letters=len(r_word)
    
    ## Criar um vetor apenas com valor * para cada letra da palavra aleatoria.
    vt_hidden=['*'] * letters
    h_word = ''.join(vt_hidden)
    print(h_word)
    
    ## Criar um vertor que vai contar cada letra da palavra selecionada. 
    vt_word = []
    for i in r_word:
       vt_word.append(i)
    #print(vt_word)       
    
    while True:
       print("\n\n")  
       l_try= input('Informe uma Letra: ')
       v_try +=1
       
       vt_used.append( l_try[:1].upper())
       
       for i,v in enumerate(vt_word): 
           if l_try[:1].upper() == v:
              vt_hidden[i] = l_try[:1].upper()
              h_word = ''.join(vt_hidden)
                
       #Chamar a funcão de limpar tela
       clear_screen(v_try) 
       print('As letras já testadas foram:')
       print(vt_used)
       print("\n\n")  
       print(h_word)
       if '*' not in(h_word):
           print("\n")  
           print('Você descobriu a palavra. Parabéns')
           print("\n\n")  
           v_out = input ('Deseja [S]air ou [I]nicianar uma nova Partida : ')
       
       if v_out == None:
            continue
       elif v_out[:1].upper() == 'I':
            break
       elif v_out[:1].upper() == 'S':
            break
       else:
            print('Opcão inválida escolhida irei Sair.')
            v_out='S'
            break
    
    if v_out[:1].upper() == 'I':
            clear_screen(0)
            continue
    elif v_out[:1].upper() == 'S':
            break
     
'''
Codigo forneceido pelo professor no curso. outra forma de solucionar:

'''
# import os

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0