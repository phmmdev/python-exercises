def get_number():
    return input("informe um numero de 1  à 7: ")


def get_week_day(number):
    match number:
        case '1':
            print(f" {number} - Domingo")
        case '2':
            print(f"{number} - Segunda")
        case "3":
            print(f"{number} - Terça")
        case "4":
            print(f"{number} - Quarta")
        case "5":
            print(f"{number} - Quinta")
        case "6":
            print(f"{number} - Sexta")
        case "7":
            print(f"{number} - Sábado")
        case _:
            print("valor inválido")


number = get_number()
get_week_day(number)