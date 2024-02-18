# os.listdir para navergar em caminhos
# caminho = r''
import os
caminho = os.path.join('c:/', 'tmp')

if os.path.exists(caminho) and os.path.isdir(caminho):
    for pasta in os.listdir(caminho):
        caminho_full = os.path.join(caminho, pasta)
        if os.path.exists(caminho_full) and os.path.isdir(caminho_full):
            print(caminho_full)
            for item in os.listdir(caminho_full):
                print('  ', item)
