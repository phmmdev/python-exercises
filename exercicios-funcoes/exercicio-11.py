from dateutil.parser import parse


def main():
    date = input("informe uma data: ")
    if check_date(date):
        spell_date(date)
    else:
        print("data inválida")


def spell_date(date):
    months = ["janeiro", "fevereiro", "março",
              "abril", "maio", "junho", "julho",
              "agosto", "setembro", "outubro",
              "novembro", "dezembro"]

    day, month, year = date.split("/")
    print(f"{day} de {months[int(month)-1]} de {year}.")


def check_date(date):
    try:
        parse(date, fuzzy = False)
        return True

    except ValueError:
        return False


main()