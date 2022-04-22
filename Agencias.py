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


# Programa

# Criando exemplo de agencia
agencia1 = Agencia(1144445555, 9809809809879, 1256)

# Alterando o valor do dinheiro em caixa
agencia1.caixa = 1000000

# Verificando o dinheiro em caixa
agencia1.verificar_caixa()

# Emprestando dinheiro
agencia1.emprestar_dinheiro(1500, 12345678945, 0.10)

# Adicionancdo um cliente
agencia1.adicionar_cliente('Carlos', 12345678945, 10000)
print(agencia1.clientes)