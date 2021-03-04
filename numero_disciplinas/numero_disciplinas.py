#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#NUMERO DE DISCIPLINAS

def numero_disciplinas(m1, m2, lista):
    horarios= []
    for e in m1.items():
        pula = False
        if e[0] in lista:   continue
        for j in e[1]:
            if j not in lista:
                pula= True
                break
        if pula == False:
            if m2[e[0]] not in horarios:
                horarios.append(m2[e[0]])
    return len(horarios)
