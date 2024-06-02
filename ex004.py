print('PASSANDO PARÂMETROS EM MÉTODOS'.center(45, '='))


class TV:
    # Método construtor
    def __init__(self):
        self.ligada = False
        self.canal = 'Globo'
        self.volume = 10

    def ligar(self):
        self.ligada = True
        print('TV foi ligada')

    def desligar(self):
        self.ligada = False
        print('TV foi desligada')

    def aumentar_volume(self, num_volume: int):
        self.volume = num_volume
        print(f'Volume aumentado para {num_volume}')

    def diminuir_volume(self, num_volume: int):
        self.volume = num_volume
        print(f'Volume diminuido para {num_volume}')

    def mudar_canal(self, canal: str):
        self.canal = canal
        print(f'Você trocou para o canal: {canal}')


tv_quarto = TV()
tv_quarto.ligar()
tv_quarto.mudar_canal('SBT')
tv_quarto.aumentar_volume(15)
tv_quarto.diminuir_volume(12)
tv_quarto.mudar_canal('Globo')
print(tv_quarto.canal)
print(tv_quarto.ligada)
tv_quarto.desligar()
print(tv_quarto.ligada)
