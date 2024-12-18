from pagamento import Pagamento

class Boleto(Pagamento):
    def processar_pagamento(self, valor):
        #algoritmo para processar boleto
        print(f'Processando pagamento de {valor} com boleto')