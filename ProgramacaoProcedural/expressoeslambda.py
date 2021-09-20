
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]


print(sorted(lista, key=lambda i: i[0], reverse=True))
print(sorted(lista, key=lambda i: i[1]))
print(lista)