#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#FORMA PALAVRA A PARTIR DE OUTRAS 3 PALAVRAS

p1 = input()
p2 = input()
p3 = input()
saida = ''

for i in range(len(p1)):
    if p1[i] > p2[i]:
        maior = p1[i]
    else:
        maior = p2[i]
    if p3[i] > maior:
        maior= p3[i]
    
    saida += maior

print(saida)
