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
import json

PATH = 'C:\\Users\\f8084478\OneDrive - TIM\\Pessoal\\GIT\\Pessoal\\Python\\Curso_Python_3\\arquivos\\'
ARQUIVOS = 'tarefas.json'
local = PATH+ARQUIVOS

def read_task(path):
    data = []
    global primery_list
    try:
        with open(path,'r',encoding='utf-8') as arquivo:
            data= json.load(arquivo)   
    except FileNotFoundError:
        print ('Arquivo não existe!')
        primery_list = []
        update_file()
    return list(data)

def update_file():
    global PATH
    global ARQUIVOS
    global primery_list
    local =  PATH + ARQUIVOS
    with open(local, 'w', encoding='utf8') as arquivo:
        data = json.dump(primery_list, arquivo, indent=2, ensure_ascii=False)
    return data

    
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Comandos: listar, desfazer, refazer e editar \nDigite um comando:')
    
    
def list_task():
    
    if not primery_list:
        print('A lista está Vazia!') 
        input('Click Enter Para Continuar.')
    else:
        print('\n','-'*30,'\n') 
        print('\n'.join(map(str, primery_list)))
        print('\n','-'*30)
        input('Click Enter para continuar.')

def exec_func(funcao):
    result = funcao()
    return None

def undo_list():
    if primery_list:
        removed_task = primery_list.pop()
        print(f'Tarefa removida: {removed_task}')
        update_file()
    else:
        print('\nNão há tarefas para desfazer.\n')
         
    exec_func(list_task)
       
def remake_list():
    global next_list
    if len(primery_list) < len(next_list):
        if len(primery_list) == 0:
           primery_list.append(next_list[0])
           update_file()
        else:
           primery_list.append(next_list[len(primery_list)])
           update_file()  
    else:
        print(f'\nNão há tarefas para serem refeitas.\n')      
        
    exec_func(list_task)
    
def add_task():
    global next_list
    item = input('Qual tarefa será adicionada: ')
    primery_list.append(item.strip())
    next_list = primery_list.copy()
    update_file()
    exec_func(list_task)

clean_screen()

primery_list = read_task(local)
next_list = read_task(local)

while True:
    option: str = input().upper()
    
    comandos={
            'LISTAR': lambda: exec_func(list_task),
            'EDITAR': lambda: exec_func(add_task),
            'DESFAZER': lambda: exec_func(undo_list),
            'REFAZER': lambda: exec_func(remake_list)
    }
    
    if option in ('LISTAR','EDITAR','DESFAZER','REFAZER'):
        comando = comandos.get(option)()   
            
    else:
        print('Comando desconhecido comandos válidos (listar, desfazer, refazer e editar)!')
        input('Click Enter para continuar.')

    clean_screen()

    continue

    # if option.upper() == 'LISTAR':
    #     if not primery_list:
    #         print('A lista está Vazia!')
    #         input('Click Enter Para Continuar.')
    #     else:
    #         exec_func(list_task)
        
    # elif option.upper() == 'EDITAR':
    #     item = input('Qual tarefa será adicionada: ')
    #     exec_func(add_task, item)
    #     exec_func(list_task)
    
    # elif option.upper() == 'DESFAZER':
    #     exec_func(undo_list)
    #     exec_func(list_task)

    # elif option.upper() == 'REFAZER':
    #     exec_func(remake_list)
    #     exec_func(list_task)

    # else:
    #     print('Comando desconhecido comandos válidos (listar, desfazer, refazer e editar)!')
    #     input('Click Enter Para Continuar.')
    # clean_screen()    
