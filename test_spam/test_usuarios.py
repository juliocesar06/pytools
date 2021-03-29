class Usuario(object):
    def __init__(self,nome):
        self.nome = nome
        self.id = None


def test_salvar_usuario(conexao,sessao):
    usuario = Usuario(nome='Julio')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)




def test_listar_usuario(conexao,sessao):
    usuarios = [Usuario(nome='Julio'),Usuario(nome='King')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



