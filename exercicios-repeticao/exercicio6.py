def main():
    max_value = 20

    print_bellow(max_value)
    print_side(max_value)


def print_bellow(max_value):
    for number in range(max_value):
        print(f"{number}")


def print_side(max_value):
    numbers = ""
    for number in range(max_value):
        numbers = numbers + " " + str(number)

    print(f"{numbers}")

main()