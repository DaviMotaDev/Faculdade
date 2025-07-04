from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass
    
    def validar_pagamento(self, valor):
        if valor > 0:
            print('Pagamento válido')
        else:
            print('Valor inválido')
