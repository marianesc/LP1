#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#TROCA CHAVE

def troca_chave(dic):
    inverso = {}
    for key in dic.keys():
        inverso[dic[key]] = key
    return inverso
