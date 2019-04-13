
import random
import string

ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gerar_nome_aleatorio():
    string = ''
    for n in range(random.randint(5, 15)):
        string += random.choice(ASCII_LETTERS)
    return string

def gerar_email_aleatorio():
    return gerar_nome_aleatorio() + '@4linux.com'

def gerar_idade_aleatoria():
    return random.randint(24, 55)

def gerar_usuario_aleatorio():
    novo_usuario = {
        'nome': gerar_nome_aleatorio(),
        'email': gerar_email_aleatorio(),
        'idade': gerar_idade_aleatoria()
    }
    return novo_usuario

if __name__ == '__main__':
    usuario = gerar_usuario_aleatorio()
    print('Testando o usuário aleatório')
    print(usuario)