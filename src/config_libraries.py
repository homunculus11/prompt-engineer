import sys
import subprocess
import json

required_libraries = []
installed_libraries = []
missing_libraries = []

def required():
    json_file = open("/config/settings.json", "r", encoding="utf-8")
    data = json.load(json_file)
    json_file.close()

    for library in data["settings"]["modules"]:
        required_libraries.append(library)

def check():
    json_file = open("/config/settings.json", "r", encoding="utf-8")
    data = json.load(json_file)
    json_file.close()

    for library, status in data["settings"]["modules"].items():
        if status:
            installed_libraries.append(library)

def check_missing():
    for library in required_libraries:
        if library not in installed_libraries:
            missing_libraries.append(library)
    return len(missing_libraries)

def install_missing():
    if not missing_libraries:
        print(f"All libraries are already downloaded {len(required_libraries)}/{len(required_libraries)}. Proceeding back to the program.")
    
    else:
        json_file = open("/config/settings.json", "r", encoding="utf-8")
        data = json.load(json_file)
        json_file.close()

        for library in missing_libraries:
            try:
                __import__(library)
                data["settings"]["modules"][library] = True
            except ImportError:
                print(f"[Error] Library {library} missing.")
                print(f"Installing library {library} now...")
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", library])
                    print(f"[Success] Library {library} was succesfully installed.")
                except subprocess.CalledProcessError as error_description:
                    print(f"[Error] Library {library} failed to install. Error description: {error_description}")

        json_file = open("/config/settings.json", "w", encoding="utf-8")
        json.dump(data, json_file, indent=4)
        json_file.close()