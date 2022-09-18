def calculte_salary(hours, value):
    salary = hours * value
    ir = salary * 0.11
    inss = salary * 0.08
    labor_union = salary * 0.05
    salary_descounted = salary - ir - inss - labor_union

    print(f"""
+ Salário Bruto : R$ {salary}
- IR (11%) : R$ {ir}
- INSS (8%) : R$ {inss}
- Sindicato ( 5%) : R$ {labor_union}
= Salário Liquido : R$ {salary_descounted}
""")


calculte_salary(220, 50)
calculte_salary(160, 30.50)