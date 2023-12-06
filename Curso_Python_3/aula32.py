"""
Repetição 
For - While
"""

v_count = 0         

while v_count <=10:
    v_count += 1 
    if v_count  == 6:
       print(f'Não vou mostarar {v_count}') 
       # break    # Sai do While e não faz mais o loop.
       continue # Volta para o While para testar a proxima condição.
    print(f'Estou no {v_count}')
    
    
    