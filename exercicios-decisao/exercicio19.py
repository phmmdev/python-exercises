def main(number):
    # number = get_number()
    hundreds = 0
    decimals = 0
    units = 0
    if not is_number_valid(number):
        print("Valor informado fora do limite especificado !")
    else:
        hundreds_mod = 0
        decimals_mods = 0
        if has_hundred(number):
            hundreds = get_hundreds(number)
            hundreds_mod = get_hundreds_mod(number)
            decimals = get_decimals(hundreds_mod)
            decimals_mods = get_decimals_mod(hundreds_mod)
            units = get_units(decimals_mods)
        elif has_decimals(number):
            decimals = get_decimals(number)
            decimals_mods = get_decimals_mod(number)
            units = get_units(decimals_mods)
        elif has_units(number):
            units = get_units(number)

    show_results(number, hundreds, decimals, units)


def show_results(number, hundreds, decimals, units):
    print(f"{number} - {hundreds} centenas , {decimals} dezenas, {units} unidades")


def get_number():
    return int(input("informe um numero de 1 a 1000: "))


def is_number_valid(number):
    return True if 0 < number <= 1000 else False


def has_hundred(number):
    return True if number > 99 else False


def get_hundreds(number):
    return number // 100


def get_hundreds_mod(number):
    return number % 100


def has_decimals(number_decimals):
    return True if 10 <= number_decimals <= 99 else False


def get_decimals(number_decimals):
    return number_decimals // 10


def get_decimals_mod(number_decimals):
    return number_decimals % 10


def has_units(number_units):
    return True if 0 <= number_units <= 9 else False


def get_units(number_units):
    return number_units





main(326)
main(300)
main(100)
main(320)
main(310)
main(305)
main(301)
main(101)
main(311)
main(111)
main(25)
main(20)
main(10)
main(21)
main(11)
main(1)
main(7)
main(16)
