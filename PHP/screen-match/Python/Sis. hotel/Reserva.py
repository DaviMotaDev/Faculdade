class Reserva:
    def __init__(self, hospede, quarto):      # cria uma reserva com um hóspede e um quarto
        self._hospede = hospede 
        self._quarto = quarto    

    def get_hospede(self):
        return self._hospede

    def get_quarto(self):
        return self._quarto

    def __str__(self):  # retorna uma string com o hóspede e o quarto
        return f"Reserva do hóspede {self._hospede.get_nome()} no quarto     {self._quarto._numero}"