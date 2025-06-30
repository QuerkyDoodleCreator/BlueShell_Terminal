import sys
import time
import random
import datetime
import os
import platform
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

def reloadOS():
	print(f"{YELLOW}Checking for updates...{RESET}")
	try:
		with urllib.request.urlopen(VERSION_CHECK_URL) as response:
			latest_version = response.read().decode().strip()
	except Exception as e:
		print(f"{RED}Failed to check version: {e}{RESET}")
		return

	if latest_version != OSversion:
		print(f"{CYAN}Update available: {latest_version} (You have {OSversion}){RESET}")
		choice = input(f"{YELLOW}Do you want to update to version {latest_version}? [Y/N]: {RESET}").strip().lower()
		if choice == "y":
			try:
				# Identify file to overwrite
				script_path = os.path.abspath(__file__)
				print(f"{YELLOW}Downloading new version from GitHub...{RESET}")
				print(f"{BLUE}Replacing current script: {script_path}{RESET}")

				# Download from GitHub and overwrite
				with urllib.request.urlopen(SCRIPT_URL) as response:
					new_code = response.read()

				with open(script_path, "wb") as f:
					f.write(new_code)

				print(f"{GREEN}Update successful! Rebooting...{RESET}")
				time.sleep(2)
				os.execv(sys.executable, ['python'] + sys.argv)
			except Exception as e:
				print(f"{RED}Update failed: {e}{RESET}")
		else:
			print(f"{YELLOW}Update cancelled. Staying on version {OSversion}.{RESET}")
	else:
		print(f"{GREEN}You're already on the latest version ({OSversion})!{RESET}")

def loadOS(): # Loads the terminal - initial start-up
	print(f"{BLUE}Welcome to BlueShellOS {RESET}")
	info=input("Would you like a list of every current command? [Y/N] ")
	if info.lower()=="y":
		print(f"{MAGENTA}BlueShellOS Version {OSversion}\n"
              f"help - Returns a list of every command\n"
              f"sys version - Returns OS version\n"
              f"sys reboot - Reboots OS\n"
              f"sys exit - Turns off OS\n"
              f"sys update - Updates OS\n"
              f"joke tell - Tells a joke\n"
              f"date date - Returns the current date\n"
              f"date time - Returns the current time\n"
              f"date datetime - Returns full date/time\n"
              f"update log - View changelog\n"
              f"cd [dir] - Change directory\n"
              f"ls - List directory contents\n"
              f"mkdir [dir] - Create directory\n"
              f"pwd - Show current directory\n"
              f"py [python code] - Run Python code\n"
              f"python - Enter Python interpereter mode\n"
              f"exit() - Exit Python interpereter mode\n"
              f" {RESET}")
		
	elif info.lower()=="n":
		print(" ")
		
	else:
		print("Invalid selection - assuming option 'N' was chosen.")
		
def runOS():  # Runs the terminal - fully operational from here on out
	os.chdir(os.path.expanduser("~"))  # Set working directory to home
	
	while True:
		cwd = os.getcwd()
		command = input(f"{BOLD}{GREEN}{cwd}{RESET}{BOLD} >>> {RESET}").strip()

		# Help Menu
		if command in ["help", "?", "h?"]:
			print(f"{MAGENTA}BlueShellOS Version {OSversion}\n"
				  f"help - Returns a list of every command\n"
				  f"sys version - Returns OS version\n"
				  f"sys reboot - Reboots OS\n"
				  f"sys exit - Turns off OS\n"
				  f"sys update - Updates OS\n"
				  f"joke tell - Tells a joke\n"
				  f"date date - Returns the current date\n"
				  f"date time - Returns the current time\n"
				  f"date datetime - Returns full date/time\n"
				  f"update log - View changelog\n"
				  f"cd [dir] - Change directory\n"
				  f"ls - List directory contents\n"
				  f"mkdir [dir] - Create directory\n"
				  f"pwd - Show current directory\n"
				  f"py [python code] - Run Python code\n"
				  f"python - Enter Python interpereter mode\n"
				  f"exit() - Exit Python interpereter mode\n"
				  f" {RESET}")

		elif command == "sys version":
			print(f"System Version: {OSversion}")

		elif command == "sys reboot":
			print("\n--------------------------------------------------\n")
			print("REBOOTING OS...")
			time.sleep(5)
			print("\nClosing Software...")
			time.sleep(3.7)
			print("Done")
			time.sleep(4.3)
			print("\nOS REBOOTED SUCCESSFULLY\n")
			print("--------------------------------------------------\n")

		elif command == "sys exit":
			print("OS shut down successfully.")
			sys.exit(0)

		elif command == "sys update":
			print("\n--------------------------------------------------\n")
			print("UPDATING OS\n")
			reloadOS()
			print("\nYou're up to date!\n")
			print("--------------------------------------------------\n")

		elif command == "joke tell":
			jokes = [
				"Why did the bananas go to the doctor? It wasn’t peeling well.",
				"Why is 6 afraid of 7? Because 7 8 9.",
				"How do you make a tissue dance? Put a little boogie in it!",
				"What did the policeman say to his tummy? FREEZE! You’re under a vest.",
				"Where do snowmen keep their money? In a snowbank.",
				"What do you call a nosey pepper? Jalo-penyo business.",
				"Why didn’t the skeleton cross the road? He didn’t have the guts.",
				"What kind of medicine do you give to a pig with a skin rash? Oinkment.",
				"What do you call an alligator in a vest? An in-vest-igator!"
			]
			print(random.choice(jokes))

		elif command == "date date":
			print(f"The current date is {datetime.date.today()}.")

		elif command == "date time":
			print(f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.")

		elif command == "date datetime":
			print(f"The current date and time is {datetime.datetime.now()}.")

		elif command == "update log":
			print(f"{MAGENTA}2025.07.29{RESET} - {BLUE}Terminal can now run Python 3.7.1 code{RESET}")
			print(f"{MAGENTA}2025.07.28b{RESET} - {BLUE}Automatic updates using GitHub repo (must have secure Internet/Ethernet connection){RESET}")
			print(f"{MAGENTA}2025.07.28a{RESET} - {BLUE}Directory commands added, terminal colours added{RESET}")
			print(f"{MAGENTA}2025.07.27{RESET} - {BLUE}BlueShellOS created{RESET}")

		elif command.startswith("cd "):
			path = command[3:].strip()
			try:
				os.chdir(path)
			except FileNotFoundError:
				print(f"{RED}No such directory: {path}{RESET}")
			except NotADirectoryError:
				print(f"{RED}Not a directory: {path}{RESET}")
			except PermissionError:
				print(f"{RED}Permission denied: {path}{RESET}")

		elif command == "ls":
			try:
				files = os.listdir()
				for f in files:
					print(f)
			except Exception as e:
				print(f"{RED}Error listing directory: {e}{RESET}")

		elif command.startswith("mkdir "):
			new_dir = command[6:].strip()
			try:
				os.mkdir(new_dir)
				print(f"{GREEN}Directory '{new_dir}' created successfully.{RESET}")
			except FileExistsError:
				print(f"{YELLOW}Directory already exists: {new_dir}{RESET}")
			except Exception as e:
				print(f"{RED}Error creating directory: {e}{RESET}")

		elif command == "pwd":
			print(os.getcwd())
			
		elif command == "python":
			print(f"{CYAN}Entering Python interpreter mode. Type 'exit()' to return.{RESET}")
			while True:
				try:
					code = input(">>> ")
					if code.strip() == "exit()":
						print(f"{CYAN}Exited Python mode.{RESET}")
						break
					try:
						result = eval(code)
						if result is not None:
							print(result)
					except SyntaxError:
						exec(code)
				except Exception as e:
					print(f"{RED}Python Error: {e}{RESET}")

		else:
			print(f"{RED}Error!{RESET} Command '{command}' does not exist.")
			
			
			
# Final Step - Run the OS
loadOS()
runOS()
