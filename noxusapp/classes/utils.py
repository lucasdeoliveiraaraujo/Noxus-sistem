def nvl(valor: str, retorno: str):
    if valor == "" or valor == "None":
        return retorno
    else:
        return valor
