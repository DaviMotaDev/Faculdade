class Conversion:

    # Construtor para inicializar as variáveis de classe
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # Essa matriz é usada como uma pilha
        self.array = []
        # Configuração de precedência
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Verificar se a pilha está vazia
    def isEmpty(self):
        return self.top == -1
    
    # Retorna o valor do topo da pilha
    def peek(self):
        return self.array[-1]
    
    # Remove o elemento da pilha
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    
    # Insere o elemento na pilha
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # Uma função utilizada para verificar se o caractere dado é operando
    def isOperand(self, ch):
        return ch.isalpha()
    
    # Verifica se a precedência do operador é estritamente menor que o topo da pilha ou não
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # A principal função que converte determinada expressão infix em expressão postfix
    def infixToPostfix(self, exp):
        # Iterar sobre a expressão para conversão
        for i in exp:
            # Se o caractere for um operador, adiciona à saída
            if self.isOperand(i):
                self.output.append(i)
            # Se o caractere for um '(', insere na pilha 
            elif i == '(':
                self.push(i)
            # Se o caractere for ')', retirar saída da pilha até que '(' seja encontrado
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)

        # Um operador é encontrado
        while not self.isEmpty():
            self.output.append(self.pop())
        
        return "".join(self.output)

# Programa de driver para testar a função acima
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
print(obj.infixToPostfix(exp))  # Deve exibir a expressão em notação postfix
