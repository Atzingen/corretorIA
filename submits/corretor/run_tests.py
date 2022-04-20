import os, sys, csv
import pandas as pd
from importlib import import_module
from .correction_scripts import test_functions

def run(script_name):
    print('run')
    module = import_module('submits.corretor.submit_scripts.' + script_name.strip('.py'))
    yield str(test_functions.test_all(module))

# data = []
# for script in scripts_for_test:
#     try:
#         module = import_module('diff.' + script.strip('.py'))
#         nota = test_functions.test_all(module)
#         print(f'Executado script de {module.nome} - atividade {module.atividade} - nota: {nota}')
#         data.append([script, module.nome.replace('_', ' '), module.CPF, module.data_nascimento, nota])
#     except Exception as e:
#         if module.nome and module.atividade and module.CPF and module.data_nascimento:
#             data.append([script, module.nome.replace('_', ' '), module.CPF, module.data_nascimento, 
#                          'erro'])
#         else:
#             data.append([script, 'erro', 'erro', 'erro'])
#         print(f'Error {module} - {e}')
# print(f'End os script \nData{data}')
# df = pd.DataFrame(data, columns=["Node do Script", "Nome", "CPF", "data_nascimento",
#                                  "Atividade", "Nota",])
# df.to_excel("resultados_full3.xlsx")