import sys
import subprocess
import json

required_libraries = []

def required():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        