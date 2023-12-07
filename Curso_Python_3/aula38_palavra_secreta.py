"""

JOGO DA PALAVRA OCULTA AULA 76
Palavra secreta.

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