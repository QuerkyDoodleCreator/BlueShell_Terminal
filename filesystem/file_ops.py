import os
from utils.colors import *

def create_file(name):
    try:
        open(name, "a").close()
        print(f"{GREEN}Created file: {name}{RESET}")
    except Exception as e:
        print(f"{RED}{e}{RESET}")

def delete_file(name):
    try:
        os.remove(name)
        print(f"{GREEN}Deleted file: {name}{RESET}")
    except Exception as e:
        print(f"{RED}{e}{RESET}")

def read_file(name):
    try:
        with open(name, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"{RED}{e}{RESET}")

def write_file(name):
    try:
        print("Enter text (EOF to save):")
        lines = []
        while True:
            line = input()
            if line == "EOF":
                break
            lines.append(line)
        with open(name, "w") as f:
            f.write("\n".join(lines))
        print(f"{GREEN}Saved to {name}{RESET}")
    except Exception as e:
        print(f"{RED}{e}{RESET}")
