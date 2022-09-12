OSs = []


def generate_votes_by_OSs():
    for index in range(7):
        OSs.append([index, 0])


def get_votes():
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print("As possíveis respostas são:")
    option = -1
    while option != 0:
        option = int(input(f"""1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
0- Encerrar"""))
        if option in range(1, 7):
            OSs[option][1] += 1
        else:
            print("Informe um valor entre 1 e 6 ou 0 para sair!")


def get_total_votes():
    total = sum(os[1] for os in OSs)
    return total


def calculate_votes_percent(total):
    for os in OSs:
        os.append(round((os[1]/total)*100, 2))


def sort_OSs_vote_list():
    OSs.sort(key=lambda x: x[1], reverse=True)


def show_results(total):
    print("Resultado da votação:")

    print(f"Sistema Operacional     Votos        %")
    print(f"-------------------     -----       ---")
    for os in OSs:
        print(f"{os[0]}                       {os[1]}           {os[2]}")

    print(f"-------------------     -----")
    print(f"Total                   {total}")
    print(f"O Sistema Operacional mais votado foi o {OSs[0][0]}, com {OSs[0][1]} votos, correspondendo a {OSs[0][2]}% dos votos.")


generate_votes_by_OSs()
get_votes()
total = get_total_votes()
calculate_votes_percent(total)
sort_OSs_vote_list()
show_results(total)
