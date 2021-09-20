"""
Operadores Lógicos
and, or, not
in e not in
"""

# (Verdadeiro E False) = Falso

#comparacao1 and comparacao


a = -1
b = 3

if not a:
    print("Preencha valor de A")
else:
    print("A é maior que B.")

nome = 'André Luiz.'

if 'u' in nome:
    print("Existe a letra U no seu nome")
else:
    print("Não existe")

####

usuario = input('Nome de usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = "Andre"
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado!')
else:
    print('Usuario ou senha incorreto!')

#####

if False:
    print('Um')
elif False:
    print('Dois')
elif False:
    print('Três')
elif True:
    print('Quatro')
elif False:
    print('Cinco')
else:
    print('Seis')


####

num_1 = 0
num_2 = 0

if not num_1 != num_2:
    print('Retorno 1')
else:
    print('Retorno 2')
