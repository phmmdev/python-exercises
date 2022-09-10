questions = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]


def ask_questions():
    print("responda com S (respostas positivas) e N (respostas negativas)")
    answares = []
    for question in questions:
        answares.append(input(question))

    return answares


def rank_answers(answares):
    positive_answares = answares.count("S")
    if positive_answares == 2:
        print("Suspeita")
    elif positive_answares == 3 or positive_answares == 4:
        print("Cumplice")
    elif positive_answares == 5:
        print("Assassino")
    else:
        print("Inocente")


answares = ask_questions()
rank_answers(answares)
