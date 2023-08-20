def main():
    string1 = input("informe a primeira string: ")
    string2 = input("informe a segunda string: ")

    len_string1 = len(string1)
    len_string2 = len(string2)

    print(f"{string1} tem {len_string1} caracteres")
    print(f"{string2} tem {len_string2} caracteres")

    if len_string1 == len_string2:
        print("Strings possuem o mesmo tamanho")
    else:
        print("Strings possuem tamanhos diferentes")

    if string1 == string2:
        print("Strings são iguais")
    else:
        print("Strings são diferentes")


main()