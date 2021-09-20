numero_inteiro = input('Digite um número inteiro: ')
numero_inteiro2 = input('Digite um número inteiro novamente: ')


#### Numero par e impar com codição IF ######

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print (f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')
else:
    print('Isso não é um número inteiro. ')

#### Numero par e impar com codição IF not ######

if not numero_inteiro2.isdigit():
    print('Isso não é um número inteiro')
else:
    numero_inteiro2 = int(numero_inteiro2)

    if not numero_inteiro2 % 2 == 0:
        print(f'{numero_inteiro2} é ímpar')
    else:
        print(f'{numero_inteiro2} é par')

## Digite um horário ####

horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if horario <= 11:
            print('Boa dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0  e 23.')

#### Contagem de caracteres do nome ####

nome = input('Digite seu nome: ')

tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto. ')
elif tamanho <= 6:
    print('Seu nome é normal. ')
else:
    print('Seu nome é muito grande. ')

