from datetime import datetime
import pytz
import time

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_brasil = pytz.timezone('Brazil/East')
        horario_brasil = datetime.now(fuso_brasil)
        return horario_brasil.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, ag, cc):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.transacoes = []
        self.agencia = ag
        self.conta = cc 

    def consultar_saldo(self):
        # Faz a consulta do saldo atual da conta
        print(f'Seu saldo atual é de: R${self.saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        # Deposita o valor informado como parâmtro ao saldo da conta
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        print(f'Depósito realizado, saldo atual de R${self.saldo:,.2f}')

    def _limite_conta(self):
        #Define o limite de crédito da conta
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        # Retira o valor informado como parâmetro do saldo da conta
        # Primeiramente o método define que a pessoa não pode sacar mais do que o limite em que a conta pode chegar.
        if (self.saldo - valor) < self._limite_conta():
            print('Você não tem saldo o suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
            print(f'Saque realizado, seu saldo atual é de R${self.saldo:,.2f}')

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque especial é de: R${self._limite_conta():,.2f}')

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        for transacao in self.transacoes:
            print(transacao)
            
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


# PROGRAMA
conta_carlos = ContaCorrente('Carlos', '999.999.999-88', 1234, 29337)

print(f'''
Nome: {conta_carlos.nome}
CPF: {conta_carlos.cpf}
Agência: {conta_carlos.agencia}
Conta: {conta_carlos.conta}
''')

conta_carlos.consultar_saldo()

# Depositando um dinheiro na conta
conta_carlos.depositar_dinheiro(10000)
time.sleep(4)

# Sacando um dinheiro na conta
# conta_carlos.sacar_dinheiro(10500)

# Checando cheque especial
conta_carlos.consultar_limite_chequeespecial()

# Criando outra conta para fazer o teste de transferência
conta_rwency = ContaCorrente('Rwency', '888.888.888-77', 5678, 96723)

# Transferindo dinheiro da conta_carlos para conta_rwency
conta_carlos.transferir(1000, conta_rwency)

# Exibindo histórico de transações da conta_carlos
print('-'*20)
conta_carlos.consultar_historico_transacoes()

#Exibindo histórico de transações da conta_rwency
print('-'*20)
conta_rwency.consultar_historico_transacoes()