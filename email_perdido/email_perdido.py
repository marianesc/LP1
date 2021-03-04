#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#EMAIL PERDIDO

def encontra_email_perdido(l1, l2):
    for e in l1:
        diferente = True
        for j in l2:
            if e == j:
                diferente = False
                break
        if diferente:
            return e

