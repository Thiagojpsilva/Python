# Introdução à função lambda (função anônima de uma linha)
# lambda usabilidade teste 
# 

def executa(funcao,*args):
   return funcao(*args)

v1 = executa(lambda  x: 'Positivo' if x >= 1 else 'Negativo',-1)

print (v1)  

