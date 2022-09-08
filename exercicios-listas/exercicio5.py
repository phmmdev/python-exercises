numbers = []
evens = []
odds = []


def get_numbers():
    while len(numbers) < 10:
        value = int(input("informe um valor:"))
        numbers.append(value)


def separate_numbers():
    for item in numbers:
        if item % 2:
            evens.append(item)
        else:
            odds.append(item)

    return evens, odds


def show_lists(lists):
    print(f"{lists}")


get_numbers()
separate_numbers()
show_lists(numbers)
show_lists(evens)
show_lists(odds)
