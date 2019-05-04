
def par(x):
    if x % 2 == 0:
        return True
    return False

def gerar_lista_numeros_pares(numero):
    return [ (i + 1) for i in range(numero) if par(i + 1) ]

lista_de_numeros_pares = gerar_lista_numeros_pares(5)
for numero in lista_de_numeros_pares:
    if not par(numero):
        raise Exception('{} não é um número par'.format(numero))

print(lista_de_numeros_pares)

# revisão rápida
# escrever uma função que recebe 
# um número inteiro e retorna uma lista
# com todos os números menores ou iguais à esse
# menos o zero
# ex: gerar_lista(5) -> [ 1, 2, 3, 4, 5 ]
#     gerar_lista(9) -> [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

exit()

# 1
def gerar_lista(numero):
    lista, x = [], 1
    while x <= numero:
        lista.append(x)
        x = x + 1           # x += 1 
    return lista

# 2
def gerar_lista(numero):
    lista = []
    for i in range(numero):
        lista.append(i + 1)
    return lista

# 3
def gerar_lista(numero):
    return [ i + 1 for i in range(numero) ]

gerar_lista = lambda n: [ i + 1 for i in range(n) ]



