#UFCG
#Prog1
#Mariane Silva de Carvalho - 119210450
#Média ponderada

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

peso1 = float(input()) / 100
peso2 = float(input()) / 100
peso3 = 1 - (peso1 + peso2)

media_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)
print('Média Final: {:.1f}'.format(media_final))
