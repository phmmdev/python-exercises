def main():
    number = input("informe um nuemro para ser revertido ")
    reversed_number = get_reversed_number(number)
    print(reversed_number)


def get_reversed_number(number):
    return number[::-1]


main()
