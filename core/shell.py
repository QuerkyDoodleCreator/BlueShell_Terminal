import os, sys, platform, subprocess

from utils.colors import *
from system.update import update_os
from system.update_log import show_update_log
from filesystem.file_ops import *
from filesystem.navigation import *
from runtime.python_mode import python_mode
from core.launcher import launch_new_terminal

def run_shell():
    os.chdir(os.path.expanduser("~"))

    while True:
        cmd = input(f"{BOLD}{GREEN}{os.getcwd()}{RESET} >>> ").strip()

        if cmd in ["help", "?"]:
            print("help, sys update, sys exit, sys reboot, update log, ls, cd, mkdir, python")

        elif cmd == "sys exit":
            sys.exit()

        elif cmd == "sys reboot":
            launch_new_terminal(os.path.abspath(sys.argv[0]))
            sys.exit()

        elif cmd == "sys update":
            update_os()

        elif cmd == "update log":
            show_update_log()

        elif cmd == "ls":
            print("\n".join(list_dir()))

        elif cmd.startswith("cd "):
            try:
                change_dir(cmd[3:])
            except Exception as e:
                print(e)

        elif cmd.startswith("mkdir "):
            make_dir(cmd[6:])

        elif cmd == "pwd":
            print(pwd())

        elif cmd.startswith("touch "):
            create_file(cmd[6:])

        elif cmd.startswith("rm "):
            delete_file(cmd[3:])

        elif cmd.startswith("cat "):
            read_file(cmd[4:])

        elif cmd.startswith("write "):
            write_file(cmd[6:])

        elif cmd == "python":
            python_mode()

        else:
            print(f"{RED}Unknown command{RESET}")
