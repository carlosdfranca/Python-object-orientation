nome = 'Carlos'
print(type(nome))  # O objeto "nome" é um objeto da classe "string" como aparece no Print
print(nome.capitalize())  # O MÉTODO é uma função dentro de uma classe, então, o método "capitalize" vai fazer uma ação no objeto "nome"


# Crinado uma Classe:
class TV():
    #Atributos:
    cor = 'preta'
    tamanho = 55
    canal = 10
    volume = 50

    #Métodos:
    def mudar_canal(self):
        pass

    def mudar_volume(self):
        pass

    def ligar_desligar(self):
        pass