import sys
import time

OSversion="1.0.1" # Specifies version of terminal

def loadOS(): # Loads the terminal - initial start-up
	print("Welcome to BlueShell Terminal")
	info=input("Would you like a list of every current command? [Y/N] ")
	if info.lower()=="y":
		print(f"BlueShell Terminal Version {OSversion}")
		print("help - returns a list of every command")
		print("sys version - Returns OS version")
		print("sys clear --r - Reboots OS")
		print("sys clear --s - Turns off OS")
		print("sys clear --u - Updates OS")
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
			print(f"BlueShell terminal Version {OSversion}")
			print("help - returns a list of every command")
			print("sys version - Returns OS version")
			print("sys clear --r - Reboots OS")
			print("sys clear --s - Turns off OS")
			print("sys clear --u - Updates OS")
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
