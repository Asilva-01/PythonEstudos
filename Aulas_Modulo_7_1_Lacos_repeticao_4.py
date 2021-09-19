
alunos = ['Felipe','Alisson','Haynes','Bylearner']
notas = [[1,10],[10,7],[8,9],[10,10]]

if(len(alunos) == len(notas)):
    for indice in range(len(alunos)):
        soma = 0
        for nota in notas[indice]:
            soma+= nota
        media = soma / len(notas[indice])
        print(f'O aluno {alunos[indice]} tem média {media}')
        if(media > 6):
            print(f'- Portanto, ele foi aprovado')
        else:
            print(f'- Portanto, ele foi reprovado')
            

