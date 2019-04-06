ista_populada = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
lista_vazia = []

# Para inserir elementos em uma lista
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append(4)
lista_vazia.append(5)
lista_vazia.append(6)
lista_vazia.append(7)
lista_vazia.append(8)
lista_vazia.append(9)
lista_vazia.append(10)

print(lista_populada)
print(lista_vazia)

# Primeiro elemento
print(lista_vazia[0])

lista_populada = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Imprimir APENAS O QUINTO ELEMENTO da lista_vazia
for n in lista_vazia:
    print('Imprimindo o número ' + str(n))

for i in range(10):
    pass

# Exercício:
# Escreva um programa que cadastre 10 
# usuários
# e salve eles em uma lista.
# Após os 10 serem cadastrados, exiba
# o nome dos usuários cadastrados

# Para os mais **apressadinhos**

# Alterar o programa para:
# 1- Perguntar se o usuário quer finalizar o programa (
#      o usuário irá digitar uma opção entre (s/n)
# )
# Utilizar a função ''.format() para criar um menu de opções
# As opções devem conter:
# 1- Cadastrar novo usuário
# 2- Listar usuário existentes
# 3- (Só para quem é vida loka) buscar e deletar um usuário

# Resolução

lista_de_usuarios = []

for i in range(10):
    usuario = {
        'nome': input('Digite seu nome: '),
        'idade': input('Digite sua idade: '),
        'email': input('Digite seu email: '),
    }
    lista_de_usuarios.append(usuario)

tamanho_da_lista = len(lista_de_usuarios)
for i in range(tamanho_da_lista):
    print(lista_de_usuarios[i]['nome'])

for usuario in lista_de_usuarios:
    print(usuario['nome'])

dontpad.com/python-520