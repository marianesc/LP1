#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#DISCIPLINA DE UM PROFESSOR

def disciplinas(alocacao, professor):
    disciplinas = []
    creditos = 0
    for e in alocacao.items():
        if professor in e[1]:
            disciplinas.append(e[0][0])
            turmas = 0
            for i in e[1]:
                if professor == i:
                    turmas += 1
            creditos += (e[0][1]) * turmas

    return (disciplinas, creditos)

