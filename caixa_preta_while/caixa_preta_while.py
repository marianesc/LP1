#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CAIXA PRETA DESCARTANDO LEITURAS

peso = 0
combustivel = 0
altitude = 0

while True:
    dados = input()
    dados_lista = dados.split()
    i = 0
    negativo = False
    while i < len(dados_lista):
        if i == 0 and int(dados_lista[i]) >= 0:
            peso += 1
        elif i == 1 and int(dados_lista[i]) >= 0:
            combustivel += 1
        elif i == 2 and int(dados_lista[i]) >= 0:
            altitude += 1
        elif i == 0 and int(dados_lista[i]) < 0:
            negativo = True
            print('dado inconsistente. peso negativo.')
            break
        elif i == 1 and int(dados_lista[i]) < 0:
            negativo = True
            print('dado inconsistente. combustível negativo.')
            break
        elif i == 2 and int(dados_lista[i]) < 0:
            negativo = True
            print('dado inconsistente. altitude negativa.')
            break
        i += 1
    if negativo:
        break

print('peso: {}'.format(peso))
print('combustível: {}'.format(combustivel))
print('altitude: {}'.format(altitude))
