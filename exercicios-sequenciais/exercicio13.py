def calculate_weight_by_height(height):
    male_weight = round((72.7*height) - 58, 2)
    female_weight = round((62.1*height) - 44.7, 2)
    print(f"para a altura {height}, o peso ideal é de um homem é de : {male_weight}")
    print(f"para a altura {height}, o peso ideal é de um mulher é de : {female_weight}")


calculate_weight_by_height(1.74)
calculate_weight_by_height(1.50)