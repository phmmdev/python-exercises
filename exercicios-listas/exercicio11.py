list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list3 = [1, 5, 9, 7, 5, 3, 2, 6, 8, 4]

# list1 = []
# list2 = []
# list3 = []


def read_values(ordem, number_list):
    print(f"Valores {ordem}: ")
    while len(number_list) < 10:
        value = int(input(f"{ordem} - informe um valor:"))
        list1.append(value)


def join_lists():
    list4 = list(zip(list1, list2, list3))
    print(f"Listas unificadas: {list4}")


read_values("primeira lista", list1)
read_values("segunda lista", list2)
read_values("terceira lista", list3)

join_lists()
