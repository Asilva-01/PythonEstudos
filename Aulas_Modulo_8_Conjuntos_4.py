conjunto = {'teste'}
print(conjunto)
print(type(conjunto))
print(type({1}))
conjunto = {1,2,3,4}
print(conjunto)

conjunto1 = {'a','b','c','d'}
conjunto2 = {'j','m','n','c','d'}
print(conjunto1)
print(conjunto2)

conjunto1.add('j')
conjunto2.add('a')
print(conjunto1)
print(conjunto2)

frutas={'maça','uva'}
print(frutas)
frutas.add('laranja')
print(frutas)
frutas.update(['pera', 'abacaxi','morango'])
print(frutas)
frutas.discard("maça")
print(frutas)
frutas.clear()
print(frutas)

conjunto_total = conjunto1.union(conjunto2)
print(conjunto_total)

conjunto_total = conjunto1.update(conjunto2)
print(conjunto_total)
conjunto1.update(conjunto2)
print(conjunto1)

conjunto1 = {'a','b','c','d'}
conjunto2 = {'j','m','n','c','d'}

interseccao = conjunto1.intersection(conjunto2)
print(interseccao)

conjunto1 = {'a','b','c','d'}
conjunto2 = {'j','m','n','c','d'}

diferenca = conjunto1.difference(conjunto2)
print(diferenca)

diferenca2 = conjunto2.difference(conjunto1)
print(diferenca2)


conjuntinho = {1,2,3}
conjuntao = {1,2,3,4,5,6}
subconjunto = conjuntinho.issubset(conjuntao)
print(subconjunto)

print(type({''}))
print(type)

set()
tuple()
list()
print()
lista = [1,2,3,4,5]
tupla = ['a','b','c','d','e','f']
conjunto1 = set(lista)
conjunto2 = set(tupla)
print(conjunto1)
print(conjunto2)

