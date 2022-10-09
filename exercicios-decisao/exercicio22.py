def is_odd(number):
    return True if number % 2 == 0 else False


def show_message(result):
    if result:
        print("Numero par")
    else:
        print("Numero impar")


show_message(is_odd(41))
show_message(is_odd(2))
show_message(is_odd(8))
show_message(is_odd(3))