import os
import time
import sys
import random

# Colors for Hacker-Style Look
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

# Fake Loading Animation
def fake_progress(message):
    sys.stdout.write(CYAN + message)
    sys.stdout.flush()
    for _ in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print(" ✅ Done!" + RESET)

# Clear Screen
os.system("clear")

# Display Hacker-Style Header
print(GREEN + """
 █████╗ ██████╗ ██████╗     ██╗   ██╗██████╗     ██████╗  █████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██║   ██║╚════██╗    ██╔══██╗██╔══██╗██╔══██╗
███████║██████╔╝██████╔╝    ██║   ██║ █████╔╝    ██████╔╝███████║██████╔╝
██╔══██║██╔═══╝ ██╔═══╝     ██║   ██║ ╚═══██╗    ██╔═══╝ ██╔══██║██╔═══╝ 
██║  ██║██║     ██║         ╚██████╔╝██████╔╝    ██║     ██║  ██║██║     
╚═╝  ╚═╝╚═╝     ╚═╝          ╚═════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝     
""" + RESET)

print(CYAN + " [👨‍💻] Elite Hacker Panel - ABD UR RAB")
print(" [🔥] Loading Hack Tools...\n" + RESET)
time.sleep(2)

# Fake Menu
print(CYAN + """
 [1] Facebook Hack
 [2] Instagram Hack
 [3] TikTok Hack
 [4] WhatsApp Hack
 [5] Number Data Hack
 [0] Exit
""" + RESET)

# Get User Input
option = input(" Select an option: ")

# Fake Hacking Simulation
if option == "1":
    print(" [🔍] Connecting to Facebook Servers...")
    fake_progress(" [🔄] Initializing Facebook Hack")
    print(RED + " [❌] ERROR! Facebook Firewall Detected!" + RESET)

elif option == "2":
    print(" [🔍] Cracking Instagram Password...")
    fake_progress(" [🔄] Processing Instagram Hack")
    print(RED + " [❌] Access Denied! Instagram Security Too Strong!" + RESET)

elif option == "3":
    print(" [🔍] Exploiting TikTok API...")
    fake_progress(" [🔄] Hacking TikTok Database")
    print(RED + " [❌] Oops! TikTok Detected Suspicious Activity!" + RESET)

elif option == "4":
    print(" [🔍] Intercepting WhatsApp Messages...")
    fake_progress(" [🔄] Decrypting WhatsApp Chats")
    print(RED + " [❌] Encryption Too Strong! Try Again Later!" + RESET)

elif option == "5":
    print(" [🔍] Fetching Number Data from Dark Web...")
    fake_progress(" [🔄] Searching Dark Web Records")
    print(RED + " [❌] FBI WARNING! Illegal Action Detected!" + RESET)

elif option == "0":
    print(" [👋] Exiting... Goodbye!")
    sys.exit()

else:
    print(RED + " [⚠️] Invalid Option! Try Again!" + RESET)