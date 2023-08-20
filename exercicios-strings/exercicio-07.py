def main():
    string = input("informe uma frase")
    spaces = string.count(" ")
    vowels = [string.count(x) for x in "aeiou"]
    print(f"espaços encontrados: {spaces}")
    print(f"vogais encontradas: {sum(vowels)}")

main()
