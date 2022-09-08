grades = [[10, 5, 7, 9],
          [9, 7, 7, 9],
          [7, 9, 7, 9],
          [8, 0, 7, 9],
          [4, 10, 7, 9],
          [6, 8, 7, 9],
          [7, 5, 7, 9],
          [6, 5, 7, 9],
          [2, 9, 7, 9],
          [5, 5, 7, 9]]

results = []


def calculate_medium_grade():
    for item in grades:
        medium = sum(item)/len(item)
        results.append([medium, item])


def show_results():
    print(f"{results}")


calculate_medium_grade()
show_results()
