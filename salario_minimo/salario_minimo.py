#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#ANÁLISE DE VARIAÇÃO DO SALÁRIO MÍNIMO

ano_inicio = int(input())
ano_fim = int(input())
contador1 = 0 
contador2 = 0
med1 = [] 
med2 = [] 

for k in range(ano_fim - ano_inicio + 1):
    salario_minimo = float(input())
    if salario_minimo <= 100:
        contador1 += 1
        med1.append(str(salario_minimo))
    else:
        contador2 += 1
        med2.append(str(salario_minimo))

perc_menor = (contador1 / (ano_fim - ano_inicio + 1)) * 100
perc_maior = (contador2 / (ano_fim - ano_inicio + 1)) * 100

print('{} ano(s) abaixo ({:.0f}% dos anos)'.format(contador1, perc_menor))
cont1 = 0
if contador1 > 0:
    for e in med1:
        cont1 += float(e)
    media1 = cont1 / len(med1)
    print('média dos anos abaixo: U$ {:.2f}'.format(media1))


print('{} ano(s) acima ({:.0f}% dos anos)'.format(contador2, perc_maior))
cont2 = 0
if contador2 > 0:
    for e in med2:
        cont2 += float(e)
    media2 = cont2 / len(med2)
    print('média dos anos acima: U$ {:.2f}'.format(media2))
