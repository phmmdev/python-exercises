def get_value_plus_taxes(value, late_days):
    late_days_taxe = 0.03
    taxe_per_day = 0.001

    result = value
    if late_days == 0:
        return result
    else:
        result = round(value + (value * late_days_taxe) + (value * (late_days * taxe_per_day)), 2)
        return result


def interaction():
    option = "S"
    try:
        while(option != "N"):


            option = input("deseja informar mais datas ? [S/N]")
    except Exception as e:
        print(f"Algo de errado ocorreu: {type(e).__name__}, {e}")


interaction()
