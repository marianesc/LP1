#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#ACIMA DO LIMITE

limite = int(input())
somas = []
saidas = []

while True:
    sequencia = input().split()
    soma = 0
    saida = ''
    if sequencia[0] == '-':
        break
    for i in range(len(sequencia)):
        soma += int(sequencia[i])
        if sequencia[i] != sequencia[-1]:
            saida += sequencia[i] + ' + '
        else: 
            saida += sequencia[i]
    somas.append(soma)
    saidas.append(saida)
    if soma > (limite * 5):
        break

for i in range(len(somas)):
    if somas[i] >= limite:
        print('{} = {}'.format(saidas[i], somas[i]))
