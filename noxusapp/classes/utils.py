def nvl(valor: str, retorno: str):
    if valor == "" or valor == "None":
        return retorno
    else:
        return valor
def gerarUsuario(nomePessoa):
    import unicodedata
    import random
    nome = nomePessoa.split()
    if(random.randint(1, 2) == 1):
        print(nome)
        inicial = random.randint(0,len(nome) - 1)
        termino = random.randint(0, len(nome) - 1)
        tentativas = 0
        while (inicial == termino and len(nome[termino]) > 2) or tentativas == 5:
            tentativas += 1
            termino = random.randint(0, len(nome) - 1)
        print(str(inicial)+"|"+str(termino))
        usuario = str(nome[inicial][0] + nome[termino]).upper()
    else:
        usuario = f"{nome[0]}.{nome[1]}.{nome[2]}".upper()

    usuario = ''.join(ch for ch in unicodedata.normalize('NFKD', usuario) if not unicodedata.combining(ch))
    return usuario