def main(number):
    multiplication_str = f"{number}! = "
    result = 1
    for i in reversed(range(1, number+1)):
        multiplication_str = multiplication_str + f"{i} . "
        result = result * i

    multiplication_str = multiplication_str[:-2]
    multiplication_str = multiplication_str + f" = {result}"

    print(f"Fatorial de:  {number}")
    print(f"{multiplication_str}")


main(5)
