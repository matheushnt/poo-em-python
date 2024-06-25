class Cofre:
    def __init__(self, senha):
        self.__senha = senha
        self.__aberto = False

    def __validar_senha(self, senha):
        if senha == self.__senha:
            self.__aberto = True
            return self.__senha

    def abrir(self, senha):
        if self.__validar_senha(senha):
            print('O cofre foi aberto')
        else:
            print('Senha incorreta')

    def fechar(self):
        self.__aberto = False
        print('O cofre foi fechado')

    def status(self):
        return 'Aberto' if self.__aberto else 'Fechado'


if __name__ == '__main__':
    cofre = Cofre(1806)
    cofre.abrir(2019)
    cofre.abrir(1806)
    print(cofre.status())
    cofre.fechar()
    print(cofre.status())
