def get_letter():
    letter = input("informe F ou  M :")
    return letter


def print_letter(letter):
    if letter == 'F':
        print("F - Feminino")
    elif letter == 'M':
        print("M - Masculino")
    else:
        print("Sexo inválido")


letter = get_letter()
print_letter(letter)