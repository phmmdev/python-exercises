def main():
    year = get_year()
    is_leap_year = check_leap_year(year)
    show_result(year, is_leap_year)


def get_year():
    return int(input("infome um ano: "))


def check_leap_year(year):
    return True if year % 4 == 0 else False


def show_result(year, is_leap_year):
    print(f"{year} é um ano bissexto") if is_leap_year else print(f"{year} não é um ano bissexto")


main()
