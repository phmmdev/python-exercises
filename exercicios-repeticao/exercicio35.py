def get_number():
    number =  int(input("informe um valor para ser validado como primo"))
    return number


def get_all_primes(number):
    divisions = []
    counter = 1
    while counter <= number:
        if counter % 2 != 0 or counter == 2:
            divisions.append(counter)
        counter += 1

    return divisions


def main():
    number = get_number()
    prime_list = get_all_primes(number)

    print(f"a lista de primos até {number} é {prime_list}")


main()

