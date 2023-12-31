"""
Gerar CPF Valido

"""

import re
import random


def gerar_9_dig():
    cpf_9 = ""
    for _ in range(9):
        cpf_9 += str(random.randint(0, 9))
    return cpf_9


def valida_digito_1():
    v_mult = 0
    lista_mult = list(range(10, 1, -1))
    for i, vl in enumerate(lista_cpf[:9]):
        v_mult: int = v_mult + (vl * lista_mult[i])
    v_dig_1 = (v_mult * 10) % 11
    v_dig_1 = (v_dig_1 if v_dig_1 <= 9 else 0)
    return v_dig_1


def valida_digito_2():
    v_mult = 0
    lista_mult = list(range(11, 1, -1))
    for i, vl in enumerate(lista_cpf[:10]):
        v_mult += (vl * lista_mult[i])
    v_dig_2 = (v_mult * 10) % 11
    v_dig_2 = (v_dig_2 if v_dig_2 <= 9 else 0)
    return v_dig_2


# Main
# Validar sequencia de digitos.
for _ in range(100):
    v1 = True
    while v1:
        cpf = gerar_9_dig()
        cpf_d1: str = cpf[0]
        if cpf_d1 * len(cpf) == cpf:
            v1 = True
        else:
            v1 = False

    cpf: int(cpf)
    lista_cpf = list(map(int, cpf))

    # Gerar primeiro digito
    v_first_dig = valida_digito_1()

    # Incluir Primeiro digito na lista
    lista_cpf.append(v_first_dig)

    # Gerar Segundo digito
    v_second_dig = valida_digito_2()

    # Incluir Segundo digito na lista
    lista_cpf.append(v_second_dig)

    # Apresentar cpf
    print(''.join(map(str, lista_cpf)))
