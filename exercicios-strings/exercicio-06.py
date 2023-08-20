def main():
    date = input("informe uma data: ")
    spell_date(date)


def spell_date(date):
    months = ["janeiro", "fevereiro", "março",
              "abril", "maio", "junho", "julho",
              "agosto", "setembro", "outubro",
              "novembro", "dezembro"]

    day, month, year = date.split("/")
    print(f"{day} de {months[int(month)-1]} de {year}.")

main()
