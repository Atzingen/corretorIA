import time
from importlib import import_module
from inspect import getmembers, isfunction
from submits.models import *

def base_test(m, base_check):
    '''
    Basic test to see if the module
    variables and functions exist in the script
    '''
    for item in base_check:
        if not item in dir(m):
            return False
    return True

def teste_progressao_aritmetica(m):
    '''
    Test Function 1
    
    return nota -> float (0.0, 1.0)
    '''
    nota, testes = 0, 0
    # parte 1 do teste
    testes += 1
    if m.progressao_aritmetica(1, 2, 4) == [1, 3, 5, 7]:
        nota += 1
    # parte 2 do teste
    testes += 1
    if m.progressao_aritmetica(3, 2, 4) == [3, 5, 7, 9]:
        nota += 1
    # parte 3 do teste
    testes += 1
    if m.progressao_aritmetica(5, 1, 2) == [5, 6]:
        nota += 1
    return nota/testes

def teste_soma_pa(m):
    nota, testes = 0, 0
    
    testes += 1
    if m.soma_pa(1, 2, 4) == 16:
        nota += 1
        
    testes += 1
    if m.soma_pa(1, 2, 2) == 4:
        nota += 1
    
    testes += 1    
    if m.soma_pa(2, 3, 2) == 7:
        nota += 1  
    return nota/testes

def teste_progressao_geometrica(m):
    nota, testes = 0, 0
    
    testes += 1
    if m.progressao_geometrica(1, 2, 4) == [1, 2, 4, 8]:
        nota += 1
        
    testes += 1
    if m.progressao_geometrica(1, 2, 3) == [1, 2, 4]:
        nota += 1
    
    testes += 1    
    if m.progressao_geometrica(1, 3, 3) == [1, 3, 9]:
        nota += 1
        
    return nota/testes

def teste_soma_pg(m):
    nota, testes = 0, 0
    
    testes += 1
    if m.soma_pg(1, 2, 3) == 7:
        nota += 1
        
    testes += 1
    if m.soma_pg(1, 2, 4) == 15:
        nota += 1

    return nota/testes

def teste_fibonacci(m):
    nota, testes = 0, 0
    
    testes += 1
    if m.fibonacci(4) == [0, 1, 1, 2]:
        nota += 1
        
    testes += 1
    if m.fibonacci(2) == [0, 1]:
        nota += 1
    
    testes += 1    
    if m.fibonacci(6) == [0, 1, 1, 2, 3, 5]:
        nota += 1
        
    return nota/testes

def teste_soma_fibonacci(m):
    nota, testes = 0, 0
    
    testes += 1
    if m.soma_fibonacci(4) == 4:
        nota += 1
        
    testes += 1
    if m.soma_fibonacci(5) == 7:
        nota += 1
    
    testes += 1    
    if m.soma_fibonacci(1) == 0:
        nota += 1
        
    testes += 1    
    if m.soma_fibonacci(2) == 1:
        nota += 1
        
    return nota/testes

def teste_primo(m):
    nota, testes = 0, 0
    
    testes += 1
    if m.primo(13) == True:
        nota += 1
        
    testes += 1
    if m.primo(21) == False:
        nota += 1
        
    return nota/testes

def teste_fit_linear(m):
    nota, testes = 0, 0
    
    testes += 1
    resp = m.fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    if resp[0]== 0 and resp[1] == 1:
        nota += 1
        
    testes += 1
    resp = m.fit_linear([1, 2, 3, 4, 5], [11, 21, 31, 41, 51])
    if  resp[0] == 1 and resp[1] == 10:
        nota += 1
        
    return nota/testes

def test_all(model, user):
    functions = [teste_progressao_aritmetica, teste_soma_pa, teste_progressao_geometrica, teste_soma_pg, teste_fibonacci, teste_soma_fibonacci, teste_primo, teste_fit_linear]
    base_check = ['nome', 'email']
    submission = Submission(user=user)
    function_format = ''
    if base_test(model, base_check):
        submission.is_valid = True 
        nota_parcial, etapas = 0, []
        for i, f in enumerate(functions):
            try:
                n = f(model)
                msg = 'OK'
            except Exception as e:
                n = 0
                msg = repr(e)
                function_format += msg + '\n\n----------------------------\n'
            etapas.append(n)
            nota_parcial += n
            yield {'partial': [f.__name__, str(100*n) + '%', 100*(i+1)/len(functions), msg]}
            time.sleep(1)
        submission.score = 10*n
    else:
        submission.is_valid = False   
    if function_format is not 'OK':
        submission.debug_data = function_format
    submission.save()
    yield {'Nota':str(10*nota_parcial/len(etapas))}