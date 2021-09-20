# string = "O Brasil é o pais do futebol, o Brasil é penta."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
#     print(f'A palavra que apareceu mais vezes é {palavra} ({contagem} vezes)')

# string = "O Brasil é penta."
# lista = string.split(' ')
# string2 = ' ; '.join(lista)
#
# print(string)
# print(lista)
# print(string2)

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista_3 = ['Luiz', 'André', 'Silva', 1, 2, 5, 'teste', 'dado', 'rrDD']

print(lista_3[2]) # imprime a posição da lista
A, B, C, *restanteLista = lista_3 # o "*" junto com a variavel "restanteLista", imprime o retante da lista criando uma nova lista
print(A) # Desempacotamento imprime o dado da lista mas por conta do "A" ser uma variavel que substitui "Luiz", não confundir com a posiçao na lista
print(restanteLista)
