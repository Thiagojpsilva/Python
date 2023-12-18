# Decoradores com paramentros

def decoradora(func):
    print('Decoradora 1')
    
    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args,**kwargs)
        return res
    return aninhada

@decoradora
def soma(x, y):
    return x + y


resultado = soma(10,5)
 