class FilaListaEncadeada:
    # Cria uma fila vazia, utilizando a estrutura de uma lista encadeada
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._contador = 0

    # Se a fila estiver vazia retorna True, senão retorna False
    def estaVazia(self):
        return self._inicio is None
    
    # Retorna quantos elementos tem na fila
    def __len__(self):
        return self._contador

    # Insere um elemento na fila
    def enfilera(self, item):
        elemento = self._NoFila(item)
        if self.estaVazia():
            self._inicio = elemento
        else:
            self._fim.next = elemento
        self._fim = elemento
        self._contador += 1
    
    # Remove e retorna o primeiro elemento da fila 
    def desenfileira(self):
        assert not self.estaVazia(), "Fila vazia!"
        elemento = self._inicio 
        if self._inicio is self._fim: 
            self._fim = None
        self._inicio = self._inicio.next
        self._contador -= 1
        return elemento.item

    # Classe privada para armazenamento de nós da lista encadeada
    class _NoFila:
        def __init__(self, item):
            self.item = item
            self.next = None
