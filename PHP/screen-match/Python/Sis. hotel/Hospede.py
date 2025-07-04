from Pessoa import Pessoa

class Hospede(Pessoa):

    def __init__(self, nome, email, id):   # Construtor da classe Hospede
        super().__init__(nome, email, id)  
        self._reservas = []

    def fazer_reserva(self, reserva):       # faz uma reserva
        self._reservas.append(reserva)

    def cancelar_reserva(self, reserva):    # cancela uma reserva
        if reserva in self._reservas:
            self._reservas.remove(reserva)

    def consultar_reserva(self):   # consulta as reservas
        return self._reservas