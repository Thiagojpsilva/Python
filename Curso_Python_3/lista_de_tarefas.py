# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

primery_list = []
next_list = []

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Comandos: listar, desfazer, refazer e editar \nDigite um comando:')
    
    
def list_task():
    print('\n','-'*30,'\n') 
    print('\n'.join(map(str, primery_list)))
    print('\n','-'*30)
    input('Click Enter Para Continuar.')

def exec_func(funcao, *args):
    result = funcao(*args)
    return result

def undo_list():
    if primery_list:
        removed_task = primery_list.pop()
        print(f'Tarefa removida: {removed_task}')
    else:
        print('\nA lista está vazia. Não há tarefas para desfazer.\n')
    
def remake_list():
    global next_list
    if len(primery_list) < len(next_list):
        if len(primery_list) == 0:
           primery_list.append(next_list[0])
        else:
           primery_list.append(next_list[len(primery_list)])  
    else:
        print(f'\nNão há tarefas para serem refeitas.\n')      

def add_task(*args):
    global next_list
    primery_list.append(*args)
    next_list = primery_list.copy()
    # print(f'Print task: {*args}')

clean_screen()

while True:
    option = input()
    
    if option.upper() == 'LISTAR':
        if not primery_list:
            print('A lista está Vazia!')
            input('Click Enter Para Continuar.')
        else:
            exec_func(list_task)
        
    elif option.upper() == 'EDITAR':
        item = input('Qual tarefa será adicionada: ')
        exec_func(add_task, item)
        exec_func(list_task)
    
    elif option.upper() == 'DESFAZER':
        exec_func(undo_list)
        exec_func(list_task)

    elif option.upper() == 'REFAZER':
        exec_func(remake_list)
        exec_func(list_task)

    else:
        print('Comando desconhecido comandos válidos (listar, desfazer, refazer e editar)!')
        input('Click Enter Para Continuar.')
    clean_screen()    
#######
## Codigo Curso
######


# # desfazer = [] -> Refazer ['caminhar', 'fazer café']
# # refazer = todo ['fazer café']
# # refazer = todo ['fazer café', 'caminhar']
# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'clear':
#         os.system('clear')
#         continue
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue