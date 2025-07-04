#prog para demonstrar a implementação de pilha utilizando a coleção .deque

from collections import deque 

stack = deque()
# função .append() para inserir elementos na pilha

stack.append('Luis')
stack.append('Any')
stack.append('João')

print('pilha inicial: ')
print(stack)

#função para remover elementos da pilha na ordem LIFO(primeiro a entrar, ultimo a sair)
print('\nElementos removidos da pilha: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nPilha após retirada dos elementos:')
print(stack)