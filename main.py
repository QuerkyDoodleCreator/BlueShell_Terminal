import sys
import time
import random
import datetime
import os
import subprocess
import urllib.request
import platform

VERSION_CHECK_URL = "https://raw.githubusercontent.com/QuerkyDoodleCreator/BlueShell_Terminal/main/version.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/QuerkyDoodleCreator/BlueShell_Terminal/main/main.py"
UPDATELOG_URL = "https://raw.githubusercontent.com/QuerkyDoodleCreator/BlueShell_Terminal/refs/heads/main/updatelog.txt"

if os.name == "nt":
	os.system("")

OSversion = "1.1.1"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ---------------- LAUNCH ----------------

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
		print(f"{RED}Launch failed: {e}{RESET}")

# ---------------- UPDATE ----------------

def updateOS():
	print(f"{YELLOW}Checking for updates...{RESET}")
	try:
		latest = urllib.request.urlopen(VERSION_CHECK_URL, timeout=5).read().decode().strip()
	except Exception as e:
		print(f"{RED}Failed: {e}{RESET}")
		return

	if latest != OSversion:
		print(f"{CYAN}Update available: {latest}{RESET}")
		if input("Update? [Y/N]: ").lower() == "y":
			try:
				path = os.path.abspath(__file__)
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

# ---------------- UPDATE LOG ----------------

def show_update_log():
	print(f"{YELLOW}Fetching update log...{RESET}")
	try:
		with urllib.request.urlopen(UPDATELOG_URL, timeout=5) as response:
			log = response.read().decode()

		print(f"{CYAN}\n--- Update Log ---{RESET}")
		print(log)

	except Exception as e:
		print(f"{RED}Failed to fetch update log: {e}{RESET}")

# ---------------- UTILITIES ----------------

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
		print("Enter text (type 'EOF' on new line to save):")
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

# ---------------- MAIN LOOP ----------------

def runOS():
	os.chdir(os.path.expanduser("~"))

	while True:
		cmd = input(f"{BOLD}{GREEN}{os.getcwd()}{RESET} >>> ").strip()

		if cmd in ["help", "?"]:
			print(f"""
help
sys update / reboot / exit / info / pyver / pip update
update log - View online changelog
cd / ls / mkdir / pwd
touch / rm / cat / write
python
""")

		elif cmd == "sys exit":
			sys.exit()

		elif cmd == "sys reboot":
			launch_new_terminal(os.path.abspath(__file__))
			sys.exit()

		elif cmd == "sys update":
			updateOS()

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

		elif cmd.startswith("cd "):
			try:
				os.chdir(cmd[3:])
			except Exception as e:
				print(e)

		elif cmd == "ls":
			print("\n".join(os.listdir()))

		elif cmd.startswith("mkdir "):
			try:
				os.mkdir(cmd[6:])
			except Exception as e:
				print(e)

		elif cmd == "pwd":
			print(os.getcwd())

		elif cmd.startswith("touch "):
			create_file(cmd[6:])

		elif cmd.startswith("rm "):
			delete_file(cmd[3:])

		elif cmd.startswith("cat "):
			read_file(cmd[4:])

		elif cmd.startswith("write "):
			write_file(cmd[6:])

		elif cmd == "python":
			print(f"{CYAN}Entering Python mode (exit() to leave){RESET}")
			while True:
				try:
					code = input(">>> ")
					if code == "exit()":
						break
					try:
						result = eval(code)
						if result is not None:
							print(result)
					except:
						exec(code)
				except Exception as e:
					print(f"{RED}{e}{RESET}")

		else:
			print(f"{RED}Unknown command{RESET}")

# ---------------- START ----------------

print(f"{BLUE}BlueShell Terminal {OSversion}{RESET}")
runOS()
