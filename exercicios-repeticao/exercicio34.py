def get_number():
    number =  int(input("informe um valor para ser validado como primo"))
    return number


def is_prime(number):
    division = 1
    counter = 1
    while counter < number:
        if number % counter == 0:
            division += 1
        counter += 1

    return True if division == 2 else False


def main():
    number = get_number()
    is_prime_result = is_prime(number)
    print(f"{number} é primo" if is_prime_result else f"{number} não é primo")

main()

