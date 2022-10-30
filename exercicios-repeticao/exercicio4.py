def main():
    populationA = 80000
    populationB = 200000

    growthA = 0.03
    growthB = 0.015

    years, final_population = calculate_evolution(populationA, growthA, populationB, growthB)
    print(f"Serão necessários {years} anos para que a população da sociedade A ultrapasse a sociedade B, em {final_population}")


def calculate_evolution(populationA, growthA, populationB, growthB):
    years = 0
    while populationA <= populationB:
        populationA += populationA * growthA
        populationB += populationB * growthB
        years += 1

    return years, round(populationA)


main()
