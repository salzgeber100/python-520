
import os
import subprocess
import datetime
import time
import random

def cadastrar_usuario():
    novo_usuario = {
        'data_cadastro': datetime.datetime.now(),
        'nome': input('Digite seu nome: '),
        'email': input('Digite seu email: '),
        'idade': input('Digite sua idade: '),        
    }
    return novo_usuario
