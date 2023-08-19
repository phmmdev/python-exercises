users_usage_rawslice = [["alexandre", "456123789"],
                ["anderson", "1245698456"],
                ["antonio", "123456456"],
                ["carlos", "91257581"],
                ["cesar", "987458"],
                ["rosemary", "789456125"]]

users_usage_refined = []


def process_list():
    mb_unity = 1024**2
    total_usage_mb = sum(int(item[1]) for item in users_usage_raw)/(mb_unity)
    for index, item in enumerate(users_usage_raw):
        mb_usage = int(item[1])/mb_unity
        users_usage_refined.append([index, item[0], round(mb_usage, 2), round(mb_usage/total_usage_mb * 100, 2)])

    return total_usage_mb, round(total_usage_mb/len(users_usage_raw), 2)


def get_result(total_usage, average_usage):
    print("ACME Inc.               Uso do espaço em disco pelos usuários")
    print("------------------------------------------------------------------------")
    print("Nr.  Usuário        Espaço utilizado     % do uso")
    for item in users_usage_refined:
        print(f"{item[0]}    {item[1]}       {item[2]} MB             {item[3]}%")

    print(f"""Espaço total ocupado: {total_usage} MB
Espaço médio ocupado: {average_usage} MB""")


total_usage, average_usage = process_list()
get_result(total_usage, average_usage)
