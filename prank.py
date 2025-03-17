import time
import random
import sys

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_hacking_animation():
    symbols = ["/", "-", "\\", "|"]
    for _ in range(20):
        sys.stdout.write(f"\rScanning system... {random.choice(symbols)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nSystem compromised!")

def main_menu():
    typewriter_effect("Welcome to Hacker Advanced Interface v1.0", 0.03)
    typewriter_effect("Type 'help' for available commands.", 0.03)

    while True:
        command = input("\nHAI> ").strip().lower()

        if command == "help":
            typewriter_effect("Available commands:")
            typewriter_effect("  hack - Start hacking simulation")
            typewriter_effect("  exit - Exit the interface")
        elif command == "hack":
            fake_hacking_animation()
            typewriter_effect("Accessing mainframe...")
            time.sleep(1)
            typewriter_effect("Bypassing firewall...")
            time.sleep(1)
            typewriter_effect("Extracting data...")
            time.sleep(1)
            typewriter_effect("Data exfiltration complete!")
        elif command == "exit":
            typewriter_effect("Shutting down Hacker Advanced Interface...")
            time.sleep(1)
            break
        else:
            typewriter_effect("Command not recognized. Type 'help' for available commands.")

if __name__ == "__main__":
    main_menu()