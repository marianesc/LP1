#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#COLEGAS DE SALA

def colegas_de_sala(salasprofs, professor):
    colegas = []
    for e in salasprofs.items():
        if e[1] == salasprofs[professor] and e[0] != professor:
            colegas.append(e[0])

    return colegas

