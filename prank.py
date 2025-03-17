#!/bin/bash

# Fake Hacking Script for Prank
# Coded by: ABD UR RAB
# Just for fun! No real hacking.

clear

echo -e "\e[32m"
echo " █████╗ ██████╗ ██████╗     ██╗   ██╗██████╗     ██████╗  █████╗ ██████╗ "
echo "██╔══██╗██╔══██╗██╔══██╗    ██║   ██║╚════██╗    ██╔══██╗██╔══██╗██╔══██╗"
echo "███████║██████╔╝██████╔╝    ██║   ██║ █████╔╝    ██████╔╝███████║██████╔╝"
echo "██╔══██║██╔═══╝ ██╔═══╝     ██║   ██║ ╚═══██╗    ██╔═══╝ ██╔══██║██╔═══╝ "
echo "██║  ██║██║     ██║         ╚██████╔╝██████╔╝    ██║     ██║  ██║██║     "
echo "╚═╝  ╚═╝╚═╝     ╚═╝          ╚═════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝     "
echo -e "\e[0m"
echo " [👨‍💻] Elite Hacker Panel - ABD UR RAB"
echo " [🔥] Loading Hack Tools..."
sleep 3

# Fake Menu
echo -e "\e[36m"
echo " [1] Facebook Hack"
echo " [2] Instagram Hack"
echo " [3] TikTok Hack"
echo " [4] WhatsApp Hack"
echo " [5] Number Data Hack"
echo " [0] Exit"
echo -e "\e[0m"

read -p " Select an option: " option

# Fake Progress Animation
fake_progress() {
    echo -ne " [🔄] Initializing"
    for i in {1..5}; do
        echo -ne "."
        sleep 1
    done
    echo -e " ✅ Done!\n"
}

# Fake Hacking Simulation
case $option in
    1)
        echo " [🔍] Connecting to Facebook Servers..."
        fake_progress
        echo -e "\e[31m [❌] ERROR! Facebook Firewall Detected!\e[0m"
        ;;
    2)
        echo " [🔍] Cracking Instagram Password..."
        fake_progress
        echo -e "\e[31m [❌] Access Denied! Instagram Security Too Strong!\e[0m"
        ;;
    3)
        echo " [🔍] Exploiting TikTok API..."
        fake_progress
        echo -e "\e[31m [❌] Oops! TikTok Detected Suspicious Activity!\e[0m"
        ;;
    4)
        echo " [🔍] Intercepting WhatsApp Messages..."
        fake_progress
        echo -e "\e[31m [❌] Encryption Too Strong! Try Again Later!\e[0m"
        ;;
    5)
        echo " [🔍] Fetching Number Data from Dark Web..."
        fake_progress
        echo -e "\e[31m [❌] FBI WARNING! Illegal Action Detected!\e[0m"
        ;;
    0)
        echo " [👋] Exiting... Goodbye!"
        exit
        ;;
    *)
        echo " [⚠️] Invalid Option! Try Again!"
        ;;
esac