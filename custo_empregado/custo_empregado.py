#UFGC - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CUSTO EMPREGADO

salario_bruto = float(input())
dias_trabalhados = float(input())
transporte = float(input())

salario_bruto6 = 0.06 * salario_bruto #quanto é 6% do salario bruto
total_transporte = dias_trabalhados * transporte #total de dinheiro gasto em transporte
fgts_empregador = 0.08 * salario_bruto
inss_empregador = 0.12 * salario_bruto

inss_empregado = 0

#if do INSS do empregado

if salario_bruto <= 1317.07:
    inss_empregado = 0.08 * salario_bruto
elif 1317.08 <= salario_bruto <= 2195.12:
    inss_empregado = 0.09 * salario_bruto
elif salario_bruto >= 2195.13:
    inss_empregado = 0.11 * salario_bruto

#if do custo total do empregador

custo_empregador = 0
salario_liquido = 0

if total_transporte > salario_bruto6:
    custo_empregador = salario_bruto + (total_transporte - salario_bruto6) + fgts_empregador + inss_empregador
    salario_liquido = salario_bruto - inss_empregado - salario_bruto6
else:
    custo_empregador = salario_bruto + fgts_empregador + inss_empregador
    salario_liquido =  salario_bruto - inss_empregado - total_transporte

print('salário bruto = R$ {:.2f}'.format(salario_bruto))
print('custo mensal = R$ {:.2f}'.format(custo_empregador))
print('salário líquido = R$ {:.2f}'.format(salario_liquido))
