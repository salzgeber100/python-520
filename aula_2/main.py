
import json

import aleatorio as foo

def imprimir_bonito(obj):
    print(json.dumps(obj, indent=2))

def gerar_lista_usuarios(n):
    lista = []
    for i in range(n):
        u = foo.gerar_usuario_aleatorio()        
        lista.append(u)
    return lista

lista_de_usuarios = gerar_lista_usuarios(100)

lista_1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
lista_2 = [ x * 2 for x in lista_1 if x % 2 == 0 ]

def transformar(x):
    return x ** 2 + 4 * x - 3

filtrar = lambda x: x % 3 == 0 or x % 5 == 0

lista_3 = [ transformar(x) for x in lista_1 if filtrar(x) ]

def gerar_csv(lista):
    TEMPLATE = '{};{};{};'
    cabecalho = TEMPLATE.format('NOME', 'EMAIL', 'IDADE')
    print(cabecalho)
    for usuario in lista:
        usuario_formatado = TEMPLATE.format(
            usuario['nome'],
            usuario['email'],
            usuario['idade']
        )
        print(usuario_formatado)

def filtrar_usuarios(usuario):
    usuario_email = usuario['email'].lower()
    if 'd'in usuario_email or 'a' in usuario_email:
        return True
    return False

# mais eficiente
gerar_csv(u for u in lista_de_usuarios if filtrar_usuarios(u))

# menos eficiente
lista_de_usuarios_filtrada = [ 
    u for u in lista_de_usuarios if filtrar_usuarios(u) 
]
gerar_csv(lista_de_usuarios_filtrada)

# 1 - Imprimam somente os usuários com mais de 30 anos
# 2 - Filtrem somente pelos emails que contém 'a' ou 'd' 
#       e imprimam um arquivo 'relatorio.csv' separado por ;
