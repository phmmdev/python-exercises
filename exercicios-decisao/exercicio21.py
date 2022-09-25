def main(value):
    if not is_value_valid(value):
        print("valores informados fora do intervalo especificado")
    else:
        hundreds = 0
        fiftys = 0
        tens = 0
        fives = 0
        ones = 0
        if is_value_in_interval(value, 100, 600):
            hundreds = get_chunk(value, 100)
            hundreds_mod = get_chunk_mod(value, 100)
            fiftys = get_chunk(hundreds_mod, 50)
            fiftys_mod = get_chunk_mod(hundreds_mod, 50)
            tens = get_chunk(fiftys_mod, 10)
            tens_mod = get_chunk_mod(fiftys_mod, 10)
            fives = get_chunk(tens_mod, 5)
            fives_mod = get_chunk_mod(tens_mod, 5)
            ones = get_chunk(fives_mod, 1)
        elif is_value_in_interval(value, 50, 100):
            fiftys = get_chunk(value, 50)
            fiftys_mod = get_chunk_mod(value, 50)
            tens = get_chunk(fiftys_mod, 10)
            tens_mod = get_chunk_mod(fiftys_mod, 10)
            fives = get_chunk(tens_mod, 5)
            fives_mod = get_chunk_mod(tens_mod, 5)
            ones = get_chunk(fives_mod, 1)
        elif is_value_in_interval(value, 10, 50):
            tens = get_chunk(value, 10)
            tens_mod = get_chunk_mod(value, 10)
            fives = get_chunk(tens_mod, 5)
            fives_mod = get_chunk_mod(tens_mod, 5)
            ones = get_chunk(fives_mod, 1)
        elif is_value_in_interval(value, 1, 10):
            fives = get_chunk(value, 5)
            fives_mod = get_chunk_mod(value, 5)
            ones = get_chunk(fives_mod, 1)

        show_results(value, hundreds, fiftys, tens, fives, ones)

def show_results(value, hundreds, fifitys, tens, fives, ones):
    print(f"{value} - Notas: {hundreds} cem , {fifitys} cinquenta, {tens} dez, {fives} cinco, {ones} um")



def is_value_valid(value):
    return True if 10 <= value <= 600 else False


def is_value_in_interval(value, limit_begin, limit_end):
    return True if limit_begin <= value <= limit_end else False


def get_chunk(value, note):
    return value // note


def get_chunk_mod(value, note):
    return value % note


main(256)
main(399)
main(95)
main(42)
main(28)
main(13)
main(8)

"""main(256)
main(399)
main(95)
main(42)
main(23)
main(15)
main(8)"""