"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.

"""

import os
lista = []
v_out = 'C'

def clear_screen():
    
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-'*60)
        title='Lista de Compras'
        print(f'{title:^60}')
        print('-'*60)

def incluir_item():
    entrada = input ("Informe o novo Item: ").upper()
    return entrada

while True:
    clear_screen()
    v_insert = False
    action = input ("[L]istar Itens\n[N]ovo item\n[A]pagar Item\n[S]air\n -->")    
    
    if action[:1].upper() == 'N':
       while v_insert == False:
            item = incluir_item()
            if item not in lista:
                lista.append(item)
                v_insert = True
            else:
                print("O item informado já consta na lista.")
                            
    elif action[:1].upper() == 'L':
       
       print("Os Item em sua lista são:",'\n','\n '.join(map(str,lista)))
       v_out = input(f"Digite [C]ontinuar no Programa ou [S]air: ".upper())
       
    elif action[:1].upper() == 'A':
       deletar: str = input("Qual item deseja apagar? ").upper()
       try:
           lista.remove(deletar)
       except ValueError as ve:
           if "not in list" in str(ve):
              print(f'O Item {deletar} não está na lista!')
              input('')
              continue
           else:
              print(f'Ocorreu um erro ao excluir o item: {ve}')
              input('')
              continue
    elif action[:1].upper() == 'S':
         v_out = 'S'
         
    else:
        print("Opção informada é inválida !")
        input('')
        
       
    if v_out[:1].upper() == 'C':
            clear_screen()
            continue
    elif v_out[:1].upper() == 'S':
            break
 
### Codigo feito pelo professos: 

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('clear')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         indice_str = input(
#             'Escolha o índice para apagar: '
#         )

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite número int.')
#         except IndexError:
#             print('Índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
#     elif opcao == 'l':
#         os.system('clear')

#         if len(lista) == 0:
#             print('Nada para listar')

#         for i, valor in enumerate(lista):
#             print(i, valor)
#     else:
#         print('Por favor, escolha i, a ou l.')        