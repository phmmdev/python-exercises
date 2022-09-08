list1 = []


def read_values():
    while len(list1) < 5:
        value = int(input("informe um valor:"))
        list1.append(value)


def show_list():
    print(list1)


read_values()
show_list()
