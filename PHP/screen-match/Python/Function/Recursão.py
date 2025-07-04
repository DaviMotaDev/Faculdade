def fatorial(numero):

    if numero == 0: #caso base ou condição de parada
        return 1
    else:
        return numero * fatorial(numero -1) # caso recursivo

print(fatorial(10))
