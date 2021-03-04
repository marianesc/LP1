#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#TIME CAMPEAO

def time_campeao(dados):
    maior_pont = 0
    for pontos in dados.values():
        if pontos[0] >= maior_pont:
            maior_pont = pontos[0]

    times = []

    for e in dados.items():
        if e[1][0] == maior_pont:
            times.append(e[0])

    return times


