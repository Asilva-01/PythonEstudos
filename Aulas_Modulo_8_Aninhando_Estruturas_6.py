cursos = {'solid':
          {'nome': 'Aprenda Design Patterns com SOLID',
          'categoria':'Design Patterns',
          'instrutor':'Felipe Cabrera',
          'alunos': 5000
          },
          'android9':{
          'nome':'Android 9.0 Avençado: APIs Nativas e banco de Dados',
          'categoria': 'Android',
          'instrutor': 'Alisson',
          'alunos': 5000
          },
          'vscode':{
              'nome': 'VS CODE: Produtividade Infinita',
              'categoria':'Programação',
              'instrutor': 'Felipe Cabrera',
              'alunos':5000}
          }
print('-'*25)

for chave in cursos.keys():
    print(chave)

print('-'*25)


print(cursos['solid']['nome'])
print(cursos['solid']['instrutor'])
print(cursos['solid']['categoria'])
print(cursos['solid']['alunos'])
print('-'*25)

lista = [[0,1,2,3],[1.2,3.4,5.6], ['abc','def','ghi']]
print(lista)
print(lista[2])
print(lista[2][1])

print('-'*25)

tuplas = ((0,1),(2.3,4.5),('a','b'),('bylearn', 'felipe'))
print(tuplas)
print(tuplas[1])
print(tuplas[1][0])
print(tuplas[3])
print(tuplas[3][0])

print('-'*25)

conj = set()
conj.add(frozenset((1,2)))
conj.add(frozenset((3,4)))
conj.add(frozenset((5,6)))
print(conj)



print('-'*25)

for i in conj:
    print(type(i))

print('-'*25)

super_estrutura = ([1,2,3], {'chave':'valor'}, {2,3,4},[1,(2,3),{'chave':(2,3)}])
print(super_estrutura)
