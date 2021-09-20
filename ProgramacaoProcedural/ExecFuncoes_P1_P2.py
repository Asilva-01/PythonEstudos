#
# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')
#
# saudacao('ola', 'Joao')
# saudacao('Oi', 'Maria')
#
# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
#
# soma(10,0,2)
# soma(10,33,22)
# soma(10,550,2)

# def aumento_percentual(valor, percentual):
#      return(valor+(valor * percentual/100))
#
# ap= aumento_percentual(334,6)
# print(ap)
# ap = aumento_percentual(1320,15)
# print(ap)
# ap = aumento_percentual(337,8)
# print(ap)


def fb(n):
    if n % 3 == 0:
        return f'fizzbuzz, {n} é divisivel por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisivel por 3 e 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisivel por 3 e 5'

    return n

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(fb(aleatorio))

