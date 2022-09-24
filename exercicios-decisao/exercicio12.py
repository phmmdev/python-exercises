def main():
    hour, value = get_hours_and_value()
    salary = get_salary(hour, value)
    IR = get_IR(salary)
    INSS = get_INSS(salary)
    FGTS = get_FGTS(salary)
    discounted_salary = get_discounted_salary(IR, INSS, salary)
    show_results(hour, value, salary, IR, INSS, FGTS, discounted_salary)

def get_hours_and_value():
    hour = int(input("informe quantidade de horas trabalhadas no mês: "))
    value = float(input("informe valor da hora trabalhada: "))

    return hour, value


def get_salary(hour, value):
    return round(hour * value, 2)


def get_IR(salary):
    discount = 0.0
    discount_text = "0%"
    if salary <= 900.00:
        pass
    elif 900 < salary <= 1500.00:
        discount = 0.05
        discount_text = "5%"
    elif 1500.00 < salary <= 2500.00:
        discount = -0.10
        discount_text = "10%"
    elif salary > 2500.00:
        discount = -0.20
        discount_text = "20%"

    discounted_value = round(salary * discount, 2)

    return [discounted_value, discount_text]


def get_INSS(salary):
    discounted_value = round(salary * 0.10, 2)
    return [discounted_value, "10%"]


def get_FGTS(salary):
    discounted_value = round(salary * 0.11, 2)
    return [discounted_value, "11%"]


def get_discounted_salary(IR, INSS, salary):
    total_discount = IR[0] + INSS[0]
    discounted_salary = salary - total_discount
    return [discounted_salary, total_discount]


def show_results(hour, value, salary, IR, INSS, FGTS, discounted_salary):
    print(f"""Salário Bruto: ({value} * {hour})        : R$ {salary}
(-) IR ({IR[1]})                     : R$   {IR[0]} 
(-) INSS ({INSS[1]})                 : R$  {INSS[0]} 
FGTS ({FGTS[1]})                      : R$  {FGTS[0]}
Total de descontos              : R$  {discounted_salary[1]}
Salário Liquido                 : R$  {discounted_salary[0]}
""")


main()
