def main():
    percent = 0.015
    salary = 1_000
    first_year = 1995

    fixed_salary = salary + (salary * percent)

    for year in range(1, 2023 - first_year -1):
        print(f"Ano: {first_year + year}, Salário: {fixed_salary}, Percentual: {percent}")

        percent = 2 * percent
        fixed_salary = round(fixed_salary + (fixed_salary * percent), 2)

main()