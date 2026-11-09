import json
from src.helpers import spaces

def settings_menu():

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
            ...;                                             print(f"   {color_settings}   {line}   ")
            text = "Settings Menu";                          print(f"   {color_settings}{spaces(line, text, -6, 2)}{text}{spaces(line, text, -7, 2)}")
            index = 1;                                       print(f"   {color_settings}   {line}   ")
            text = " ";                                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
            text = "Configure Project Path";                 print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
            if data["settings"]["save_prompts"]:             # Holy mess, ignore this
                text = "Disable Prompt History"
            else:
                text = "Enable prompt history"       
            ...;                                             print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
            text = "Change prompt format (.txt, .MD, both)"; print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
            text = "Change background color";                print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
            text = "Change text color";                      print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
            text = "Change text brightness";                 print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
            text = " ";                                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
            text = "Back to the Main Menu";                  print(f"   {color_settings}   B. {text}{spaces(line, text, 3)}   ");
            text = " ";                                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
            ...;                                             print(f"   {color_settings}   {line}   "); 

            user_choice = input("Enter choice: ")

            match user_choice:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "B" | "b":
                    active = False
                case _:
                    print(f"{Fore.RED}[Error] You didn't select an available option. Try again.")