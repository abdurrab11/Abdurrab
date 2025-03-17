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
{A}              WELCOME TO ABDURRAB TOOLS
{Y}═══════════════════════════════════════════════════
{Y}       [•] Tool Owner    :   ABDURRAB
{Y}       [•] Github        :   ABDURRAB
{Y}       [•] Tool Name     :   ABD TOOLS
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

#----------------------------[MENU]--------------------------------#
def show_menu():
    print(f"{G}[1] {A}File Cloning")
    print(f"{G}[2] {A}Random Cloning")
    print(f"{G}[3] {A}Contact Us")
    print(f"{G}[0] {A}Exit Menu")
    
    choice = input(f"{G}Choose an option: {A}")
    return choice

#----------------------------[FILE CLONING]--------------------------------#
def file_cloning():
    print(f"{G}[+] {A}File Cloning Started...")
    # Add your file cloning logic here

#----------------------------[RANDOM CLONING]--------------------------------#
def random_cloning():
    print(f"{G}[+] {A}Random Cloning Started...")
    # Add your random cloning logic here

#----------------------------[CONTACT US]--------------------------------#
def contact_us():
    print(f"{G}[+] {A}Contact Us:")
    print(f"{G}[•] {A}Email: abdurrab@example.com")
    print(f"{G}[•] {A}Github: https://github.com/abdurrab")

#----------------------------[MAIN FUNCTION]--------------------------------#
def main():
    os.system("clear")
    print(logo)
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            file_cloning()
        elif choice == "2":
            random_cloning()
        elif choice == "3":
            contact_us()
        elif choice == "0":
            print(f"{G}[+] {A}Exiting Tool...")
            break
        else:
            print(f"{R}[!] Invalid Option! Try Again...")

#----------------------------[START]--------------------------------#
if __name__ == "__main__":
    main()