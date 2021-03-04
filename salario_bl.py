#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SALÁRIO BRUTO E LÍQUIDO

nome = input()
quantidade_horas_extras = float(input())
salario_minimo = float(input())
valor_hora_extra = float(input())

salario_hora_extra = quantidade_horas_extras * valor_hora_extra
salario_bruto = 4 * salario_minimo + salario_hora_extra
desconto_INSS = salario_bruto * 0.12
desconto_imposto_renda = salario_bruto * 0.2
salario_liquido = salario_bruto - desconto_INSS - desconto_imposto_renda

print('O Salário Bruto de Antonio é de R$ {:.2f}'.format(salario_bruto))
print('O Salário Líquido de Antonio é de R$ {:.2f}'.format(salario_liquido))
