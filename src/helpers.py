import json

def spaces(line, text, bonus_spaces):
    total_spaces = len(line) - len(text) - bonus_spaces
    return " " * total_spaces

def config_path():
    json_file = open("config/settings.json", "r", encoding="utf-8")
    data = json.load(json_file)
    json_file.close()

    print("[Caution] Paste full folder Path")
    print("[Caution] (Example: C:\\Users\\ThisUserIsCool\\Desktop\\MyFolder)")
    data["settings"]["path"] = input("Paste Path Here: ").strip().strip('"').strip("'")

    json_file = open("config/settings.json", "w", encoding="utf-8")
    json.dump(data, json_file, indent=4)
    json_file.close()