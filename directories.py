import sys
import time
import random
import datetime
import os
import platform

OSversion = "1.0.2"
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
	time.sleep(5)
	print(f"{YELLOW}Gathering appropriet files from https://github.com/QuerkyDoodleCreator/BlueShell_Terminal...{RESET}")
	time.sleep(1)
	print(f"{GREEN}Done{RESET}")
	time.sleep(9)
	print(f"{YELLOW}Removing bloatware...{RESET}")
	time.sleep(1)
	print(f"{GREEN}Done{RESET}")

def loadOS(): # Loads the terminal - initial start-up
	print(f"{BLUE}Welcome to BlueShellOS {RESET}")
	info=input("Would you like a list of every current command? [Y/N] ")
	if info.lower()=="y":
		print(f"{MAGENTA}BlueShellOS Version {OSversion} \nhelp - Returns a list of every command \nsys version - Returns OS version \nsys clear --r - Reboots OS \nexit - Turns off OS \nsys clear --u - Updates OS \njoke tell - Tells a joke \ndate date - Returns the current date \ndate time - Returns the current time \ndate datetime - Returns the exact current date and time \nupdate log - Returns a list of every update ever made to the OS\n {RESET}")
		
	elif info.lower()=="n":
		print(" ")
		
	else:
		print("Invalid selection - assuming option 'N' was chosen.")
		
def runOS(): # Runs the terminal - fully operational from here on out
	userName=input("Enter your name: ")
	commlineName=userName.lower().split()[0]
	
	while True:
		command=input(f"{BOLD}{GREEN}{commlineName}@blueshell-terminal{RESET}:{BLUE}~ ${RESET} ") # Command Line!
		if command=="help" or command=="?" or command =="h?":
			print(f"{MAGENTA}BlueShellOS Version {OSversion} \nhelp - Returns a list of every command \nsys version - Returns OS version \nsys clear --r - Reboots OS \nexit - Turns off OS \nsys clear --u - Updates OS \njoke tell - Tells a joke \ndate date - Returns the current date \ndate time - Returns the current time \ndate datetime - Returns the exact current date and time \nupdate log - Returns a list of every update ever made to the OS\n {RESET}")
			
		elif command=="sys version":
			print(f"System Version: {OSversion}")
			
		elif command=="sys clear --r":
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			print("REBOOTING OS...")
			time.sleep(5)
			print(" ")
			print("Closing Software...")
			time.sleep(3.7)
			print("Done")
			time.sleep(4.3)
			print(" ")
			print("OS REBOOTED SUCCESFULLY")
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			
		elif command=="exit":
			print("OS shut down succesfully.")
			sys.exit(0)
			
		elif command=="sys clear --u":
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			print("UPDATING OS")
			print(" ")
			reloadOS()
			print(" ")
			print("--------------------------------------------------")
			print(" ")
			print("You're up to date!")
			
		elif command=="joke tell":
			jokes = ["Why did the bananas go to the doctor. It wasn’t peeling well.", "Why is 6 afraid of 7? Because 7 8 9.", "How do you make a tissue dance? Put a little boogie in it!", "What did the policeman say to his tummy? FREEZE! You’re under a vest.", "Where do snowmen keep their money? In a snowbank.", "What do you call a nosey pepper? Jalo-penyo business.", "Why didn’t the skeleton cross the road? He didn’t have the guts.", "What kind of medicine do you give to a pig with a skin rash? Oinkment.", "What do you call an alligator in a vest? An in-vest-igator!"]
			joke = random.choice(jokes)
			print(joke)
			
		elif command=="date date":
			current_date = datetime.date.today()
			print(f"The current date is {current_date}.")
			
		elif command=="date time":
			current_datetime = datetime.datetime.now()
			current_time = current_datetime.strftime("%H:%M:%S")
			print(f"The current time is {current_time}.")
			
		elif command=="date datetime":
			current_datetime = datetime.datetime.now()
			print(f"The current date and time is {current_datetime}.")
			
		elif command=="update log":
			# to add a log, insert a print() statement ABOVE all other print statements! Use this format: print(f"{MAGENTA}YYYY.MM.DD{RESET} - {BLUE}Update here{RESET}")
			print(f"{MAGENTA}2025.07.28{RESET} - {BLUE}Terminal colours added, new commands created.{RESET}")
			print(f"{MAGENTA}2025.07.27{RESET} - {BLUE}BlueShellOS created{RESET}")
			
		else:
			print(f"{RED}Error!{RESET} Command '{command}' doesn't exist.")
