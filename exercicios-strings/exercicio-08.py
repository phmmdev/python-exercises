def main():
    string = input("informe uma frase para verificar se é palindromo: ")
    string = string.replace(" ", "")

    if(string == string[::-1]):
        print("o texto informa é um palindromo")
    else:
        print("o texto informado não é um palindromo")


main()
