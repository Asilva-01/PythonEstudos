def ola(meu_nome):
    
    print("Olá,", meu_nome)

ola('Felipe')

print('-'*25)

def ola_idade(meu_nome,minha_idade):
    print(f'Olá {meu_nome}, você tem: {minha_idade} anos!')
ola_idade('André',39)

print('-'*25)
def media(nota1,nota2):
    media=(nota1 + nota2)/2
    return media
minha_media = media(9,7)
print(f"minha média é: {minha_media}")
print('-'*25)

def media():
    nota1 = float(input("Minha primeira nota: "))
    nota2 = float(input("Minha segunda nota: "))
    media = (nota1 + nota2)/2
    return media
minha_media = media()
print("Minha média é: ", minha_media)


print('-'*25)

def media2():
    nota1 = float(input("Minha primeira nota: "))
    nota2 = float(input("Minha segunda nota: "))
    return calcular_media(nota1,nota2)

def calcular_media(nota1,nota2):
    media2 = (nota1+nota2)/2
    return media2

def calcular_aprovacao(media2):
    if(media2 >=6):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
    
calcular_aprovacao(media2())


