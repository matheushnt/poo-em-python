print('PASSANDO PARÂMETROS NO MÉTODO CONSTRUTOR'.center(50, '-'))


class Carro:
    def __init__(self, marca, nome, ano):
        self.marca = marca
        self.nome = nome
        self.ano = ano

    def ligar(self):
        print('O carro foi ligado')

    def desligar(self):
        print('O carro foi desligado')

    def tocar_musica(self, msc):
        print(f'Tocando a música: {msc}')

    def abrir_porta_malas(self):
        print('O porta-malas foi aberto')


# Instâncias criadas
carro1 = Carro(marca='Toyota', nome='Yaris', ano=2024)
carro2 = Carro(marca='Chevrolet', nome='Onix', ano=2023)
carro3 = Carro(marca='Fiat', nome='Argo', ano=2022)

carro1.ligar()
carro2.ligar()
carro3.ligar()
carro1.tocar_musica('Honda')
carro2.abrir_porta_malas()
carro3.desligar()
