import sys
import subprocess
import json

required_libraries = []
installed_libraries = []
missing_libraries = []

def required():
    json_file = open("config/settings.json", "r", encoding="utf-8")
    data = json.load(json_file)

    for library_name in data["settings"]["modules"]:
        required_libraries.append(library_name)

    json_file.close()

def check():
    json_file = open("config/settings.json", "r", encoding="utf-8")
    data = json.load(json_file)

    for library_name, status in data["settings"]["modules"].items():
        if status:
            installed_libraries.append(library_name)

    json_file.close()

def check_missing():
    for library_name in required_libraries:
        if library_name not in installed_libraries:
            missing_libraries.append(library_name)