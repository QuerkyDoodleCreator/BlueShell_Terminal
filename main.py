import sys
import time
import random
import datetime
import os
import subprocess
import urllib.request

VERSION_CHECK_URL = "https://raw.githubusercontent.com/QuerkyDoodleCreator/BlueShell_Terminal/main/version.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/QuerkyDoodleCreator/BlueShell_Terminal/main/main.py"

if os.name == "nt":
    os.system("")

OSversion = "1.0.6"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# --------------------------------- LAUNCH ---------------------------------

def launch_new_terminal(script_path):
    try:
        if os.name == "nt":
            python_exe = sys.executable
            subprocess.Popen(f'start "" "{python_exe}" "{script_path}"', shell=True)
        elif sys.platform == "darwin":
            subprocess.Popen([
                "osascript", "-e",
                f'tell application "Terminal" to do script "{sys.executable} \\"{script_path}\\""'
            ])
        else:
            try:
                subprocess.Popen(["gnome-terminal", "--", sys.executable, script_path])
            except FileNotFoundError:
                subprocess.Popen(["x-terminal-emulator", "-e", f'{sys.executable} "{script_path}"'])
    except Exception as e:
        print(f"{RED}Failed to launch terminal: {e}{RESET}")

# --------------------------------- REBOOT ---------------------------------

def rebootOS():
    print(f"{YELLOW}Rebooting BlueShell Terminal...{RESET}")
    time.sleep(1)

    script_path = os.path.abspath(__file__)
    launch_new_terminal(script_path)

    print(f"{YELLOW}Closing old terminal...{RESET}")
    time.sleep(1)
    sys.exit(0)

# --------------------------------- UPDATE ---------------------------------

def updateOS():
    print(f"{YELLOW}Checking for updates...{RESET}")
    try:
        with urllib.request.urlopen(VERSION_CHECK_URL) as response:
            latest_version = response.read().decode().strip()
    except Exception as e:
        print(f"{RED}Failed to check version: {e}{RESET}")
        return

    if latest_version != OSversion:
        print(f"{CYAN}Update available: {latest_version} (You have {OSversion}){RESET}")
        choice = input(f"{YELLOW}Do you want to update? [Y/N]: {RESET}").strip().lower()

        if choice == "y":
            try:
                script_path = os.path.abspath(__file__)
                temp_path = script_path + ".new"

                # Download new version
                with urllib.request.urlopen(SCRIPT_URL) as response:
                    new_code = response.read()

                with open(temp_path, "wb") as f:
                    f.write(new_code)

                if os.name == "nt":
                    # ---------- WINDOWS SAFE UPDATE ----------
                    updater_path = script_path + ".updater.bat"

                    with open(updater_path, "w") as f:
                        f.write(f"""@echo off
timeout /t 2 >nul
move /Y "{temp_path}" "{script_path}"
start "" "{sys.executable}" "{script_path}"
del "%~f0"
""")

                    print(f"{GREEN}Update ready. Restarting...{RESET}")
                    subprocess.Popen(["cmd", "/c", updater_path])
                    sys.exit(0)

                else:
                    # ---------- LINUX / MAC ----------
                    os.replace(temp_path, script_path)

                    print(f"{GREEN}Update successful! Restarting...{RESET}")
                    time.sleep(1)

                    launch_new_terminal(script_path)
                    sys.exit(0)

            except Exception as e:
                print(f"{RED}Update failed: {e}{RESET}")
        else:
            print(f"{YELLOW}Update cancelled.{RESET}")
    else:
        print(f"{GREEN}You're already on the latest version!{RESET}")

# --------------------------------- LOAD ---------------------------------

def loadOS():
    print(f"{BLUE}Welcome to BlueShell Terminal{RESET}")
    info = input("Would you like a list of every current command? [Y/N] ")

    if info.lower() == "y":
        print(f"{CYAN}BlueShell Terminal Version {OSversion}{RESET}\n"
              f"{MAGENTA}help - Returns commands\n"
              f"sys version - Terminal version\n"
              f"sys reboot - Reboot\n"
              f"sys exit - Exit\n"
              f"sys update - Update\n"
              f"joke tell - Joke\n"
              f"date date/time/datetime\n"
              f"cd / ls / mkdir / pwd\n"
              f"python - Interpreter\n")

# --------------------------------- RUN ---------------------------------

def runOS():
    os.chdir(os.path.expanduser("~"))

    while True:
        cwd = os.getcwd()
        command = input(f"{BOLD}{GREEN}{cwd}{RESET}{BOLD} >>> {RESET}").strip()

        if command in ["help", "?", "h?"]:
            loadOS()

        elif command == "sys version":
            print(f"Terminal Version: {OSversion}")

        elif command == "sys reboot":
            rebootOS()

        elif command == "sys exit":
            print("Terminal shut down successfully.")
            sys.exit(0)

        elif command == "sys update":
            updateOS()

        elif command == "joke tell":
            print(random.choice([
                "Why did the bananas go to the doctor? It wasn’t peeling well.",
                "Why is 6 afraid of 7? Because 7 8 9.",
                "How do you make a tissue dance? Put a little boogie in it!"
            ]))

        elif command == "date date":
            print(datetime.date.today())

        elif command == "date time":
            print(datetime.datetime.now().strftime('%H:%M:%S'))

        elif command == "date datetime":
            print(datetime.datetime.now())

        elif command.startswith("cd "):
            try:
                os.chdir(command[3:].strip())
            except Exception as e:
                print(f"{RED}{e}{RESET}")

        elif command == "ls":
            for f in os.listdir():
                print(f)

        elif command.startswith("mkdir "):
            try:
                os.mkdir(command[6:].strip())
                print(f"{GREEN}Directory created.{RESET}")
            except Exception as e:
                print(f"{RED}{e}{RESET}")

        elif command == "pwd":
            print(os.getcwd())

        elif command == "python":
            print(f"{CYAN}Entering Python mode (exit() to leave){RESET}")
            while True:
                try:
                    code = input(">>> ")
                    if code.strip() == "exit()":
                        break
                    try:
                        result = eval(code)
                        if result is not None:
                            print(result)
                    except SyntaxError:
                        exec(code)
                except Exception as e:
                    print(f"{RED}{e}{RESET}")

        else:
            print(f"{RED}Command not found.{RESET}")

# --------------------------------- START ---------------------------------

loadOS()
runOS()
