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
|   Version  : 3.0 (Termux Fixed)      |
+--------------------------------------+''')

    slowprint(''' \033[93m
[01] python
[02] python2
[03] php
[04] openjdk-17 (java)
[05] git
[06] perl
[07] bash
[08] nano
[09] curl
[10] openssl
[11] openssh
[12] wget
[13] clang
[14] nmap
[15] w3m
[16] hydra
[17] ruby
[18] dnsutils (host command)
[19] net-tools (macchanger alternative)
[20] coreutils
''')

    choice = input("\033[93mDo you want to install all packages [y/n] : ").strip().lower()
    if choice == 'n':
        sys.exit("\n\033[91mExiting...")

    if choice == 'y':
        # Update packages
        os.system("pkg update -y && pkg upgrade -y")

        # Install packages (fixed names)
        packages = [
            "python", "python2", "php", "openjdk-17", "git", "perl", "bash", "nano",
            "curl", "openssl", "openssh", "wget", "clang", "nmap", "w3m", "hydra",
            "ruby", "dnsutils", "net-tools", "coreutils"
        ]

        # Enable repo for hydra if not installed
        os.system("pkg install -y x11-repo")

        os.system("pkg install " + " ".join(packages) + " -y")

        print("\n\033[92mAll packages installed successfully!\n")

        # Welcome message
        print("\033[95m+-------------------------------------------------+")
        slowprint('''\033[95m|             Welcome To HATAN BASIC              |
|         All Basic Packages Installed ✔️          |
|            Your System Is Ready To Use           |''')
        print("+-------------------------------------------------+")

    input("\n\nPress Enter to exit : ")

if __name__ == "__main__":
    main()
