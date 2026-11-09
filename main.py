from src.config import config_libraries
from src.helpers import spaces

def main():
    config_libraries() #Everything from file config.py
    
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

    active = True
    line = "======================================================"
    while active:
        
        index = 1;                       print(f"{Fore.BLACK}{Back.CYAN}{line}")
        text = "Configure Project Path"; print(f"{Fore.BLACK}{Back.CYAN}{index}. {text}{spaces(line, text, 3)}"); index += 1
        text = "Generate prompt";        print(f"{Fore.BLACK}{Back.CYAN}{index}. {text}{spaces(line, text, 3)}"); index += 1
        text = "Load prompt template";   print(f"{Fore.BLACK}{Back.CYAN}{index}. {text}{spaces(line, text, 3)}"); index += 1
        text = "Change settings";        print(f"{Fore.BLACK}{Back.CYAN}{index}. {text}{spaces(line, text, 3)}"); index += 1
        text = "Exit program";           print(f"{Fore.BLACK}{Back.CYAN}0. {text}{spaces(line, text, 3)}");       index += 1
        ...;                             print(f"{Fore.BLACK}{Back.CYAN}{line}");                                 index += 1

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