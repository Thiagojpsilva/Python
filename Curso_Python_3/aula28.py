"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] i = inicio : f = final : p = Salto
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'

# Escreve ao contratrio
print(variavel[::-1])

# Pega posição
print(variavel[5])

# pega a partir da posição ate o final
print(variavel[4:])

# pega a partir da posição ate valor definido
print(variavel[4:7])

# Vai da primeira letra e realiza saltos definidos
print(variavel[::2])

# contar os caracteres
print(len(variavel))

# Centralizar entre 50 espaços - incluido o valor da string (Tem que ser usado
# em fstrings)
print(f'{variavel: ^50}')

# Manter a direita entre 50 espaços - incluido o valor da string (Tem que ser
# usado em fstrings)
print(f'{variavel: >50}')

# Manter a esquerda entre 50 espaços - incluido o valor da string (Tem que ser
# usado em fstrings)
print(f'{variavel: <50}.')

# Pode ser preencho com um valor especifico (Tem que ser usado em fstrings)
print('*'*50)

# Pode ser preencho com um valor especifico (Tem que ser usado em fstrings)
print(f'{variavel:*^50}')

# Pode ser preencho com um valor especifico (Tem que ser usado em fstrings)
print('*'*50)

# Vai mostrar o + em caso de positivo
print(f'{1000.30030:+,.2f}')

# Irá mostrar o - em caso de negativo mas o positivo não vai apresentar o +
print(f'{1000.30030:-,.2f}')

print(f'{-1000.30030:-,.2f}')
