def check_decimal(number):
    if isinstance(number, float):
        return not number.is_integer()
    else:
        return False


def check_decimal_alternative(number):
    rounded_number = round(number)
    return True if number != rounded_number else False


def show_message(result):
    if result:
        print("Numero decimal")
    else:
        print("Numero inteiro")


show_message(check_decimal(10))
show_message(check_decimal(5.5))
show_message(check_decimal(1.0))

print("-"*20)

show_message(check_decimal_alternative(10))
show_message(check_decimal_alternative(5.5))
show_message(check_decimal_alternative(1.0))