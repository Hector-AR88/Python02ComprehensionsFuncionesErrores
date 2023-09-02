print('Conjutons de muestra')
set_a = {'col','mex','bol'}
set_b = {'per','bol','arg'}
print(set_a)
print(set_b)

#union
print('Union de los conjuntos')
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# inteseccion
print('Interseccion de los conjutnos')
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# diferencia
print('Diferencia')
set_c = set_a.difference(set_b)
print(set_c)
print(set_a-set_b)

# diferencia simetrica
print('Diferencia simetrica')
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)