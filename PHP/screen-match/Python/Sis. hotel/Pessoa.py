class Pessoa:

    def __init__(self, nome, email, id):  # Construtor da classe Pessoa
        self._nome = nome
        self._email = email
        self._id = id
        
    def get_id(self):    # Método para obter o ID, email e nome da pessoa
        return self._id
    
    def get_email(self):
        return self._email
    
    def get_nome(self):
        return self._nome