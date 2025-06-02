import sys
import os
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
import app 

def test_home():
    assert app.home() == 'Bem-vindo à API de tarefas!'
