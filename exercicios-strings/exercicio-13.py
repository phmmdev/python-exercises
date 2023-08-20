from random import choice, randint


def main():
    chances = 6
    word = select_word();
    secret = shuffle_word(word)
    won = False

    while chances > 0 and not won:
        print(f"Canches: {chances}/6")
        print(f"a palavra embaralhada é {secret.upper()}")
        play = get_play()

        won = has_won(word, play)
        if not won:
            print("resposta incorreta, tente novamente")

    if not won:
        print(f"Você perdeu !! Resposta: {word}")
    else:
        print(f"Você venceu !!")


def select_word():
    words = ["casa", "foguete", "arvore", "guarda-chuva", "vaga-lume", "escada", "gira-sol", "refrigerante",
             "enxugar", "exoesqueleto"]
    return choice(words)


def shuffle_word(word):
    positions = list(word)
    word_size = len(word)
    for i in range(word_size - 1, 0, -1):
        j = randint(0, i + 1)
        positions[i], positions[j] = positions[j], positions[i]
    return ''.join(positions)


def get_play():
    play = input("Qual é a palavra oculta?:  ")
    return play


def has_won(word, play):
    return True if word == play else False


main()