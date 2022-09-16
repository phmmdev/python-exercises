import random

dice_values = list(range(1, 7))
result = []


def rolls_dices():
    for count in range(100):
        result.append(random.choice(dice_values))


def show_result():
    for side in dice_values:
        print(f"{side} - numero de vezes: {result.count(side)}")


rolls_dices()
show_result()
