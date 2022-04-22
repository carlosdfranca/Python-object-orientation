from random import randint


class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R${:,.2f}'.format(self.caixa))
        else:
            print('O valor de caixa está OK. Caixa atual: R${:,.2f}'.format(self.caixa))
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            self.caixa = self.caixa - valor
            print('Empréstimo efutuado! Caixa atual: R${:,.2f}'.format(self.caixa))
        else:
            print('Não foi possivel realizar o emprestimo pela falta do valor em caixa. Caixa atual: R${:,.2f}'.format(self.caixa))
            
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0
        
    def depositar_paypal(self, valor):
        if valor <= self.caixa:
            self.caixa -= valor
            self.caixa_paypal += valor
            print(f'Depósito realizado. \nCaixa atual: R${self.caixa:,.2f} \nCaixa atual do Paypal: R${self.caixa_paypal:,.2f}')
        else:
            print('Ops... Não tem dinheiro em caixa suficiente para o depósito. \nCaixa atual: R${:,.2f}'.format(self.caixa))
    
    def sacar_paypal(self, valor):
        if valor <= self.caixa_paypal:
            self.caixa_paypal -= valor
            self.caixa += valor
            print(f'Saque realizado. \nCaixa atual: R${self.caixa:,.2f} \nCaixa atual do Paypal: R${self.caixa_paypal:,.2f}')
        else:
            print('Ops... Não tem dinheiro no Paypal suficiente para o saque. \nCaixa atual do Paypal: R${:,.2f}'.format(self.caixa_paypal))
    

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001, 9999))
        self.caixa = 10000000
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >= 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
            print(f'{nome} foi adicionado a lista de clientes')
        else:
            print('O cliente não tem o patrimônio mínimo para entrar na Agencia Premium')



if __name__ == '__main__':
    # Criando exemplo de agencia
    agencia1 = Agencia(1144445555, 17128632000138, 1256)

    # Crinado exemplo de agencia virtual
    agencia_virtual1 = AgenciaVirtual('www.meusitevirtual.com.br', 1199998888, 97734477000132)

    # Colocando um valor de caixa para a agencia_virtual1m e verificando 
    print('-'*10 + 'AGENCIA VIRTUAL' + '='* 10 )
    agencia_virtual1.verificar_caixa()

    # Depositando para o Paypal
    agencia_virtual1.depositar_paypal(50000)

    # Sacando do Paypal
    agencia_virtual1.sacar_paypal(25000)


    # Criando exemplo de Agencia Comum
    agencia_comum = AgenciaComum(1177776666, 87203559000105)


    # Criando ecemplo de Agencia Premium
    agencia_premium = AgenciaPremium(1177776666, 87203559000105)
    agencia_premium.adicionar_cliente('Carlos', 12345678945, 500000000)
    print(agencia_premium.clientes)