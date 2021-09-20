print('Escolhe a opção correta para as questões abaixo:')


perguntas = {
    'pergunta 1':{
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'respostas_certas': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'respostas_certas': 'c',
    },

    'pergunta 3': {
        'pergunta': 'Quanto é 2*2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'respostas_certas': 'b',
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 10*3? ',
        'respostas': {'a': '30', 'b': '10', 'c': '6', },
        'respostas_certas': 'a',
    },
    'pergunta 5':{
        'pergunta': 'Quanto é 100-2? ',
        'respostas': {'a': '1', 'b': '92', 'c': '5',},
        'respostas_certas': 'b',
    },
    'pergunta 6': {
        'pergunta': 'Quanto é 20*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '40', },
        'respostas_certas': 'c',
    },
    'pergunta 6':{
        'pergunta': 'Quanto é 50+10? ',
        'respostas': {'a': '1', 'b': '40', 'c': '5',},
        'respostas_certas': 'b',
    },
    'pergunta 7': {
        'pergunta': 'Quanto é 55-2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '53', },
        'respostas_certas': 'c',
    },


}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha as opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['respostas_certas']:
        print('Você acertou!!!')
        respostas_certas += 1
    else:
        print('Infelizmente você errou!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100


print(f'Você acertou {respostas_certas} respostas de um total de {qtd_perguntas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')