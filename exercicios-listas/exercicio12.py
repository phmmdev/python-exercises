import random

persons = []


def generate_persons_list(quantity):
    for i in range(quantity):
        person = [random.randint(1, 100), random.uniform(1.50, 2.00)]
        persons.append(person)


def calculate_average_height():
    total_heigh = 0
    for person in persons:
        total_heigh += person[1]

    return total_heigh/len(persons)


def count_persons_by_age_and_average_height(age, average_heigt):
    total_persons = 0
    for person in persons:
        if person[0] > age and person[1] < average_heigt:
            total_persons += 1

    print(f"Total: {total_persons}")


generate_persons_list(30)
average_height = calculate_average_height()
count_persons_by_age_and_average_height(13, average_height)
