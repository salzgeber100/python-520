
import random
import string
import json
usuarios = []

def random_string(a, b):
    return ''.join(random.choices(string.ascii_letters, k=random.randint(10,20)))
    
for n in range(20):
    usuarios.append({
        'nome': random_string(10, 20),
        'idade': random.randint(20, 50),
        'email': random_string(5, 10) + '@4linux.com',
        'sexo': random.choice([ 'M', 'F', '?' ]),
        'endereco': 'Rua ' + random_string(30, 50)
    })

print(json.dumps(usuarios, indent=2))

exit()

usuario = {
    'nome': input('Digite seu nome: '),
    'idade': input('Digite sua idade: '),
    'email': input('Digite seu email: '),
}

nome = usuario['nome']
print('Usuário {} cadastrado com sucesso !'.format(usuario))


exit()

print(usuario)
print(type(usuario))

print(usuario['nome'])
print(type(usuario['nome']))

print(usuario['idade'])
print(type(usuario['idade']))

exit()

# nomes de varíaveis

GRAVIDADE = 9.8

primeiro_nome = 'Lucas'
segundo_nome = 'Ricciardi'
ultimo_nome = 'de Salles'

idade = '25'
idade = 25

professor = True

variavel = 'string'
print(type(variavel))
variavel = 121
print(type(variavel))
variavel = True
print(type(variavel))

exit()

print('hello, world')

condicao = 'Lucas Ricciardi de Salles'
print(type(condicao))
condicao = 25
print(type(condicao))
condicao = True
print(type(condicao))

if condicao:
    print('verdade')
else:
    erro