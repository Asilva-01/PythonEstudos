num = int(input("digite o numero:" ))

cont = 1
soma2 = 0
while cont <= num:
    soma1 = 1 / cont
    soma2 = soma2 + (soma1**2)

    cont = cont + 1

print("{:.6f}".format(soma2))
