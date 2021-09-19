tupla = tuple([i for i in range(11)])
print(tupla)

lista = [1,2,3]
tupla = tuple(lista)
print(type(lista))
print(type(tupla))
tupla= (1,2,3,4,5)
lista = list(tupla)
lista.append(6)
lista[2] = 'Teste'
lista.remove(4)
tupla = tuple(lista)
print(tupla)
tupla =(1,2,3,4,5)
print(tupla[0])
print(tupla[1:4])
print(tupla[-1])
print(len(tupla))
print(3 in tupla)
print(5 not in tupla)
for i in tupla:
    print(i)
