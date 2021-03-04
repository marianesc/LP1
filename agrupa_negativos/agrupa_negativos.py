def agrupa_negativos(lista):
    dic = {"nao-negativos":[], "negativos":[]}
    for e in lista:
        if e < 0:
            dic["negativos"].append(e)
        else:
            dic["nao-negativos"].append(e)

    return dic

