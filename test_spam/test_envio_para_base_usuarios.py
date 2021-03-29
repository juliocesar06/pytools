from spam.enviador_de_email import Enviador
from spam.main import EnviadorDeSpam



def test_envio_de_spam(sessao):
    envio_de_spam =  EnviadorDeSpam(sessao, Enviador)
    envio_de_spam.enviar_emails(
        'julio@gmail.com',
        'new work python',
        '15000',
    )