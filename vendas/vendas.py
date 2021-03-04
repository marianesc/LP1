#UFCG
#PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#VENDAS
#vl = vendidos na loja, vt = vendidos por Teresa, vc = vendidos por Carla, vj = vendidos por Joaquim

vl = int(input())
vt = int(input())
vc = int(input())

vj = vl - (vt + vc)

vt_pct = (vt / vl) * 100
vc_pct = (vc / vl) * 100
vj_pct = (vj / vl) * 100

print('Teresa vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(vt,vl,vt_pct))
print('Joaquim vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(vj,vl,vj_pct))
print('Carla vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(vc,vl,vc_pct))
