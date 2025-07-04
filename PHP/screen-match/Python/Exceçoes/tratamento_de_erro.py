try: 
    x = int(input("Digite um número: "))
    resultado = 10 / x 
    print(f"O resultado é {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError: 
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
finally:
    print("Fim do processo.")
