from ContasBancos import ContaCorrente, CartaoCredito


# Conta
print('='* 10 + ' CONTA ' + '='* 10)
conta_carlos = ContaCorrente('Carlos', '999.999.999-88', 1234, 29337)

print(f'''
Nome: {conta_carlos.nome}
CPF: {conta_carlos.cpf}
Agência: {conta_carlos.agencia}
Conta: {conta_carlos.conta}
''')

# Cartão
print('='* 10 + ' CARTÃO ' + '='* 10)
cartao_carlos = CartaoCredito('Fulano Ciclano de Beutrano', conta_carlos)

print(f'''
Titular: {cartao_carlos.titular}
Número do cartão : {cartao_carlos.numero}
Validade: {cartao_carlos.validade}
Código de segurança: {cartao_carlos.cod_seguranca}
Conta do cartão: {cartao_carlos.conta_corrente.agencia}-{cartao_carlos.conta_corrente.conta}
''')

cartao_carlos.senha = '1235'
print(cartao_carlos.senha)