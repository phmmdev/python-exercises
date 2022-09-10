import random


salers = []
classification = []
initial_value = 200
final_value = 1000


def generate_salers(min_value, max_value, quantity):
    for count in range(quantity):
        salers.append(random.randint(min_value, max_value))


def set_limits(max_value):
    if max_value <= 1000:
        return 100
    else:
        return int(max_value / 100)


def generate_classification(max_value):
    x = int(max_value / 100)
    for count in range(x):
        classification.append(0)


def define_position(sale, limits):
    return int(sale / limits)


def classify_sales(min_value, max_value, limits):
    for sale in salers:
        for initial_value in range(min_value, max_value, 100):
            if sale in range(initial_value, initial_value+100):
                position = define_position(sale, limits)
                classification[position] += 1


def shows_list(list_to_show):
    print(f"{list_to_show}")


generate_salers(initial_value, final_value, 5)
shows_list(salers)
limits = set_limits(final_value)
generate_classification(final_value)
classify_sales(initial_value, final_value, limits)
shows_list(classification)



