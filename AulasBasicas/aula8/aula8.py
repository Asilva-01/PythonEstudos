nome = 'André Luiz'
idade = 40
altura = 1.73
peso = 77
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} peso {peso} e seu imc é {imc: .2f}.')
print(f'{nome} nasceu em {nascimento}.')