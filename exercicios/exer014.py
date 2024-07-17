from datetime import datetime
import pytz


class Pagamento:
    def __init__(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
