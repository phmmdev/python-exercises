players = []


def generate_votes_by_players():
    for index in range(24):
        players.append([index, 0])


def get_votes():
    print("Enquete: Quem foi o melhor jogador?")
    option = -1
    while option != 0:
        option = int(input(f"Número do jogador (0=fim):"))
        if option in range(1, 24):
            players[option][1] += 1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")


def get_total_votes():
    total = sum(player[1] for player in players)
    return total


def calculate_votes_percent(total):
    for player in players:
        player.append(round((player[1]/total)*100, 2))


def sort_players_vote_list():
    players.sort(key=lambda x: x[1], reverse=True)


def show_results(total):
    print("Resultado da votação:")
    print(f"Foram computados {total} votos.")

    print(f"Jogagar    Votos    %")
    for player in players:
        print(f"{player[0]}    {player[1]}    {player[2]}")

    print(f"O melhor jogador foi o número {players[0][0]}, com {players[0][1]} votos, correspondendo a {players[0][2]}% do total de votos.")


generate_votes_by_players()
get_votes()
total = get_total_votes()
calculate_votes_percent(total)
sort_players_vote_list()
show_results(total)
