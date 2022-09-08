list1 = []


def read_values():
    while len(list1) < 10:
        value = int(input("informe um valor:"))
        list1.append(value)


def show_reversed_list():
    print(list1[::-1])


read_values()
show_reversed_list()