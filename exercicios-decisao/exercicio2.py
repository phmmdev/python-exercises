def get_numbers():
    number = int(input("informe o primeiro valor "))
    return number


def get_positive_negative(number):
    if number >= 0:
        print(f"{number} é um valor positivo")
    else:
        print(f"{number} é um valor negativo")


number = get_numbers()
get_positive_negative(number)
