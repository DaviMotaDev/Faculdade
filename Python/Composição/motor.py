class Motor:
    
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print('Motor ligado')

    def desligar(self): 
        self.ligado = False