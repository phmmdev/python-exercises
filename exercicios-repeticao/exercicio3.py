def main():
    get_values()


def get_values():
    get_name()
    get_age()
    get_salary()
    get_sex()
    ge_status()


def get_name():
    valid_name =  False
    while not valid_name:
        name = input("informe seu nome:")
        if len(name) < 3:
            print("o nome deve ser maior que 3 caracteres")
        else:
            valid_name = True

    return name


def get_age():
    valid_age = False
    while not valid_age:
        age = input("informe sua idade:")
        if age in range(0,151):
            print("idade fora do intervalo de 0 e 150")
        else:
            valid_age = True

    return age


def get_salary():
    valid_salary = False
    while not valid_salary:
        salary = float(input("informe seu salário:"))
        if salary <= 0:
            print("salário deve ser superior a 0")
        else:
            valid_salary = True

    return salary


def get_sex():
    valid_sex= False
    while not valid_sex:
        sex = input("informe seu sexo (F/M): ")
        if sex not in ["m","f"]:
            print("sexo inválido")
        else:
            valid_sex = True

    return sex


def ge_status():
    valid_status = False
    while not valid_status:
        status = input("informe seu estado civil (C/S/D/V): ")
        if status not in ["c","s", "d","v"]:
            print("sexo inválido")
        else:
            valid_status = True

    return status


main()