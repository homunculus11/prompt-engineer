import json
from src.helpers import spaces, config_path
from colorama import init, Fore, Back, Style
init(autoreset=True)

json_file = open("config/settings.json", "r", encoding="utf-8")
data = json.load(json_file)
json_file.close()

def colors_menu():
    ...

def format_menu():

    active = True
    line = "═" * 46

    while active:
        # Getting the terminal interface colors straight from the .json file (ignore the messy code line -> color_settings)
        color_settings = (getattr(Back, data["settings"]["background_color"]) + getattr(Fore, data["settings"]["text_color"]) + getattr(Style, data["settings"]["text_brightness"]))

        # Output (can be done better, but I'm too lazy)
        ...;                                             print(f"   {color_settings}   {line}   ")
        text = "Choose File Format";                     print(f"   {color_settings}{spaces(line, text, -6, 2)}{text}{spaces(line, text, -7, 2)}")
        index = 1;                                       print(f"   {color_settings}   {line}   ")
        text = " ";                                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
        text = ".txt (Text File Format)";                print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = ".md (MarkDown File Format)";             print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = "Both (Both File Formats)";               print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = "Copy to clipboard";                      print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
        text = " ";                                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
        text = "Back to the Main Menu";                  print(f"   {color_settings}   B. {text}{spaces(line, text, 3)}   ");
        text = " ";                                      print(f"   {color_settings}   {text}{spaces(line, text, 0)}   "); # Newline
        ...;                                             print(f"   {color_settings}   {line}   "); 

        user_choice = input("Enter choice: ")

        match user_choice:
            case "1":
                data["settings"]["prompt_format"] = ".txt"
                print("[Success] Successfully changed prompt format to be saved as .txt.") # Needs a format change
            case "2":
                data["settings"]["prompt_format"] = ".md"
                print("[Success] Successfully changed prompt format to be saved as .md.") # Needs a format change
            case "3":
                data["settings"]["prompt_format"] = "both"
                print("[Success] Successfully changed prompt format to be saved as both .md and .txt.") # Needs a format change
            case "4":
                data["settings"]["prompt_format"] = "clipboard"
                print("[Success] Successfully changed prompt format to be saved to clipboard only.") # Needs a format change
            case "B" | "b":
                active = False
            case _:
                print(f"{Fore.RED}[Error] You didn't select an available option. Try again.")


def settings_menu():

    active = True
    line = "═" * 46

    while active:
        # Getting the terminal interface colors straight from the .json file (ignore the messy code line -> color_settings)
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
        text = "Change prompt format (.txt, .md, both)"; print(f"   {color_settings}   {index}. {text}{spaces(line, text, 3)}   "); index += 1
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
                config_path()
            case "2":
                if data["settings"]["save_prompts"]:
                    data["settings"]["save_prompts"] = False
                    print("[Success] Successfully disabled prompt history.") # Needs a format change
                else:
                    data["settings"]["save_prompts"] = True
                    print("[Success] Successfully enabled prompt history.") # Needs a format change
            case "3":
                format_menu()
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

    json_file = open("config/settings.json", "w", encoding="utf-8")
    json.dump(data, json_file, indent=4)
    json_file.close()
            