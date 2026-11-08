from src.config_libraries import config_libraries

def main():
    config_libraries() #Everything from file config_libraries.py
    
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

    active = True
    line = "======================================================"
    while active:
        index = 1
        print(f"{Fore.YELLOW}{line}")
        print(f"{Fore.YELLOW}{index} Configure Project Path"); index += 1
        print(f"{Fore.YELLOW}{index} Generate prompt"); index += 1
        print(f"{Fore.YELLOW}{index} Load prompt template"); index += 1
        print(f"{Fore.YELLOW}{index} Change settings"); index += 1
        print(f"{Fore.YELLOW}0. Exit program"); index += 1
        print(f"{Fore.YELLOW}{line}"); index += 1

        user_choice = input("Enter choice: ")

        match user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "0":
                active = False
            case _:
                print(f"{Fore.RED}[Error] You didn't select an available option. Try again.")


if __name__ == "__main__":
    main()