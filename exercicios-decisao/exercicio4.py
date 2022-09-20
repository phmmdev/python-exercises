def get_letter():
    letter = input("informe uma letra")
    return letter.lower().strip()


def decide_consonant_or_not(letter):
    vowel = ['a', 'e', 'i', 'o', 'u']

    if letter in vowel:
        print(f"{letter} é um vogal")
    else:
        print(f"{letter} é uma consoante")


letter = get_letter()
decide_consonant_or_not(letter)