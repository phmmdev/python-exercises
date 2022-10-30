def main():
    populationA = get_population()
    populationB = get_population()

    growthA = get_population_growth()
    growthB = get_population_growth()

    years, final_population = calculate_evolution(populationA, growthA, populationB, growthB)
    print(f"Serão necessários {years} anos para que a população da sociedade A ultrapasse a sociedade B, em {final_population}")


def get_population():
    population = -1
    while population < 0:
        population = int(input("informe o valor da sociedade em questão: "))
        if population < 0:
            print("valor infomado inválido, informe um valor positivo")

    return population


def get_population_growth():
    population_growth = -1
    while population_growth < 0:
        population_growth = float(input("informe a taxa de crescimento da sociedade em questão: "))
        if population_growth < 0:
            print("valor infomado inválido, informe um valor positivo")

    return population_growth


def calculate_evolution(populationA, growthA, populationB, growthB):
    years = 0
    while populationA <= populationB:
        populationA += populationA * growthA
        populationB += populationB * growthB
        years += 1

    return years, round(populationA)


main()
