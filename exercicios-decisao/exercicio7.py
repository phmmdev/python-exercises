def get_numbers():
    first_number = int(input("informe o primeiro valor "))
    second_number = int(input("informe o segundo valor "))
    third_number = int(input("informe o terceiro valor "))

    return first_number, second_number, third_number


def get_greater(first_number, second_number, third_number):
    if first_number >= second_number and first_number >= third_number:
        print(f"O primeiro valor é maior : {first_number}")
    elif second_number >= first_number and second_number >= third_number:
        print(f"O segundo valor é maior : {second_number}")
    else:
        print(f"O terceiro valor é maior : {third_number}")


def get_smaller(first_number, second_number, third_number):
    if first_number <= second_number and first_number <= third_number:
        print(f"O primeiro valor é menor : {first_number}")
    elif second_number <= first_number and second_number <= third_number:
        print(f"O segundo valor é menor : {second_number}")
    else:
        print(f"O terceiro valor é menor : {third_number}")


first_number, second_number, third_number = get_numbers()
get_greater(first_number, second_number, third_number)
get_smaller(first_number, second_number, third_number)

