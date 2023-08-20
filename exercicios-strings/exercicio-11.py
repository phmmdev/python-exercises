from random import choice


def main():
    chances = 6
    word = select_word();
    letters = set_letters(word)
    won = False

    while chances > 0 and not won:
        print(f"Canches: {chances}/6")
        display(word, letters)
        play = get_play()

        if not is_valid_play(play):
            print("jogada inválida")
        else:
            result, letters = has_letter(play, word, letters)
            if not result:
                chances -= 1
            else:
                won = has_won(letters)

    display(word, letters)

    if not won:
        print(f"Você perdeu !! Resposta: {word}")
    else:
        print(f"Você venceu !!")


def select_word():
    words = ["casa", "foguete", "arvore", "guarda-chuva", "vaga-lume", "escada", "gira-sol", "refrigerante", "enxugar", "exoesqueleto"]
    return choice(words)


def set_letters(word):
    letters = [x for x in list(word) if x != "-"]
    return letters


def display(word, letters):
    display_text = ""
    for i in list(word):
        if i == "-":
            display_text += " - "
        else:
            if i in letters:
                display_text += " _ "
            else:
                display_text += i.upper() + " "

    print(display_text)


def get_play():
    play = input("informe uma letra:  ")
    return play


def is_valid_play(play):
    return False if not 0 < len(play) < 2 else True


def has_letter(play, word, letters):
    if play in word:
        letters = [x for x in letters if x != play]
        return True, letters
    else:
        return False, letters


def has_won(letters):
    return True if len(letters) == 0 else False


main()
