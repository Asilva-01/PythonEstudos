
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break


    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    print(digitadas)

    if letra in secreto:
        print(f'UHUULL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta. ')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Que legal, VOCÊ GANHOU!!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario} !')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances}, chances.')
    print()



