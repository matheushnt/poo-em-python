print('ATRIBUTOS DE CLASSE'.center(45, '='))


class TV:
    # Atributo da Classe
    cor = 'Preto Ouro Negro'

    # Atributos da Instância
    def __init__(self, marca, tamanho, definicao):
        self.marca = marca
        self.tamanho = tamanho
        self.definicao = definicao

    # Métodos
    def ligar(self):
        print('A TV foi ligada')

    def desligar(self):
        print('A TV foi desligada')

    def mudar_canal(self, canal):
        print(f'Canal alterado para {canal}')


tv_quarto = TV(marca='Samsung', tamanho=55, definicao='4K')
tv_sala = TV(marca='LG', tamanho=60, definicao='4K')

tv_sala.ligar()
tv_sala.mudar_canal('Netflix')
tv_quarto.ligar()
tv_quarto.mudar_canal('Disney+')

print(f'Cor da TV da Sala: {tv_sala.cor}')
print(f'Cor da TV do quarto: {tv_quarto.cor}')

# Alterando o Atributo da Classe
TV.cor = 'Cinza'    # Não é recomendado fazer essa alteração

print(f'Cor da TV da Sala: {tv_sala.cor}')
print(f'Cor da TV do quarto: {tv_quarto.cor}')

"""
OBS: Quando um atributo é alterado com frequência, o ideal é ser definido como
um Atributo de Instância. Mas se um Atributo é comum para todas as Instâncias
criadas a partir de uma mesma Classe, é recomendado ser definido como um
Atributo de Classe.
"""
