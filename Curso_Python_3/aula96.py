'''pathlib trabalhando com caminhos'''

import os
from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)
# print(caminho_arquivo.parent.parent)

# Definir o arquivo e depois cria-lo
# arquivo = Path.home() / 'desktop' / 'arquivo_teste_python.txt'
pasta_raiz = Path.home() / 'desktop' / 'Pasta_TJ'
# print(Path.home() / 'desktop')
# Criar arquivo.
pasta_raiz.mkdir(exist_ok=True)
subpasta = pasta_raiz / 'subpasta'
subpasta.mkdir(exist_ok=True)

for i in range(10):
    file = subpasta / f'TJ_{i}.txt'
    # file.touch()
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open("a+") as text_file:
        text_file.write('Olá TJ \r\n')
        text_file.write(f'{file.name}')

# Função para deletar pasta e subpastas.


def rmtree(dir_: Path, remove_dir_=True):
    for file in dir_.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file)
            file.rmdir()
        else:
            print('File: ', file)
            file.unlink()


# rmtree(pasta_raiz)
# pasta_raiz.rmdir()
