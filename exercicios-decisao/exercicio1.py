def get_numbers():
    first_number = int(input("informe o primeiro valor "))
    second_number = int(input("informe o segundo valor "))

    return first_number, second_number


def get_greater(first_number, second_number):
    if first_number > second_number:
        print(f"O maior numero é {first_number}")
    else:
        print(f"O maior numero é {second_number}")


def get_greater_alternative(first_number, second_number):
    greater = max(first_number, second_number)
    print(f"O maior numero é {greater}")


first_number, second_number = get_numbers()
get_greater(first_number, second_number)
get_greater_alternative(first_number, second_number)

