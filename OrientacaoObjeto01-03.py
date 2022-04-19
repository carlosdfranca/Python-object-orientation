# Criando nossa primeira classe com Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class = Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem difine o que acontece quando você cria uma instância de uma classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente ja havia comentado

# CLASSE
class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligado = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10

    #MÉTODOS
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f'Canal alterado para {self.canal}')

# PRGRAMA
# Criando instâncias da classe TV
tv_sala = TV()
tv_quarto = TV()

# Modificando o atributo "cor" da instância "tv_sala"
tv_sala.cor = 'branca'

print(f'Cor da tv da sala: {tv_sala.cor}')
print(f'Cor da tv do quarto: {tv_quarto.cor}')
print('=-'*30)

# Modificando o atributo tamanho da instancia "tv_quarto"
tv_quarto.tamanho = 32

print(f'Tamanho da tv da sala: {tv_sala.tamanho}')
print(f'Tamanho da tv do quarto {tv_quarto.tamanho}')
print('=-'*30)

# Usando o método "mudar_canal"
tv_sala.mudar_canal(input('Qual canal você gostaria? '))

print(f'Canal da tv da sala: {tv_sala.canal}')
print(f'Canal da tv do quarto: {tv_quarto.canal}')
print('=-'*30)