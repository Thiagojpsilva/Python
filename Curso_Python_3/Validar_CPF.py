"""
Calculo dos dígitos do CPF

"""

import re
import sys

cpf = input("DIGITE O CPF:")


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


# cpf = cpf.replace('.','').replace('-','')
# Modulo de expressão regulares. Retirar dados diferente de numeros.
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
)
# Validar sequencia de digitos.
cpf_d1: str = cpf[0]
if cpf_d1 * len(cpf) == cpf:
    print('CPF digitado não pode ser Sequencial!')
    sys.exit()

cpf: int(cpf)

lista_cpf = list(map(int, cpf))

if len(cpf) != 11:
    print("CPF TEM QUE POSSUIR 11 DIGITOS.")
else:
    v_first_dig = valida_digito_1()
    v_valida_d1 = ('Válido' if v_first_dig == lista_cpf[-2] else 'Inválido')
    if v_valida_d1 == 'Válido':
        v_second_dig = valida_digito_2()
        v_valida_d2 = ('Válido' if v_second_dig ==
                       lista_cpf[-1] else 'Inválido')
        if v_valida_d2 == 'Válido':
            print(f"O CPF {cpf} É VÁLIDO!!")
        else:
            print(f"O CPF {cpf} É INVÁLIDO - SEGUNDO DIGITO!!")

    else:
        print(f"O CPF {cpf} É INVÁLIDO - PRIMEIRO DIGITO!!")

# Codigo do professo:
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
# entrada = input('CPF [746.824.890-70]: ')
# cpf_enviado_usuario = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )

# entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_e_sequencial:
#     print('Você enviou dados sequenciais.')
#     sys.exit()

# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')
