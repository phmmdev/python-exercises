def get_numbers():
    first_number = int(input("informe o primeiro valor "))
    second_number = int(input("informe o segundo valor "))
    third_number = int(input("informe o terceiro valor "))

    return first_number, second_number, third_number


def sort_numbers(first_number, second_number, third_number):
    begin = 0
    middle = 0
    end = 0

    if first_number > second_number and first_number > third_number:
        end = first_number
        if second_number >= third_number:
            middle = second_number
            begin = third_number
        else:
            middle = third_number
            begin = second_number
    elif second_number > first_number and second_number > third_number:
        end = second_number
        if first_number >= third_number:
            middle = first_number
            begin = third_number
        else:
            middle = third_number
            begin = first_number
    else:
        end = third_number
        if first_number >= second_number:
            middle = first_number
            begin = second_number
        else:
            middle = second_number
            begin = first_number

    print(f"{begin}, {middle}, {end}")


first_number, second_number, third_number = get_numbers()
sort_numbers(first_number, second_number, third_number)
