#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SELEÇÃO PROJETO

cre = float(input())
meses = float(input())
nota = float(input())

if cre < 7 and meses < 6:
    print('Candidato eliminado. Experiência abaixo do limite.')
elif cre < 7:
    print('Candidato eliminado. CRE abaixo do limite.')
elif meses < 6:
    print('Candidato eliminado. Experiência abaixo do limite.')
elif nota <= 3:
    print('Candidato classificado.')
elif nota > 3:
    print('Candidato aprovado.')
