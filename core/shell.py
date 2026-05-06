import os, sys, platform, subprocess

from utils.colors import *

from system.update import update_os
from system.update_log import show_update_log

from filesystem.file_ops import (
    create_file,
    delete_file,
    read_file,
    write_file
)

from filesystem.navigation import (
    change_dir,
    list_dir,
    make_dir,
    pwd
)

from runtime.python_mode import python_mode
from core.launcher import launch_new_terminal


def run_shell():
    os.chdir(os.path.expanduser("~"))

    while True:
        cmd = input(f"{BOLD}{GREEN}{os.getcwd()}{RESET} >>> ").strip()

        # ---------------- HELP ----------------
        if cmd in ["help", "?"]:
            print(f"""
help
sys update / reboot / exit / info / pyver / pip update
update log - View online changelog
cd / ls / mkdir / pwd
touch / rm / cat / write
python
""")

        # ---------------- SYSTEM ----------------
        elif cmd == "sys exit":
            sys.exit()

        elif cmd == "sys reboot":
            launch_new_terminal(os.path.abspath(sys.argv[0]))
            sys.exit()

        elif cmd == "sys update":
            update_os()

        elif cmd == "update log":
            show_update_log()

        elif cmd == "sys info":
            print(f"""
OS: {platform.system()} {platform.release()}
Python: {platform.python_version()}
Executable: {sys.executable}
""")

        elif cmd == "sys pyver":
            print(platform.python_version())

        elif cmd == "sys pip update":
            subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

        # ---------------- NAVIGATION ----------------
        elif cmd.startswith("cd "):
            try:
                change_dir(cmd[3:])
            except Exception as e:
                print(f"{RED}{e}{RESET}")

        elif cmd == "ls":
            try:
                print("\n".join(list_dir()))
            except Exception as e:
                print(f"{RED}{e}{RESET}")

        elif cmd.startswith("mkdir "):
            try:
                make_dir(cmd[6:])
            except Exception as e:
                print(f"{RED}{e}{RESET}")

        elif cmd == "pwd":
            print(pwd())

        # ---------------- FILE OPS ----------------
        elif cmd.startswith("touch "):
            create_file(cmd[6:])

        elif cmd.startswith("rm "):
            delete_file(cmd[3:])

        elif cmd.startswith("cat "):
            read_file(cmd[4:])

        elif cmd.startswith("write "):
            write_file(cmd[6:])

        # ---------------- PYTHON ----------------
        elif cmd == "python":
            python_mode()

        # ---------------- UNKNOWN ----------------
        else:
            print(f"{RED}Unknown command{RESET}")
