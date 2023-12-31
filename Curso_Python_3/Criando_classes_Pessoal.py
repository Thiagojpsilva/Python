
import json

PATH = 'C:\\Users\\f8084478\OneDrive - TIM\\Pessoal\\GIT\\Pessoal\\Python' \
       '\\Curso_Python_3\\arquivos\\'
ARQUIVOS = 'pesoas.json'
local = PATH+ARQUIVOS


class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome.upper()
        self.idade = int(idade)
        self.altura = float(altura)
        self.peso = int(peso)


def update_file(pessoas, path):
    with open(path, 'w', encoding='utf8') as arquivo:
        json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
    return


def Carga_dodos():
    p1 = Pessoa(input("Nome:"), input("Idade:"),
                input("Altura:"), input("Peso:"))
    p2 = Pessoa(input("Nome:"), input("Idade:"),
                input("Altura:"), input("Peso:"))
    p3 = Pessoa(input("Nome:"), input("Idade:"),
                input("Altura:"), input("Peso:"))
    groups = [vars(p1), vars(p2), vars(p3)]
    update_file(groups, local)


if __name__ == '__main__':
    Carga_dodos()
