def get_salary():
    salary = float(input("informe o salário a ser re-ajustado: "))
    return salary


def aply_ajust(salary):
    if salary >= 1500.00:
        new_salary = salary * 1.05
        show_results(salary, new_salary, "5%")
    elif 1500 > salary > 700.00:
        new_salary = salary * 1.10
        show_results(salary, new_salary, "10%")
    elif 700.00 > salary > 280.00:
        new_salary = salary * 1.15
        show_results(salary, new_salary, "15%")
    else:
        new_salary = salary * 1.20
        show_results(salary, new_salary, "20%")


def show_results(old_salary, new_salary, percent):
    print(f"Salário anterio: {old_salary}")
    print(f"Aumento aplicado: {percent}")
    print(f"Valor Aumento: {new_salary - old_salary}")
    print(f"Salário Novo: {new_salary}")


salary = get_salary()
aply_ajust(salary)
