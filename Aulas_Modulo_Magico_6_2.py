def main():
    numero_escolhido = 3
    numero_magico = int(input("Valor escolhido pelo magico: "))

    if numero_magico > numero_escolhido:
        print("Diminua o chute")
    elif numero_magico < numero_escolhido:
        print("Aumente o chute")
    else:
        print("Você acertou")

main()
