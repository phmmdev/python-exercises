letters = []
vogais = ['a', 'e', 'i', 'o', 'u']


def get_letters():
    consoantes = 0
    while len(letters) < 10:
        value = input("informe um letra:")
        letters.append(value)

        if value.lower() not in vogais:
            consoantes = consoantes + 1

    print(f"Total de consoantes: {consoantes}")


get_letters()
