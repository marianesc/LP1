#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#NÚMERO DE DÍGITOS

n = int(input())
a = n
contador = 0

while True:
   x = a // 10
   contador += 1
   if int(a // 10) == 0:
       break
   a = x

print(contador)
