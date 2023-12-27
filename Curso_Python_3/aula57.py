# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self,cor):
        # private protecet 
        self._cor = cor
        #self.cor_tinta = cor
        #self._cor = cor
    
    #Properte para o codigp clente se comporta como um atributo, mas na classe 
    # é um metodo.    
    @property
    def cor(self):
        #return self.cor_tinta
        return self._cor
    
    @property
    def cor_tampa(self):
        return 123456
     
    @cor.setter
    def cor(self,valor):
        print('Estou no setter', valor)
        self._cor = valor 
    
#####################################################

caneta = Caneta('Azul')
caneta_bic = Caneta('Vermelha')
## Getter obter valor.
print(caneta_bic.cor)
print(caneta.cor)
print(caneta.cor_tampa)
caneta.cor = 'ROSA'
print(caneta.cor)
print(caneta._cor)




# class Caneta:
#     def __init__(self,cor):
#         # private protecet public
#         self.cor_tinta = cor
        
#     #### Getter 
#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta
    
# #####################################################

# caneta = Caneta('Azul')
# caneta_bic = Caneta('Vermelha')
# print(caneta_bic.get_cor())
# print(caneta.get_cor())





