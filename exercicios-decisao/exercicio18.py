# Poderia ser utilizado REGEX para esta validação

def main():
    date = get_date()
    is_date_valid(date)


def get_date():
    return input("informe uma data no formado dd/mm/yyyy: ")


def is_date_valid(date):
    splitted_date = date.split("/")
    if is_day_valid(splitted_date[0]) and is_mounth_valid(splitted_date[1]) and is_year_valid(splitted_date[2]):
        return print(f"{date} é uma data no formato correto")
    else:
        return print(f"{date} é uma data no formato incorreto")


def is_day_valid(day):
    return True if 0 < len(day) <= 2 and 1 <= int(day) <= 31 else False


def is_mounth_valid(mounth):
    return True if 0 < len(mounth) <= 2 and 1 <= int(mounth) <= 12 else False


def is_year_valid(year):
    return True if 0 < len(year) <= 4 and 1 <= int(year) <= 9999 else False


main()