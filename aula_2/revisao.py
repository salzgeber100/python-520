
lista_de_gatos = [

    {
        'nome': 'gato',
        'peso': 5000,
        'idade': 6,
        'apelido': 'sedoso', 
    },

    {
        'nome': 'fernando',
        'peso': 3750,
        'idade': 3,
        'apelido': 'brilhoso'
    }
]

'''
def get_input_as_int(mensagem):
    user_input = input(mensagem)
    for token in user_input:
        print('Caracter atual: {}'.format(token))
        if token not in '0123456789':
            print('Caracter invalido encontrado')
            print('Encerrando o algoritmo com erro')
            return -1
    print('Algoritmo executado com sucesso !')
    return int(user_input)
'''

def get_input_as_int(mensagem, erro):
    user_input = input(mensagem)
    try:
        return int(user_input)
    except ValueError:
        raise ValueError(erro)

def tratamento_de_tentativas(numero_tentativas, mensagem, erro):
    for tentativa in range(numero_tentativas):
        try:
            return get_input_as_int(mensagem, erro)
        except ValueError as err:
            restantes = numero_tentativas - (tentativa + 1)
            print('Um erro aconteceu, Você ainda tem {} tentativas'.format(restantes))
            print(err)
    print('Você errou o input {} vezes.'.format(numero_tentativas))
    print('Vou encerrar o programa')
    exit()

novo_gato = {
    'nome': input('Digite o nome: '),
    'peso': tratamento_de_tentativas(
        5, 'Digite o peso: ', 'O peso deve ser um número maior que 0'
    ),
    'idade': tratamento_de_tentativas(
        3, 'Digite a idade: ', 'A idade deve ser um número maior que 10'
    ),
    'apelido': input('Digite o apelido: ')
}
lista_de_gatos.append(novo_gato)

for gato in lista_de_gatos:
    print('Peso do gato: {}'.format(gato['peso']))
    if gato['peso'] > 4000:
        print('Esse é o gato')
    else:
        print('Ela é a Malawi')

exit()

# teste de sanidade do interpretador
print('hello, world')