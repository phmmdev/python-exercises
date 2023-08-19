from random import randrange


def main():
    sequences = {}
    for i in range(100000):
        sequence = generate_sequences()
        if is_magic_square(sequence):
            sequences[i] = sequence

    print(sequences)

def generate_sequences():
    sequence = []
    option = list(range(1, 10))
    for i in range(9):
        random_index = randrange(len(option))
        sequence.append(option[random_index])
        option.pop(random_index)

    return sequence


def is_magic_square(sequence):
    if (sequence[0] + sequence[1] + sequence[2]) == (sequence[3] + sequence[4] + sequence[5]) == (sequence[6] + sequence[7] + sequence[8]):
        if (sequence[0] + sequence[3] + sequence[6]) == (sequence[1] + sequence[4] + sequence[7]) == (sequence[2] + sequence[5] + sequence[8]):
            if (sequence[0] + sequence[4] + sequence[8]) == (sequence[2] + sequence[4] + sequence[6]):
                return True
    return False


main()
