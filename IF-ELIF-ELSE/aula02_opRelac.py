""""
Operadores Relacionais 
== > >= <= !=
"""

num_1 = 2
num_2 = '2'

expressao = num_1 != num_2

print(expressao)


nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# Limite para pegar empréstimo
idade_menor = 20 # muito jovem
idade_maior = 40 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, pode pegar o emprésitimo. ' )
else:
    print(f'{nome}, NÃO pode pegar o emprésitimo. ')

======

nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior = True
idade = int(idade)

if idade > 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} NÃO é maior de idade.')

