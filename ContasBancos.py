from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
        Cria um objeto ContaCorrente para gerenciar as contas dos clientes.
        
        Atributos: 
            nome (str): Nome do cliente
            cpf (str): cpf do cliente
            agencia (int): agencia responsavel pela conta do cliente
            conta (int): Número da conta corrente do cliente
            saldo (flt): saldo disponível na conta do ciente
            limite  (flt): limite de cheque especial do cliente
            transacoes (list): histórico de transações da conta do cliente
            cartoes (list): cartoes de credito usados na conta do clinte
    """
    
    
    @staticmethod
    def _data_hora():
        fuso_brasil = pytz.timezone('Brazil/East')
        horario_brasil = datetime.now(fuso_brasil)
        return horario_brasil.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, ag, cc):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self._agencia = ag
        self._conta = cc
        self.cartoes = []

    def consultar_saldo(self):
        # Faz a consulta do saldo atual da conta
        print(f'Seu saldo atual é de: R${self._saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        # Deposita o valor informado como parâmtro ao saldo da conta
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        print(f'Depósito realizado, saldo atual de R${self._saldo:,.2f}')

    def _limite_conta(self):
        #Define o limite de crédito da conta
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        # Retira o valor informado como parâmetro do saldo da conta
        # Primeiramente o método define que a pessoa não pode sacar mais do que o limite em que a conta pode chegar.
        if (self._saldo - valor) < self._limite_conta():
            print('Você não tem saldo o suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            print(f'Saque realizado, seu saldo atual é de R${self._saldo:,.2f}')

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque especial é de: R${self._limite_conta():,.2f}')

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        for transacao in self._transacoes:
            print(transacao)
            
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_brasil = pytz.timezone('Brazil/East')
        horario_brasil = datetime.now(fuso_brasil)
        return horario_brasil
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


# PROGRAMA

# Conta
print('='* 10 + ' CONTA ' + '='* 10)
conta_carlos = ContaCorrente('Carlos', '999.999.999-88', 1234, 29337)

print(f'''
Nome: {conta_carlos._nome}
CPF: {conta_carlos._cpf}
Agência: {conta_carlos._agencia}
Conta: {conta_carlos._conta}
''')

# Cartão
print('='* 10 + ' CARTÃO ' + '='* 10)
cartao_carlos = CartaoCredito('Fulano Ciclano de Beutrano', conta_carlos)

print(f'''
Titular: {cartao_carlos.titular}
Número do cartão : {cartao_carlos.numero}
Validade: {cartao_carlos.validade}
Código de segurança: {cartao_carlos.cod_seguranca}
Conta do cartão: {cartao_carlos.conta_corrente._agencia}-{cartao_carlos.conta_corrente._conta}
''')