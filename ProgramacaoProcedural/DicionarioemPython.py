
# d1 = {1: 'valor 1', 'chave2': 'valor 2', 3: 'valor 3', 'chave4': 'valor 4'}
#
# print(d1[3])

# clientes = {
#     'cliente1' : {
#         'nome': 'André',
#         'sobrenome': 'Luiz',
#
#    },
#     'cliente2': {
#         'nome': 'Maria',
#         'sobrenome': 'Vicky',
#
#     },
#
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

########################################XX############################
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ('André', 'Luiz' )}
v = d1.copy()

v[1] = 'André'
v['d'] = ('Luiz', 'André')

print(d1)
print(v)

