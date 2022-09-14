
salaries = []


def get_salaries():
    while True:
        salarie = int(input(f"informe o salário"))
        if salarie != 0:
            bonus = salarie * 0.2
            salaries.append([salarie, max(100, bonus)])
        else:
            break


def get_total_bonus():
    total = sum(salarie[1] for salarie in salaries)
    return total


def get_total_min_bonus_payed():
    total = sum(map(lambda i: i[1] == 100, salaries))
    return total


def get_max_bonus_payed():
    salarie = max(salarie[1] for salarie in salaries)
    return salarie


def shows_result(salaries_count, total_bonus, total_min_bonus, max_bonus_payed):
    print("Salário    - Abono  ")
    for salarie in salaries:
        print(f"{salarie[0]}    - {salarie[1]}  ")

    print(f"""Foram processados {salaries_count} colaboradores
Total gasto com abonos: R$ {total_bonus}
Valor mínimo pago a {total_min_bonus} colaboradores
Maior valor de abono pago: R$ {max_bonus_payed}""")


get_salaries()
salaries_count = len(salaries)
total_bonus = get_total_bonus()
total_min_bonus = get_total_min_bonus_payed()
max_bonus_payed = get_max_bonus_payed()

shows_result(salaries_count, total_bonus, total_min_bonus, max_bonus_payed)
