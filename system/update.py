import os
import sys
import subprocess
import shutil

from utils.colors import *
from core.launcher import launch_new_terminal

REPO_URL = "https://github.com/QuerkyDoodleCreator/BlueShell_Terminal.git"

def update_os():
    print(f"{YELLOW}Updating from GitHub...{RESET}")

    try:
        current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        parent_dir = os.path.dirname(current_dir)
        repo_name = "BlueShell_Terminal"
        repo_path = os.path.join(parent_dir, repo_name)

        # If .git exists → pull
        if os.path.exists(os.path.join(current_dir, ".git")):
            print(f"{CYAN}Existing repo detected. Pulling latest changes...{RESET}")
            subprocess.check_call(["git", "-C", current_dir, "pull"])
            print(f"{GREEN}Update complete!{RESET}")

            launch_new_terminal(sys.argv[0])
            sys.exit()

        # Otherwise → fresh clone
        else:
            print(f"{CYAN}Cloning fresh copy...{RESET}")

            temp_path = repo_path + "_new"

            if os.path.exists(temp_path):
                shutil.rmtree(temp_path)

            subprocess.check_call(["git", "clone", REPO_URL, temp_path])

            # Replace current directory
            backup_path = current_dir + "_old"

            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)

            os.rename(current_dir, backup_path)
            os.rename(temp_path, current_dir)

            print(f"{GREEN}Update complete! Restarting...{RESET}")

            launch_new_terminal(os.path.join(current_dir, "main.py"))
            sys.exit()

    except Exception as e:
        print(f"{RED}Update failed: {e}{RESET}")
