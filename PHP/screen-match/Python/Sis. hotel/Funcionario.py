from Pessoa import Pessoa  # Importando a classe Pessoa

class Funcionario(Pessoa):  # Criando a classe Funcionario que herda da classe Pessoa
    def add_quarto(self, hotel, quarto):
        hotel.add_quarto(quarto)

    def remover_quarto(self, hotel, quarto): 
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel, hospede):
        hotel.registrar_hospede(hospede)

    def cancelar_reserva(self, hotel, reserva):
        hotel.cancelar_reserva(reserva)
