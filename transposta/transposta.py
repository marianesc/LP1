#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#TRANSPOSTA

def transposta(M):
    T = []
    for i in range(len(M[0])):
        T.append([])
        for j in range(len(M)):
            T[i].append(M[j][i])

    return T

