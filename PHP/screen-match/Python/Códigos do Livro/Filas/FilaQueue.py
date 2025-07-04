f = Fila() # type: ignore
print(list(f._items))    #[]
print(list(f,estaVazia())) #type: ignore | True
f.enfileira(34)
print(list(f._items)) #[34]
f.enfileira(26)
print(list(f._items)) #[34, 26]
f.estaVazia()
f.enfileira(44) # [34, 26, 44]
print(list(f._items))
f.desenfilera()
print(list(f._items)) # [26, 44]
f.enfileira(55)
print(list(f._items)) # [26, 44, 55]
print(f.__len__()) # 3 (itens na fila)
f.enfileira(73)
print(list(f._items)) # [26, 44, 55, 73]
