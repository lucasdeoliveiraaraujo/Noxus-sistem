def nvl(valor: str, retorno: str):
    if valor == "" or valor == "None":
        return retorno
    else:
        return valor


def gerarUsuario(nomePessoa, usuarioexiste: bool = False):
    import unicodedata
    import random
    nome = nomePessoa.split()
    if random.randint(1, 2) == 1:
        inicial = random.randint(0, len(nome) - 1)
        termino = random.randint(0, len(nome) - 1)
        tentativas = 0
        while (inicial == termino and len(nome[termino]) > 2) or tentativas == 5:
            tentativas += 1
            termino = random.randint(0, len(nome) - 1)

        usuario = str(nome[inicial][0] + nome[termino]).upper()
    else:
        usuario = ""
        for idx, dados in enumerate(nome):
            usuario = dados + "." + usuario
        usuario = str(usuario.upper().strip())[0:len(usuario) - 1]

    if usuarioexiste:
        usuario = usuario + str(random.randint(0, 9999999))
    usuario = ''.join(ch for ch in unicodedata.normalize('NFKD', usuario) if not unicodedata.combining(ch))
    return usuario
