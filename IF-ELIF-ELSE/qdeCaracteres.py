usuario = input('Digite seu usuário: ')

qtde_caracteres = len(usuario)

if qtde_caracteres < 6:
    print('você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')

###
string1 = input('Digite aqui: ')
string2 = input('Digite novamente: ')

print(f'A quantidade total de caracterece digitados foi {len(string1) + len(string2)}')