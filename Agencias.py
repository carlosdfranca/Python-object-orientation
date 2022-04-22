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
    pass

class AgenciaComum(Agencia):
    pass

class AgenciaPremium(Agencia):
    pass


# Programa

# Criando exemplo de agencia
agencia1 = Agencia(1144445555, 17128632000138, 1256)

# crinado exemplo de agencia virtual
agencia_virtual1 = AgenciaVirtual(1199998888, 12416954000169, 9876)

# Colocando um valor de caixa para a agencia_virtual1m e verificando 
agencia_virtual1.caixa = 15000
agencia_virtual1.verificar_caixa()

# Criando Agencia Premium
agencia_premium1 = AgenciaPremium(1199997777, 67366415000154, 7654)

# Colocando um valor de caixa para a agencia_premium1 e verificando
agencia_premium1.caixa = 100000000
agencia_premium1.verificar_caixa()