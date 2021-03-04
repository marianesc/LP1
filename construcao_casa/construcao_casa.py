#UFCG
#PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CONSTRUÇÃO DE CASA

l1 = float(input())
l2 = float(input())
area_casa = float(input())

quantidade = int((l1 * l2) // area_casa)

print('{} casa(s) pode(m) ser construída(s) no terreno.'.format(quantidade))
