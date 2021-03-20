import requests


def buscar_user(usuario):

    """
    :param usuario: Buscar usuario no GitHub
    :param usuario: str com nome do usuário
    :return: str com link avatar
    """
    url = f'https://api.github.com/users/{usuario}'

    resp = requests.get(url)

    return resp.json()['avatar_url']


if __name__ == '__main__':

    nome = input('nome do usuario...:')
    print(buscar_user(nome))
hjdhfjhdskjfhkdjs