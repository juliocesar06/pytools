import pytest

from spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
                        'remetente',
                         ['juliogmail.com','leandro_gmail.com']
    )
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'leandro@gmail.com',
            'Cursos PythonPro',
            'Primeira Turma de Python.',
        )
