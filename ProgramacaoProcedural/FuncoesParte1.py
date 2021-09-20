
def funcao(msg = 'Padrao', nome = 'usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')

    print(msg, nome)

funcao( nome='Zezinho', msg='Hello')

funcao('Ola','André')
funcao('Ola','Joao')
funcao('Oi','Pessoal')
funcao('Ola','Amigo')

def saudacao(msg1='Oi', nome1='USER'):
    return f'{msg1}, {nome1}'

variavel = saudacao()
print(variavel)