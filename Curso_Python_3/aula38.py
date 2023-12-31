# Exercícios com funções
# def duplica(i):
#     return(i*2)
# def triplica(i):
#     return(i*3)
# def quadruplica(i):
#     return(i*4)

def criar_multiplicador(mult):
    def multiplicar(numero):
        return numero * mult
    return multiplicar

# Main


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplica = criar_multiplicador(4)

print(duplicar(2), triplicar(2), quadriplica(2))
