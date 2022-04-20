from datetime import datetime
import pytz
import time

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
        self._cartoes = []

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
    
    def __init__(self, titular, conta_corrente):
        self.numero = 123456
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)


# PROGRAMA
conta_carlos = ContaCorrente('Carlos', '999.999.999-88', 1234, 29337)

print(f'''
Nome: {conta_carlos._nome}
CPF: {conta_carlos._cpf}
Agência: {conta_carlos._agencia}
Conta: {conta_carlos._conta}
''')

cartao_carlos = CartaoCredito('Fulano Ciclano de Beutrano', conta_carlos)

print(cartao_carlos.titular , '|' , cartao_carlos.conta_corrente._conta)