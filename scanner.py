import random
import time
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII Art for the tool
def display_banner():
    print(Fore.GREEN + """
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """)
    print(Fore.CYAN + "Network Scanner and Hacking Tool")
    print(Fore.YELLOW + "===================================")
    print()

# Fake hacking animation
def hacking_animation():
    symbols = ["/", "-", "\\", "|"]
    for _ in range(20):
        sys.stdout.write(Fore.RED + f"\rScanning network... {random.choice(symbols)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(Fore.GREEN + "\nNetwork scan complete!\n")

# Generate a random IP address
def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Simulate IP scanning
def scan_ips():
    print(Fore.BLUE + "[*] Scanning for active IP addresses...\n")
    time.sleep(2)
    active_ips = [generate_ip() for _ in range(random.randint(5, 10))]
    for ip in active_ips:
        print(Fore.GREEN + f"[+] Found active IP: {ip}")
    return active_ips

# Simulate port scanning
def scan_ports(ip):
    print(Fore.BLUE + f"\n[*] Scanning ports for IP: {ip}...\n")
    time.sleep(1)
    open_ports = random.sample(range(1, 1024), random.randint(5, 10))
    for port in open_ports:
        print(Fore.GREEN + f"[+] Port {port} is open")
    return open_ports

# Simulate a fake exploit
def fake_exploit(ip, port):
    print(Fore.BLUE + f"\n[*] Attempting to exploit {ip} on port {port}...\n")
    hacking_animation()
    print(Fore.RED + f"[!] Exploit successful! Gained access to {ip}:{port}\n")

# Main menu
def main_menu():
    display_banner()
    print(Fore.YELLOW + "1. Scan Network for Active IPs")
    print(Fore.YELLOW + "2. Scan Ports for a Specific IP")
    print(Fore.YELLOW + "3. Run Fake Exploit")
    print(Fore.YELLOW + "4. Exit")
    choice = input(Fore.CYAN + "\nEnter your choice: ")
    return choice

# Main function
def main():
    active_ips = []
    while True:
        choice = main_menu()
        if choice == "1":
            active_ips = scan_ips()
        elif choice == "2":
            if not active_ips:
                print(Fore.RED + "\n[!] No active IPs found. Please scan the network first.\n")
            else:
                ip = input(Fore.CYAN + "Enter the IP to scan: ")
                if ip in active_ips:
                    scan_ports(ip)
                else:
                    print(Fore.RED + "\n[!] IP not found in active IP list.\n")
        elif choice == "3":
            if not active_ips:
                print(Fore.RED + "\n[!] No active IPs found. Please scan the network first.\n")
            else:
                ip = input(Fore.CYAN + "Enter the IP to exploit: ")
                if ip in active_ips:
                    port = int(input(Fore.CYAN + "Enter the port to exploit: "))
                    fake_exploit(ip, port)
                else:
                    print(Fore.RED + "\n[!] IP not found in active IP list.\n")
        elif choice == "4":
            print(Fore.RED + "\nExiting the tool. Goodbye!\n")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()