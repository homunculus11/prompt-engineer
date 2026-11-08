from src.config_libraries import config_libraries

def main():
    config_libraries() #Everything from file config_libraries.py
    
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

    active = True
    line = "======================================================"
    while active:
        print(f"{Fore.YELLOW}{line}")
        print(f"{Fore.YELLOW}1. Generate prompt")
        print(f"{Fore.YELLOW}2. Load prompt template")
        print(f"{Fore.YELLOW}3. Change settings")
        print(f"{Fore.YELLOW}0. Exit program")
        print(f"{Fore.YELLOW}{line}")

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