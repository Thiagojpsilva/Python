# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

path='C:\\Users\\f8084478\\OneDrive - TIM\\Pessoal\\GIT\\Pessoal\\Arquivos_Aula\\'
file='file_aula55.txt'


# f1 = open(path+file,'w')
# f1.close()

with open(path+file,'w') as f1:
    f1.write('Linha 1 \n')
    f1.write('Linha 2 \n')
    
with open(path+file,'w+') as f1:
    f1.write('Linha 1 \n')
    f1.write('Linha 2 \n')
    f1.writelines(
        ('Linha 3 \n','Linha 4\n')
        )
    f1.seek(0,0)
    print(f1.read().strip())
    
# with open(path+file,'r') as f1:
#     print(f1.read())
    