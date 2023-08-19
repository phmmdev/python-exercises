from re import compile


def is_time_format(input):
    time_re = compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
    return bool(time_re.match(input))


def convert_format_hour(hours):
    try:
        hour, minutes = str(hours).split(":")
        hour = int(hour)
        if hour >= 12:
            result = abs(int(hour) - 12)
            return f"{result}:{minutes}"
        else:
            return f"{hours}"
    except Exception as e:
        print(f"Algo de errado ocorreu: {type(e).__name__}, {e}")


def print_hour(hours,  period):
        print(hours + (" A.M" if period == "A" else " P.M"))


def interaction():

    option = "S"
    try:
        while(option != "N"):
            hours = input("informe as horas para ser convertidas: ")
            period = input("informe o periodo das horas A = AM, P = PM: ")

            if is_time_format(hours) and period in ("A", "P"):
                result = convert_format_hour(hours)
                print_hour(result, period)
            else:
                print("Formato ou opção informada inválida")

            option = input("deseja informar mais datas ? [S/N]")
    except Exception as e:
        print(f"Algo de errado ocorreu: {type(e).__name__}, {e}")


interaction()
