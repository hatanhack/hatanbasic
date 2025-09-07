#!/usr/bin/python3
import os
import time
import sys

# Function to clear the screen
def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

# Function for slow printing
def slowprint(s, delay=0.05):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Main program
def main():
    clear_screen()

    print('\033[91mHATANBASIC\033[0m\n')

    print(''' \033[95m
+--------------------------------------+
| This Tool Installs Basic Packages    |
+--------------------------------------+
|   Coded By : hatanhack               |
|   Version  : 2.0                     |
+--------------------------------------+''')

    slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils
[00] termux-setup-storage (for storage access)
''')

    choice = input("\033[93mDo you want to install all packages [y/n] : ").strip().lower()
    if choice == 'n':
        sys.exit("\n\033[91mExiting...")

    if choice == 'y':
        # Update packages
        os.system("pkg update -y && pkg upgrade -y")

        # Install packages
        packages = [
            "python", "python2", "python-dev", "python3", "php", "java", "git",
            "perl", "bash", "nano", "curl", "openssl", "openssh", "wget", "clang",
            "nmap", "w3m", "hydra", "ruby", "macchanger", "host", "dnsutils", "coreutils"
        ]
        os.system("pkg install " + " ".join(packages) + " -y")

        print("\n\033[92mAll packages installed successfully!\n")

        # Setup Termux storage
        input("Press Enter to set up Termux storage (if needed)...")
        os.system("termux-setup-storage")

        # Welcome message
        print("\033[95m+-------------------------------------------------+")
        slowprint('''\033[95m|             Welcome To HATAN BASIC              |
|         All Basic Packages Installed ✔️          |
|            Your System Is Ready To Use           |''')
        print("+-------------------------------------------------+")

    input("\n\nPress Enter to exit : ")

if __name__ == "__main__":
    main()
