from utils.colors import *

def python_mode():
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
