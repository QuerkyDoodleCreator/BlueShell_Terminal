import sys
import time

OSversion="1.0.1" # Specifies version of terminal

def loadOS(): # Loads the terminal - initial start-up
	print("Welcome to BlueShell Terminal")
	print(" BluShell Terminal Copyright (C) 2025 QuerkyDoodleCreator \nThis program comes with ABSOLUTELY NO WARRANTY; for details see GitHub Repository. \nThis is free software, and you are welcome to redistribute it\nunder certain conditions; see GitHub Repository for details. \n[https://github.com/QuerkyDoodleCreator/BlueShell_Terminal/blob/main/LICENSE]")
    
	info=input("Would you like a list of every current command? [Y/N] ")
	if info.lower()=="y":
		print(f"BlueShell Terminal Version {OSversion}")
		print("help - returns a list of every command")
		print("sys version - Returns Terminal version")
		print("sys clear --r - Reboots Terminal")
		print("sys clear --s - Turns off Terminal")
		print("sys clear --u - Updates Terminal")
	elif info.lower()=="n":
		print("")
	else:
		print("Invalid selection - assuming option 'N' was chosen.")
		
def runOS(): # Runs the terminal - fully operational from here on out
	userName=input("Enter your name: ")
	commlineName=userName.lower().split()[0]
	
	while True:
		command=input(f"{commlineName}$blueshell-terminal: ")
		if command=="help":
			print(f"BlueShell Terminal Version {OSversion}")
			print("help - returns a list of every command")
			print("sys version - Returns Terminal version")
			print("sys clear --r - Reboots Terminal")
			print("sys clear --s - Turns off Terminal")
			print("sys clear --u - Updates Terminal")
		elif command=="sys version":
			print(f"System Version: {OSversion}")
		elif command=="sys clear --r":
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			print("REBOOTING OS...")
			print(" ")
			print("--------------------------------------------------")
			print(" ")
		elif command=="sys clear --s":
			print("OS shut down succesfully.")
			sys.exit(0)
		elif command=="sys clear --u":
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			print("UPDATING OS")
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			print("You're up to date!")
