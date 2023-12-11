# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def calcular_lista(*args):
    soma = 1
    for num in args:
        soma*=num
    return soma
    
def par_ou_impar(num):
    print(f'{num} é: '+'Par' if num%2 ==0 else 'Impar')

#Main 

v_mult = calcular_lista(1,2,3)
par_ou_impar(v_mult)
