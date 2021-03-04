#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#ROTEIROS AEROPORTOS

def eh_roteiro(iata, voos, roteiro):
    roteiros = roteiro.split('/')
    for i in range(len(roteiros) - 1):
        possivel = False
        if iata[roteiros[i + 1]] in voos[iata[roteiros[i]]]:
            possivel = True
        else: break

    return possivel

