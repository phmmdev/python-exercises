def generate_list(value):
    return list(range(value)) if 0 < value < 1000 else list(range(10))


def get_min(generated_list):
    min_value = generated_list[0]
    for element in generated_list:
        min_value = element if element < min_value else min_value

    return min_value


def get_max(generated_list):
    max_value = generated_list[0]
    for element in generated_list:
        max_value = element if element > max_value else max_value

    return max_value


def sum_list(generated_list):
    total = 0
    for element in generated_list:
        total += element

    return total


default_list = generate_list(10000)
print(get_min(default_list))
print(get_max(default_list))
print(sum_list(default_list))