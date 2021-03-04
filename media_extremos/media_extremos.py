#UFCG - PROG1
#MARIANE SILVA DE CARVALHO
#MÉDIA DOS EXTREMOS

n = int(input())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

menor = nums[0]
maior = nums[0]

for n in range(len(nums)):
    if nums[n] < menor:
        menor = nums[n]
    if nums[n] > maior:
        maior = nums[n]

media = (menor + maior) / 2

abaixo = 0
acima = 0

for l in range(len(nums)):
    if nums[l] < media:
        abaixo += 1
    elif nums[l] > media:
        acima += 1

print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))
print('Média dos extremos: {:.2f}'.format(media))
print('{} número(s) abaixo da média'.format(abaixo))
print('{} número(s) acima da média'.format(acima))
