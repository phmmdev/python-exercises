

name = "Pedro Henrique Marcon  de Moraes"
jumps = [6.5, 6.1, 6.2, 5.4, 5.3]


def calculate_average_jum_distance(jumps):
    return round(sum(jumps)/len(jumps), 2)


def shows_result(name, jumps, average_jump_distance):

    print(f"Atleta: {name}")

    print(f"""Primeiro Salto: {jumps[0]} m
Segundo Salto: {jumps[1]} m
Terceiro Salto: {jumps[2]} m
Quarto Salto: {jumps[3]} m
Quinto Salto: {jumps[4]} m
""")

    print(f"""Resultado final:
    
Atleta: {name}
Saltos: {str(jumps)[1:-1].replace(',', ' -')}
Média dos saltos: {average_jump_distance} m""")


average_jump_distance = calculate_average_jum_distance(jumps)
shows_result(name, jumps, average_jump_distance)