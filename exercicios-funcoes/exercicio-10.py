from random import randint


def main():
    win_values = [7, 11]
    lose_values = [2, 3, 12]
    result = -1
    play_counter = 1
    while result == -1:
        play_result = play()
        print(f"[#{play_counter}] rodada teve resultado: {play_result}")
        result = check_play(play_result, win_values, lose_values)
        if result == -1:
            update_conditions(lose_values, win_values, play_result)
        play_counter += 1

    print(f"Você {'venceu' if result == 1 else 'perdeu'} !!")


def update_conditions(lose_values, win_values, play_result):
    update_win_values(play_result, win_values)
    update_lose_values(lose_values)
    print(f"Seu ponto é: {play_result}, repita para vencer")


def roll_dice():
    return randint(1,6)


def play():
    first_dice = roll_dice()
    second_dice = roll_dice()
    return first_dice + second_dice


def update_win_values(play_result, win_values):
    win_values.clear()
    win_values.append(play_result)


def update_lose_values(lose_values):
    lose_values.clear()
    lose_values.append(7)


def check_play(play_result, win_values, lose_values):
    if play_result in win_values: return 1
    elif play_result in lose_values: return 0
    else: return -1


main()