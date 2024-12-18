class Quarto:
    def __init__(self, numero, tipo, disponivel=True):   # cria um quarto com um número, tipo e disponibilidade
        self._numero = numero
        self._tipo = tipo
        self._disponivel = disponivel

    def reservar(self):
        self._disponivel = False

    def liberar(self):
        self._disponivel = True

    def esta_disponivel(self):
        return self._disponivel

    def __str__(self):      # retorna uma string com o número e o tipo do quarto
        return f"Quarto {self._numero} - Tipo: {self._tipo} - {'Disponível' if self._disponivel else 'Reservado'}"