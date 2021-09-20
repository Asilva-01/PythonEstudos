# def ola_mundo():
#     return 'Ola mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
# print(executando)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome,saudacao):
    return f'Opa beleza? {nome}'

executando = mestre(fala_oi, 'Andre')
print(executando)
executando2 = mestre(saudacao, 'Luiz', saudacao)
print(executando2)
