#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#ROTAÇÃO DA DIAGONAL SECUNDARIA

def rotaciona_ds(matriz, sentido):
    if sentido == 'cima':
        aux = 1
        for ilin in range(len(matriz)):
            matriz[ilin][len(matriz) - aux], matriz[ilin + 1][len(matriz) - aux - 1] = matriz[ilin + 1][len(matriz) - aux - 1], matriz[ilin][len(matriz) - aux]
            aux += 1
            if ilin == len(matriz) - 2:
                break


    elif sentido == 'baixo':
        aux = 0
        for ilin in range(len(matriz) - 1, -1, -1):
            matriz[ilin][aux], matriz[ilin - 1][aux + 1] = matriz[ilin - 1][aux + 1], matriz[ilin][aux]
            aux += 1
            if ilin == 1:
                break

