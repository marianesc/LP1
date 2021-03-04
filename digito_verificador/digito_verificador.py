#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#DÍGITO VERIFICADOR DE 5 DÍGITOS

conta = input()
soma = int(conta[0]) + int(conta[1]) + int(conta[2]) + int(conta[3]) + int(conta[4])
verificador =  soma % 11

print('{}-{:02}'.format(conta,verificador))
