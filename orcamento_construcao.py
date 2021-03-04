#UFCG
#Prog1
#Mariane Silva de Carvalho - 119210450
#Orçamento Construção

tijolo_preco_unidade = float(input('Digite o preço da unidade do tijolo (Em reais): '))
tijolo_altura = float(input('Digite a altura do tijolo (Em metros): '))
tijolo_comprimento = float(input('Digite o comprimento do tijolo (Em metros): '))
parede_altura = float(input('Digite a altura das paredes (Em metros): '))
parede_comprimento = float(input('Digite o comprimento das paredes (Em metros): '))

num_tijolos_altura = parede_altura / tijolo_altura  
num_tijolos_largura = parede_comprimento / tijolo_comprimento
num_tijolos_total = num_tijolos_altura * num_tijolos_largura
orcamento_final = num_tijolos_total * tijolo_preco_unidade

print('O número total de tijolos é {} e o orçamento final é de R$ {}'. format(num_tijolos_total, orcamento_final))

