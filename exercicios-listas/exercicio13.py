import random

months = ["Janeiro", "Fevereiro",
          "Março", "Abril",
          "Maio", "Junho",
          "Julho", "Agosto",
          "Setembro", "Outubro",
          "Novembro", "Dezembro"]

months_and_temperatures = []


def generate_temperatures_by_month():
    for count in range(12):
        months_and_temperatures.append([months[count], random.randint(-5, 40)])


def calculate_average_temperature():
    avegare_temperature = 0
    for month in months_and_temperatures:
        avegare_temperature += month[1]

    avegare_temperature = avegare_temperature/12
    return avegare_temperature


def filter_months_by_temperature(average_temperature):
    filtered_months = []
    for month in months_and_temperatures:
        if month[1] > average_temperature:
            filtered_months.append(month)

    return filtered_months


def shows_months(months):
    print(f"{months}")


generate_temperatures_by_month()
average_temperature = calculate_average_temperature()
filtered_months = filter_months_by_temperature(average_temperature)
shows_months(filtered_months)

