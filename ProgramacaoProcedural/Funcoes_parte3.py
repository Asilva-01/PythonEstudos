

def func(*args, **kwargs):
    print(args)

    nome = kwargs['nome']
    print(nome)
    idade = kwargs['idade']
    print(idade)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome ='Andre', sobrenome='Luiz', idade=40)

