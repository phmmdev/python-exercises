def main():
    max_value = 50
    print_even_numbers(max_value)


def print_even_numbers(max_value):
    for number in range(max_value):
         if number % 2 !=0:
             print(f"{number}")


main()
