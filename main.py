import sys
import time
import random
import datetime
import os
import platform
import subprocess
import urllib.request

if os.name == "nt":
	os.system("")

OSversion = "1.0.3"
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
	print(f"{YELLOW}Checking for updates on GitHub...{RESET}")
	time.sleep(1)

	# URL to raw GitHub file
	download_url = "https://raw.githubusercontent.com/QuerkyDoodleCreator/BlueShell_Terminal/refs/heads/main/directories.py"
	file_name = os.path.basename(__file__)  # The current file name

	try:
		# Download latest version of the script
		urllib.request.urlretrieve(download_url, file_name)
		print(f"{GREEN}Update successful! Rebooting...{RESET}")
		time.sleep(2)
		os.execv(sys.executable, ['python'] + sys.argv)  # Restart script
	except Exception as e:
		print(f"{RED}Update failed: {e}{RESET}")

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
				  f"pwd - Show current directory\n{RESET}")

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
			print(f"{MAGENTA}2025.07.28b{RESET} - {BLUE}Automatic updates using GitHub rpo (must have secure Internet/Ethernet connection){RESET}")
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

		else:
			print(f"{RED}Error!{RESET} Command '{command}' doesn't exist.")
			
			
			
# Final Step - Run the OS
loadOS()
runOS()
