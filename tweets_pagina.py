#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#TWEETS POR PÁGINA

tweets = int(input())

paginas = tweets // 400
perdidos = (tweets % 400)
porcentagem = perdidos * 100 / tweets

print('Serão necessárias {} página(s) para visualizar os tweets.'.format(paginas))
print('{:.1f}% dos tweets serão perdidos.'.format(porcentagem))
