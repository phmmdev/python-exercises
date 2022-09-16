import random

status = [[1, "necessita da esfera"],
          [2, "necessita de limpeza"],
          [3, "necessita troca do cabo ou conector"],
          [4, "quebrado ou inutilizado"]]

mouses = []


def get_mouses():
    for count in range(1, 200):
        mouses.append([count, random.choice(status)[0]])


def calculate_result():
    for item in status:
        condition = lambda x: x[1] == item[0]
        total_mouse = sum(condition(mouse) for mouse in mouses)
        item.append(total_mouse)
        item.append(round(total_mouse/len(mouses), 2) * 100)


def show_results():
    print(f"Quantidade e mouse: {len(mouses)}")
    print("""Situação                               Quantidade              Percentual""")
    for item in status:
        print(f"{item[0]}- {item[1]}                {item[2]}               {item[3]}%")


get_mouses()
calculate_result()
show_results()

