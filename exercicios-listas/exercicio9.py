# people = [[22, 1.74], [29, 1.73], [18, 1.60], [15, 1.70], [30, 1.80]]
people = []


def get_people_data():
    while len(people) < 5:
        person_data = input("informe idade e altura (separados por espaço): ").split()
        people.append(person_data)


def show_reversed_order():
    people.reverse()
    print(f"{people}")


get_people_data()
show_reversed_order()

