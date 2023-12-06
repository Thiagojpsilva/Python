"""
Atividade aula 54

"""

input_num = input('Digite um número inteiro:')

try:
    num_int = int(input_num)
    if (num_int % 2) == 0 :
        print('Número é Par')
    else:
        print('Número é ímpar')
except:
    print('Número não é interio.')
    
print('-'*60)

input_hr = input('Digite a hora do dia:')

try:
    hora = int(input_hr)

    if hora >= 0 and hora <=11:
        print ('Bom dia!!')
    elif hora >= 12 and hora <=17:
        print ('Boa tarde!!')
    elif hora >= 18 and hora <=23: 
        print ('Boa Noite!!')
    else:
        print ('Não reconheço essa hora.')
except:
    print ('Não reconheço essa hora. Digite uma hora entre 0 e 23!')

print('-'*60)

input_nome = input('Qual seu nome?')

qtd_nome=len(input_nome)

if qtd_nome > 1:
    if qtd_nome <= 2:
        print('Seu nome é curto!')
    elif qtd_nome >= 5 and qtd_nome <= 6:
        print('Seu nome é Normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite um nome válido!')
    