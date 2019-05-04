
import datetime

'''
    Quando o usuário passar um ticket válido na catraca,
    a catraca deve liberar e o preço da passagem deve ser
    descontado do saldo do ticket. Um ticket válido
    é um ticket que está dentro do prazo de validade, 
    tem saldo suficiente para pagar a passagem e pertence
    à mesma concessionária da catraca.
'''

########################################################################
# Constantes
########################################################################

PRECO_DA_PASSAGEM = 20000.00

########################################################################
# Erros
########################################################################

class ErroTicketExpirado(Exception):
    pass

class ErroConcessionariaDiferente(Exception):
    pass

class ErroSaldoInsuficiente(Exception):
    pass

########################################################################
# Classes
########################################################################

class Ticket:

    def __init__(self, validade, saldo, concessionaria):
        self.validade = validade
        self.saldo = saldo
        self.concessionaria = concessionaria

class Catraca:

    def __init__(self, concessionaria):
        self.concessionaria = concessionaria
        self.estado = 'travada'

    def esta_liberada(self):
        if self.estado == 'liberada':
            return True
        return False

    def liberar(self, ticket):
        
        if ticket.validade < datetime.datetime.now():
            raise ErroTicketExpirado

        if ticket.saldo < PRECO_DA_PASSAGEM:
            raise ErroSaldoInsuficiente

        if ticket.concessionaria != self.concessionaria:
            raise ErroConcessionariaDiferente

        ticket.saldo = ticket.saldo - PRECO_DA_PASSAGEM
        self.estado = 'liberada'

########################################################################
# Testes
########################################################################

# Teste de ticket vencido

try:

    validade = datetime.datetime.now() - datetime.timedelta(days=2)
    saldo = PRECO_DA_PASSAGEM + 300.00
    concessionaria = 'sptrans'

    ticket = Ticket(validade, saldo, concessionaria)

    catraca = Catraca(concessionaria='sptrans')

    catraca.liberar(ticket)

    print('BUG ENCONTRADO')

except ErroTicketExpirado:
    print('Teste de ticket expirado ok')

# Teste de concessionário diferente

try:

    validade = datetime.datetime.now() + datetime.timedelta(days=365)
    saldo = PRECO_DA_PASSAGEM + 300.00
    concessionaria = 'emtu'

    ticket = Ticket(validade, saldo, concessionaria)

    catraca = Catraca(concessionaria='sptrans')

    catraca.liberar(ticket)

    print('BUG ENCONTRADO')
    
except ErroConcessionariaDiferente:
    print('Teste de concessionária diferente ok')

# Teste de saldo insuficiente

try:

    validade = datetime.datetime.now() + datetime.timedelta(days=365)
    saldo = PRECO_DA_PASSAGEM - 1.00
    concessionaria = 'sptrans'

    ticket = Ticket(validade, saldo, concessionaria)

    catraca = Catraca(concessionaria='sptrans')

    catraca.liberar(ticket)

    print('BUG ENCONTRADO')
    
except ErroSaldoInsuficiente:
    print('Teste de saldo insuficiente ok')

# teste de catraca liberada


validade = datetime.datetime.now() + datetime.timedelta(days=365)
saldo = PRECO_DA_PASSAGEM + 1.00
concessionaria = 'sptrans'

ticket = Ticket(validade, saldo, concessionaria)

catraca = Catraca(concessionaria='sptrans')

catraca.liberar(ticket)

try:

    assert ticket.saldo == (saldo - PRECO_DA_PASSAGEM)
    assert catraca.esta_liberada()

    print('teste de fluxo feliz ok')

except:
    print('BUG ENCONTRADO')
