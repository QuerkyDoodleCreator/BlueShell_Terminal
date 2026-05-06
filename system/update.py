import urllib.request, os, sys, subprocess
from config import VERSION, VERSION_CHECK_URL, SCRIPT_URL
from core.launcher import launch_new_terminal
from utils.colors import *

def update_os():
    print(f"{YELLOW}Checking for updates...{RESET}")
    try:
        latest = urllib.request.urlopen(VERSION_CHECK_URL, timeout=5).read().decode().strip()
    except Exception as e:
        print(f"{RED}Failed: {e}{RESET}")
        return

    if latest != VERSION:
        print(f"{CYAN}Update available: {latest}{RESET}")
        if input("Update? [Y/N]: ").lower() == "y":
            try:
                path = os.path.abspath(sys.argv[0])
                temp = path + ".new"

                data = urllib.request.urlopen(SCRIPT_URL).read()
                open(temp, "wb").write(data)

                if os.name == "nt":
                    bat = path + ".updater.bat"
                    open(bat, "w").write(f"""@echo off
timeout /t 2 >nul
move /Y "{temp}" "{path}"
start "" "{sys.executable}" "{path}"
del "%~f0"
""")
                    subprocess.Popen(["cmd", "/c", bat])
                    sys.exit()
                else:
                    os.replace(temp, path)
                    launch_new_terminal(path)
                    sys.exit()

            except Exception as e:
                print(f"{RED}Update failed: {e}{RESET}")
    else:
        print(f"{GREEN}Up to date!{RESET}")
