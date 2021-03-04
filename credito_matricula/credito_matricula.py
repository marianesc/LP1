def num_creditos(bd_ufcg, matricula):
    creditos = 0
    for i in bd_ufcg.values():
        for e in i.items():
            if matricula in e[1]:
                creditos += e[0][1]

    return creditos

