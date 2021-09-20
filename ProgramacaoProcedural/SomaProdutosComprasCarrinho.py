carrinho = []

carrinho.append(('Produto 1', 30.55))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 30.23))


total = sum([float(y) for x, y in carrinho])
print(carrinho)
print('Valor total do carrinho é =>',total)