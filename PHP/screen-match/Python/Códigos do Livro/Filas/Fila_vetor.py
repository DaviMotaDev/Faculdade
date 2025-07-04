class Fila:
    # cria uma fila 
    def __init__(self):
        self._items = list()
    # se a fila estiver vazia retorna True, senão retorna False.
    def estaVazia(self):
        return len(self) == 0 
    # retorna os elementos que estiver na fila.
    def __len__(self):
        return len(self._items)
    # insere elementos à fila    .
    def enfilera(self, item):
        self._items.append(item)
    # remove e retorna o primeiro elemento da fila.
    def desenfileira(self):
        assert not self.estaVazia(), "Fila vazia!"
        return self._items.pop(0)
