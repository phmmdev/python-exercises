def get_number():
    number =  int(input("informe um valor para ser validado como primo"))
    return number


def is_prime(number):
    divisions = []
    counter = 1
    while counter < number:
        if number % counter == 0:
            divisions.append(counter)
        counter += 1

    return (True, divisions) if len(divisions) == 1 else (False, divisions)


def main():
    number = get_number()
    is_prime_result = is_prime(number)

    print(f"{number} é primo" if is_prime_result[0] else f"{number} não é primo e esses são seus divisores {is_prime_result[1]}")

main()

