cont = [0,0,0,0,0,0,0,0,0,0]
n = int(input())

for k in range(n):
    matricula = input()
    for digito in matricula:
        cont[int(digito)] += 1

maior = 0
for i in range(len(cont)):
    if cont[i] > cont[maior]:
        maior = i

print(maior,cont[maior])
