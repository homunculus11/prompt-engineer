import json
from src.config import config_libraries
from src.helpers import spaces

def main():
    config_libraries() # Everything from file config.py
    
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

    active = True
    line = "═" * 46
    while active:
        # Getting the terminal interface colors straight from the .json file (ignore the messy code line -> color_settings)
        json_file = open("config/settings.json", "r", encoding="utf-8")
        data = json.load(json_file)
        json_file.close()
        color_settings = (getattr(Back, data["settings"]["background_color"]) + getattr(Fore, data["settings"]["text_color"]) + getattr(Style, data["settings"]["text_brightness"]))

        # Output (can be done better, but I'm too lazy)
        index = 1;                       print(f"   {color_settings}   {line}   ")
        text = " ";                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
        text = "Configure Project Path"; print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = "Generate prompt";        print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = "Load prompt template";   print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = "Change settings";        print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = " ";                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
        text = "Exit program";           print(f"   {color_settings}   Q. {text}{spaces(line, text, 3)}   ");
        text = " ";                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
        ...;                             print(f"   {color_settings}   {line}   "); 

        user_choice = input("Enter choice: ")

        match user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "Q" | "q":
                active = False
            case _:
                print(f"{Fore.RED}[Error] You didn't select an available option. Try again.")


if __name__ == "__main__":
    main()