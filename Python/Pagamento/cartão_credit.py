from pagamento import Pagamento

class CartaoCredito(Pagamento):
    def processar_pagamento(self, valor):
        #Algoritmo para pagamento com cartão
        print(f'Processando pagamento de {valor} com cartão de crédito')