dict = {'string_chave':1, 'string_chave2':2.4, 'string_chave3':'string'}
print(dict)
dict_num = {1:'um', 2:'dois',3:'tres',4:'quatro', 5:'cinco'}
print(dict_num)
dict_num[1]
for i in range(1,6):
    print(dict_num[i])
dict = {'dog': 'cachorro', 'cat':'gato'}
for i in dict:
    print(i)
for chaves in dict:
    print(chaves)

print('-'*25)

for chave in dict:
    print(dict[chave])

print("Todas as chaves:", dict.keys())
print("Todas os valores:",dict.values())

print('-'*25)

for valor in dict.values():
    print(valor)

print('-'*25)

for chave in dict.keys():
    print(chave)

print('-'*25)

for chave, valor in dict.items():
    print(f"A chave é {chave} e o valor é {valor}")
    print(f"O tipo da chave é {type(chave)} e o tipo do valor é {type(valor)}")


print('-'*25)


for chave, valor in dict.items():
    print(f"em inglês é {chave} e em porquguês é {valor}")

print('-'*25)

print(dict)

print('-'*25)

dict['monkey'] = 'macaco'

if 'monkey' in dict:
    print(f"{dict['monkey']} está no dicionario")
else:
    print("Eu não sei a traduçao desse palavra")

print('-'*25)
    
print(dict)

print('-'*25)

dict['banana'] = 'banana'

print(dict)

print('-'*25)

if 'banana' in dict:
    print(f"{dict['banana']} está no dicionario")

print(dict)

print('-'*25)

dict.pop('banana')
print(dict)

print('-'*25)

if 'banana' in dict:
    dict.pop('banana')
    print(dict)


print('-'*25)

dict.clear()
print(dict)
