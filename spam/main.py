
class EnviadorDeSpam:
    def __init__(self,sessao,conexao):
        self.conexao = conexao
        self.sessao = sessao

    def enviar_emails(self, address, subjetive, value):
        pass