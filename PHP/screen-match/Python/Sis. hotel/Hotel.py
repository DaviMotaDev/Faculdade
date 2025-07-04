class Hotel:

    def __init__(self): # função para criar 3 listas
        self._quartos = []
        self._hospedes = []
        self._reservas = []

    def add_quarto(self, quarto):  # adiciona um quarto a lista do hotel
        self._quartos.append(quarto)

    def remover_quarto(self, quarto):  # remove um quarto da lista do hotel
        if quarto in self._quartos:
            self._quartos.remove(quarto)

    def registrar_hospede(self, hospede):   # adiciona um hospede a lista do hotel
        if hospede not in self._hospedes:
            self._hospedes.append(hospede)

    def cancelar_reserva(self, reserva):   # cancela uma reserva da lista do hotel
        if reserva in self._reservas:
            reserva._quarto.liberar()
            self._reservas.remove(reserva)

    def listar_quartos(self):   # lista os quartos do hotel
        for quarto in self._quartos:
            print(quarto)
