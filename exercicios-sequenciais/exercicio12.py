def calculate_weight_by_height(height):
    weight = round((72.7*height) - 58, 2)
    print(f"para a altura {height}, o peso ideal é de {weight}")


calculate_weight_by_height(1.74)
calculate_weight_by_height(1.50)