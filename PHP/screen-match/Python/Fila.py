fila = []

def enfileirar(item):
    fila.append(item)
    print(f"{item} entrou na fila")
    print("fila atual:", fila)

def desenfileirar():
    if fila: 
        item = fila.pop(0)
        print(f"{item}, saiu da fila")
        print("fila atual", fila)
    else:
        print("fila está vazia")

while True:
    print("\nMenu:")
    print("1. Adicionar número à fila.")
    print("2. Mostrar a fila.")
    print("3. Excluir número da fila.")
    print("4. Sair.")

    escolha = input("\nescolha uma opção: ")
    
    if escolha == "1":
        item = input("\nDigite o número a ser enfileirado:")
        enfileirar(item)

    elif escolha == "2":   
        print("\n fila atual: ", fila)
    
    elif escolha == "3":
         desenfileirar()

    elif escolha == "4":
        print("\n programa encerrado.")
        break

    else:
        print("opção inválida tente novamente.")