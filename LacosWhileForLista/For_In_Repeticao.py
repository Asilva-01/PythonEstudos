texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 'P':
        nova_string = nova_string + letra.lower()
    elif letra == 'o':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)