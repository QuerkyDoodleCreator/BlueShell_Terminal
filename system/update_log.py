import urllib.request
from config import UPDATELOG_URL
from utils.colors import *

def show_update_log():
    print(f"{YELLOW}Fetching update log...{RESET}")
    try:
        with urllib.request.urlopen(UPDATELOG_URL, timeout=5) as response:
            log = response.read().decode()

        print(f"{CYAN}{BOLD}\n[UPDATE LOG]{RESET}")
        print(log)

    except Exception as e:
        print(f"{RED}Failed: {e}{RESET}")
