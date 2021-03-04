#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SOMA LINHA E COLUNA

def soma_linha_e_coluna(matriz,l,c):
    soma = 0
    for ilin in range(len(matriz)):
        soma += matriz[ilin][c]
    for icol in range(len(matriz[0])):
        soma += matriz[l][icol]

    soma -= (2 * matriz[l][c])
    return soma

