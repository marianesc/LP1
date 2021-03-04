#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#LIMITE DE GASTOS

media_estabelecida = float(input())

while True:
    sequencia = input()
    gastos = sequencia.split()
    if sequencia == 'fim':
        break
    soma = 0
    for e in gastos:
        soma += float(e)
    media = soma / len(gastos)
    if media < media_estabelecida / 2:
        break
    if media > media_estabelecida:
        print(sequencia)

#Um erro
