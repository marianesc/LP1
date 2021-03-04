#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#OCORRENCIAS LETRA

frase = input()
letras = str.lower(frase)
dic = {}

for e in letras:
    if e == ' ': continue
    if e not in dic.keys():
        dic[e] = 1
    else:
        dic[e] += 1

maior = 0
x = ' '
for i in dic.items():
    if i[1] > maior:
        maior =  i[1]
        x = i[0]

print('{} {}'.format(x, maior))
