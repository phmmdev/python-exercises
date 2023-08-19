def sum_elements(n1, n2, n3):
    return sum([n1, n2, n3])


def sum_variation(*args):
    total = sum(args)
    return total


print(sum_elements(1,2,3))
print(sum_variation(1, 2, 3, 4, 5))
