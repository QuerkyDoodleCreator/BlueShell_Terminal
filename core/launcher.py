import os, sys, subprocess

def launch_new_terminal(script_path):
    try:
        if os.name == "nt":
            subprocess.Popen(f'start "" "{sys.executable}" "{script_path}"', shell=True)
        elif sys.platform == "darwin":
            subprocess.Popen([
                "osascript", "-e",
                f'tell application "Terminal" to do script "{sys.executable} \\"{script_path}\\""'
            ])
        else:
            subprocess.Popen(["x-terminal-emulator", "-e", f'{sys.executable} "{script_path}"'])
    except Exception as e:
        print(f"Launch failed: {e}")
