#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#MATRIZ MENOR

def matriz_menor(mat1, mat2):
    Mr = []
    for ilin in range(len(mat1)):
        Mr.append([])
        for icol in range(len(mat1[0])):
                if mat1[ilin][icol] <= mat2[ilin][icol]:
                    Mr[ilin].append(mat1[ilin][icol])
                else:
                    Mr[ilin].append(mat2[ilin][icol])
    return Mr

