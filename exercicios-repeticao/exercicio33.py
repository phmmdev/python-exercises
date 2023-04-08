import random

def main():
    temperatures = generate_temperature()
    print(f"Maior temperatura: {get_max_temperature(temperatures)}º")
    print(f"Maior temperatura: {get_min_temperature(temperatures)}º")
    print(f"Média temperatura: {get_avg_temperature(temperatures)}º")

def generate_temperature():
    temperatures = []
    for i in range(random.randint(1, 100)):
        temperatures.append(random.randint(0, 40))

    return temperatures


def get_max_temperature(temperatures):
    return max(temperatures)


def get_min_temperature(temperatures):
    return min(temperatures)


def get_avg_temperature(temperatures):
    temperature_total = 0
    for temp in temperatures:
        temperature_total += temp

    return round(temperature_total / len(temperatures), 1)


main()
