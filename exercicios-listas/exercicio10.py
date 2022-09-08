list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# list1 = []
# list2 = []


def read_values():
    print("Valores primeira lista : ")
    while len(list1) < 10:
        value = int(input("Lista 1 - informe um valor:"))
        list1.append(value)

    print("Valores segunda lista : ")
    while len(list2) < 10:
        value = int(input("Lista 2 - informe um valor:"))
        list2.append(value)


def join_lists():
    list3 = list(zip(list1, list2))
    print(f"Listas unificadas: {list3}")


read_values()
join_lists()
