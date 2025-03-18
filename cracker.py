import random
import time
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII Art for the tool
def display_banner():
    print(Fore.GREEN + """
    ██████╗  █████╗ ███████╗███████╗ ██████╗ ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ██████╔╝███████║███████╗███████╗██║   ██║██████╔╝█████╗  
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══██╗██╔══╝  
    ██║     ██║  ██║███████║███████║╚██████╔╝██║  ██║███████╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """)
    print(Fore.CYAN + "Password Cracking Tool")
    print(Fore.YELLOW + "=========================")
    print()

# Fake cracking animation
def cracking_animation():
    symbols = ["/", "-", "\\", "|"]
    for _ in range(20):
        sys.stdout.write(Fore.RED + f"\rCracking password... {random.choice(symbols)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(Fore.GREEN + "\nPassword cracked!\n")

# Simulate brute-force attack
def brute_force_attack():
    print(Fore.BLUE + "[*] Starting brute-force attack...\n")
    time.sleep(2)
    cracking_animation()
    password = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(6))
    print(Fore.GREEN + f"[+] Password found: {password}\n")

# Simulate dictionary attack
def dictionary_attack():
    print(Fore.BLUE + "[*] Starting dictionary attack...\n")
    time.sleep(2)
    cracking_animation()
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    password = random.choice(common_passwords)
    print(Fore.GREEN + f"[+] Password found: {password}\n")

# Simulate a fake exploit
def fake_exploit():
    print(Fore.BLUE + "[*] Attempting to exploit the system...\n")
    cracking_animation()
    print(Fore.RED + "[!] Exploit successful! Gained access to the system.\n")

# Main menu
def main_menu():
    display_banner()
    print(Fore.YELLOW + "1. Brute-Force Attack")
    print(Fore.YELLOW + "2. Dictionary Attack")
    print(Fore.YELLOW + "3. Run Fake Exploit")
    print(Fore.YELLOW + "4. Exit")
    choice = input(Fore.CYAN + "\nEnter your choice: ")
    return choice

# Main function
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            brute_force_attack()
        elif choice == "2":
            dictionary_attack()
        elif choice == "3":
            fake_exploit()
        elif choice == "4":
            print(Fore.RED + "\nExiting the tool. Goodbye!\n")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()