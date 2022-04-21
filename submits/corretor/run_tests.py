import os, sys, csv
import pandas as pd
from importlib import import_module
from .correction_scripts import test_functions

def run(script_name):
    print('run')
    module = import_module('submits.corretor.submit_scripts.' + script_name.strip('.py'))
    yield str(test_functions.test_all(module))
