#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#RESUMOS IGUAIS

def agrupa_resumos_iguais(lista):
    dic = {}
    for numero in lista:
        soma = 0
        for e in str(numero):
            soma += int(e)

        if soma not in dic.keys():
            dic[soma] = [numero]
        else:
            dic[soma].append(numero)

    return dic

