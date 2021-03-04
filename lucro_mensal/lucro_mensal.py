#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#LUCRO MENSAL DE UMA EMPRESA

n = 12
lista = []

for i in range(12):
    luc_desp = input().split()
    lucro = float(luc_desp[0]) - float(luc_desp[1])
    lista.append(lucro)

print('jan {:4.1f}'.format(float(lista[0])))
print('fev {:4.1f}'.format(float(lista[1])))
print('mar {:4.1f}'.format(float(lista[2])))
print('abr {:4.1f}'.format(float(lista[3])))
print('mai {:4.1f}'.format(float(lista[4])))
print('jun {:4.1f}'.format(float(lista[5])))
print('jul {:4.1f}'.format(float(lista[6])))
print('ago {:4.1f}'.format(float(lista[7])))
print('set {:4.1f}'.format(float(lista[8])))
print('out {:4.1f}'.format(float(lista[9])))
print('nov {:4.1f}'.format(float(lista[10])))
print('dez {:4.1f}'.format(float(lista[11])))
