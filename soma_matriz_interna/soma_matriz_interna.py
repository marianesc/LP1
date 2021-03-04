#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SOMA MATRIZ INTERNA

def soma_matriz_interna(matriz, inicio, fim):
    soma = 0
    for ilin in range(inicio[0], fim[0] + 1):
        for icol in range(inicio[1], fim[1] + 1):
            soma += matriz[ilin][icol]

    return soma

