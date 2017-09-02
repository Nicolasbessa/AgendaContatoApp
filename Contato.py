from Telefone import Telefone
class Contato(Telefone):

    def __init__(self, pessoa):
        self.pessoa = pessoa

    def listarTelefone(self):