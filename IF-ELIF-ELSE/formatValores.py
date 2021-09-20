num_1 = 1

print(f'{num_1:0>10}')

num_2 = 1150

print(f'{num_2:0^10}')

num_3 = 1150

print(f'{num_3:0>10.2f}')

nome = 'Andre Luiz'
sobrenome = 'da Silva'
nome_formatado = ' {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

nome2 = 'Andre Luiz'
nome2 = nome2.ljust(20, '#')
print(nome2)

nome3 = 'Andre luiz'
print(nome3.lower()) # tudo minusculo
print(nome3.upper()) # tudo maisucuço
print(nome3.title()) # Primeiras letras maiusculas
