#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#REPROVADOS POR FALTA

contador = 0

while True:
    registro = input()
    f = 0
    i = 0 
    if registro == '-':
        break
    while i < len(registro):
        if registro[i] == 'f':
            f += 1
        if f == 9:
            contador += 1
            break
        i += 1

print('{} aluno(s) reprovado(s) por falta.'.format(contador))
