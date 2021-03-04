#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#BUSCA EM MATRIZ

def busca_matriz(m, e):
    para = False
    for ilin in range(len(m)):
        for icol in range(len(m[0])):
            if e == m[ilin][icol]:
                return (ilin, icol)
                para = True
                break
        if para: break

