def main():
    string = input("informe uma frase para ser convertida:  ")
    leet_alphabet = set_leet_alphabet()
    leet(string, leet_alphabet)


def set_leet_alphabet():
    return {'a':'4',
            'e':'3',
            'i':'!',
            'u':'|_|',
            'o':'0',
            't':'7',
            's':'5',
            'l':'1',
            'g':'6'}


def leet(string, leet_alphabet):
    for k,v in leet_alphabet.items():
        string = string.replace(k, v)
    print(string)


main()