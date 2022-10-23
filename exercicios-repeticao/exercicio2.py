def main():
    get_user_password()


def get_user_password():
    check_user_password = False
    while not check_user_password:
        user =  input("informe o nome do usuário")
        password = input("informe a senha")

        if user == password or (user and password) is None or (user and password):
            check_user_password = False
            print("usuário e senha não podem ser identicos")
        else:
            check_user_password = True
            print("acesso liberado")


main()

