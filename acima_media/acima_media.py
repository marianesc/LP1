#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#ACIMA DA MÉDIA (CRIMINALIDADE)

media_ssp = float(input())
lista = []

while True:
    valores = input()
    valores_lista = valores.split()
    soma = 0
    if valores_lista[0] == 'fim':
        break
    for i in range(len(valores_lista)):
        soma += int(valores_lista[i])
    media = soma / len(valores_lista)
    if media <= media_ssp / 2:
        break
    elif media > media_ssp:
        lista.append(valores)

for e in lista:
    print(e)
